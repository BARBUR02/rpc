import Ice
import sys

from generated import UserService

# Ice.loadSlice("path/to/user_service.ice")  # Load the Slice definitions

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("DynamicUserService:default -p 10000")
    userService = UserService.DynamicUserServicePrx.checkedCast(base)

    if not userService:
        raise RuntimeError("Invalid proxy")

    # Call methods on the servant object via the proxy
    result = userService.sayHello()
    print("Result from sayHello:", result)

    result = userService.getUsers()
    print("Result from getUsers:", result)

    userService.addUser(UserService.UserData(name="Jakub", age=21))
    # {"name": "Jakub", "age": 21}

    result = userService.getUsers()
    print("Result from getUsers after adding user:", result)

    userService.processUserList(result)

    # You can call other methods similarly
