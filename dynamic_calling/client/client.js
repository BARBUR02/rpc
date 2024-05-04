
import { Ice } from "ice";

async function main() {
    const communicator = Ice.initialize();
    const base = communicator.stringToProxy("DynamicUserService:default -p 10000");

    console.log(userService)
    console.log(typeof userService)
    console.log(userService.constructor.name)
    console.log(userService.ice_toString)
    console.log(userService.ice_invoke)
    console.log(userService.ice_twoway)
    console.log(userService.ice_connectionCached)
    console.log(userService.ice_invocationTimeout)

    const result1 = await base.ice_invoke("sayHello", [], null);
    console.log("Result from sayHello:", result1);

    const result2 = await base.ice_invoke("getUsers", [], null);
    console.log("Result from getUsers:", result2);

    const userData = { name: "Jakub", age: 21 };
    await base.ice_invoke("addUser", [userData], null);
    console.log("User 'Jakub' added successfully.");

    const result3 = await base.ice_invoke("getUsers", [], null);
    console.log("Result from getUsers after adding user:", result3);

    await base.ice_invoke("processUserList", [result3], null);
    console.log("User list processed successfully.");


    communicator.destroy();
}

main().catch((error) => {
    console.error("Error:", error);
});
