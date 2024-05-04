import Ice
import sys

from generated import UserService

# Ice.loadSlice("path/to/user_service.ice")  # Load the Slice definitions

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("DynamicUserService:default -p 10000")

    try:
        [ok, outParams] = base.ice_invoke("sayHello", Ice.OperationMode.Normal, b"")
        if ok:
            print("Successfull call!")
        else:
            print("User exception")
    except Ice.LocalException as ex:
        print(ex)

    try:
        [ok, outParams] = base.ice_invoke("getUsers", Ice.OperationMode.Normal, b"")
        if ok:
            print("Successfull call!")
            print(outParams)
        else:
            print("User exception")
            print(outParams)
    except Ice.LocalException as ex:
        print(ex)

    try:
        # [ok, outParams] = base.ice_invoke(
        #     "addUser",
        #     Ice.OperationMode.Normal,
        #     str(UserService.UserData(name="Jakub", age=21)).encode(),
        # )
        [ok, outParams] = base.ice_invoke(
            "addUser",
            Ice.OperationMode.Normal,
            "".encode(),
        )

        if ok:
            print("Successfull call!")
            print(outParams)
        else:
            print("User exception")
            print(outParams)
    except Ice.LocalException as ex:
        print(ex)

    # Call methods on the servant object via the proxy
    # result = userService.sayHello()
    # print("Result from sayHello:", result)

    # result = userService.getUsers()
    # print("Result from getUsers:", result)

    # userService.addUser(UserService.UserData(name="Jakub", age=21))
    # # {"name": "Jakub", "age": 21}

    # result = userService.getUsers()
    # print("Result from getUsers after adding user:", result)

    # userService.processUserList(result)

    # You can call other methods similarly
