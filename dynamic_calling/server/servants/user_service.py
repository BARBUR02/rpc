# import UserService
from generated import UserService

from math import inf

users: list[UserService.UserData] = []


class DynamicUserServiceI(UserService.DynamicUserService):
    def sayHello(self, current=None):
        print("Inside sayHello")
        return "Hello"

    def addUser(self, userData: UserService.UserData, current=None):
        print(userData)
        users.append(userData)

    def getUsers(self, current=None):
        return users

    def processUserList(self, userList: list[UserService.UserData], current=None):
        oldest_user, youngest_user = None, None
        oldest_age, youngest_age = -inf, +inf
        avg_age = 0
        for user in userList:
            if user.age > oldest_age:
                oldest_user = user
            if user.age < youngest_age:
                youngest_user = user
            avg_age += user.age

        if userList:
            avg_age = avg_age / len(userList)

        print(f"Received users: {userList}")
        print(f"\tAverage age: {avg_age}")
        print(f"\tOldest user: {oldest_user.name}")
        print(f"\tYoungest user: {youngest_user.name}")
