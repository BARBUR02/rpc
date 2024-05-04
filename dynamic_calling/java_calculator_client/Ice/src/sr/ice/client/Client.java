package sr.ice.client;

import com.zeroc.Ice.*;
import com.zeroc.Ice.Object;

import java.lang.Exception;
import java.util.Scanner;


public class Client {

    public static void main(String[] args) {
        Communicator communicator = null;
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        try {
            communicator = Util.initialize(args);
            ObjectPrx proxy = communicator.stringToProxy("DynamicCalculatorAdapter:tcp -h 127.0.0.1 -p 10000 -z : udp -h 127.0.0.1 -p 10000 -z");

            while (running) {
                System.out.print("> ");
                String input = scanner.nextLine();
                String[] arguments = input.split("\\s+");

                if (arguments[0].isEmpty()) {
                    continue;
                }

                var os = new OutputStream();

                switch (arguments[0]) {
                    case "add", "subtract" -> {
                        os.startEncapsulation();
                        os.writeInt(Integer.parseInt(arguments[1]));
                        os.writeInt(Integer.parseInt(arguments[2]));
                        os.endEncapsulation();
                    }
                    case "avg" -> {
                        os.startEncapsulation();
                        if (arguments.length > 1) {
                            long[] arr = new long[arguments.length - 1];
                            for (int i = 1; i < arguments.length; i++) {
                                arr[i - 1] = Long.parseLong(arguments[i]);
                            }
                            os.writeLongSeq(arr);
                        } else {
                            os.writeLongSeq(new long[0]);
                        }
                        os.endEncapsulation();
                    }
                    case "quit" -> running = false;
                    default -> {
                        System.out.println("Command not supported");
                        continue;
                    }
                }

                if (!running){
                    break;
                }
                Object.Ice_invokeResult r = proxy.ice_invoke(arguments[0], OperationMode.Normal, os.finished());

                if(r.returnValue) {
                    var is = new InputStream(communicator, r.outParams);
                    is.startEncapsulation();
                    switch (arguments[0]) {
                        case "add", "subtract" -> System.out.println("result: " + is.readInt());
                        case "avg" -> System.out.println("result " + is.readDouble());
                    }
                    try {
                        is.endEncapsulation();
                    } catch (EncapsulationException ignored){
                    }
                }
                else {
                    try {
                        var is = new InputStream(communicator, r.outParams);
                        is.startEncapsulation();
                        is.throwException();
                        is.endEncapsulation();
                    } catch (com.zeroc.Ice.UnknownUserException e) {
                        e.printStackTrace();
                    }
                }
            }

        } catch (LocalException e) {
            e.printStackTrace();
            System.exit(1);
        } catch (Exception e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
        if (communicator != null) { //clean
            try {
                communicator.destroy();
            } catch (Exception e) {
                System.err.println(e.getMessage());
                System.exit(1);
            }
        }
        System.exit(0);
    }
}

