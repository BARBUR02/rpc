# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.10
#
# <auto-generated>
#
# Generated from file `user_service.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module UserService
_M_UserService = Ice.openModule("generated.UserService")
__name__ = "UserService"

if "UserData" not in _M_UserService.__dict__:
    _M_UserService.UserData = Ice.createTempClass()

    class UserData(object):
        def __init__(self, name="", age=0):
            self.name = name
            self.age = age

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.name)
            _h = 5 * _h + Ice.getHash(self.age)
            return _h % 0x7FFFFFFF

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_UserService.UserData):
                return NotImplemented
            else:
                if self.name is None or other.name is None:
                    if self.name != other.name:
                        return -1 if self.name is None else 1
                else:
                    if self.name < other.name:
                        return -1
                    elif self.name > other.name:
                        return 1
                if self.age is None or other.age is None:
                    if self.age != other.age:
                        return -1 if self.age is None else 1
                else:
                    if self.age < other.age:
                        return -1
                    elif self.age > other.age:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_UserService._t_UserData)

        __repr__ = __str__

    _M_UserService._t_UserData = IcePy.defineStruct(
        "::UserService::UserData",
        UserData,
        (),
        (("name", (), IcePy._t_string), ("age", (), IcePy._t_int)),
    )

    _M_UserService.UserData = UserData
    del UserData

if "_t_Users" not in _M_UserService.__dict__:
    _M_UserService._t_Users = IcePy.defineSequence(
        "::UserService::Users", (), _M_UserService._t_UserData
    )

_M_UserService._t_DynamicUserService = IcePy.defineValue(
    "::UserService::DynamicUserService", Ice.Value, -1, (), False, True, None, ()
)

if "DynamicUserServicePrx" not in _M_UserService.__dict__:
    _M_UserService.DynamicUserServicePrx = Ice.createTempClass()

    class DynamicUserServicePrx(Ice.ObjectPrx):

        def sayHello(self, context=None):
            return _M_UserService.DynamicUserService._op_sayHello.invoke(
                self, ((), context)
            )

        def sayHelloAsync(self, context=None):
            return _M_UserService.DynamicUserService._op_sayHello.invokeAsync(
                self, ((), context)
            )

        def begin_sayHello(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_UserService.DynamicUserService._op_sayHello.begin(
                self, ((), _response, _ex, _sent, context)
            )

        def end_sayHello(self, _r):
            return _M_UserService.DynamicUserService._op_sayHello.end(self, _r)

        def addUser(self, userData, context=None):
            return _M_UserService.DynamicUserService._op_addUser.invoke(
                self, ((userData,), context)
            )

        def addUserAsync(self, userData, context=None):
            return _M_UserService.DynamicUserService._op_addUser.invokeAsync(
                self, ((userData,), context)
            )

        def begin_addUser(
            self, userData, _response=None, _ex=None, _sent=None, context=None
        ):
            return _M_UserService.DynamicUserService._op_addUser.begin(
                self, ((userData,), _response, _ex, _sent, context)
            )

        def end_addUser(self, _r):
            return _M_UserService.DynamicUserService._op_addUser.end(self, _r)

        def getUsers(self, context=None):
            return _M_UserService.DynamicUserService._op_getUsers.invoke(
                self, ((), context)
            )

        def getUsersAsync(self, context=None):
            return _M_UserService.DynamicUserService._op_getUsers.invokeAsync(
                self, ((), context)
            )

        def begin_getUsers(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_UserService.DynamicUserService._op_getUsers.begin(
                self, ((), _response, _ex, _sent, context)
            )

        def end_getUsers(self, _r):
            return _M_UserService.DynamicUserService._op_getUsers.end(self, _r)

        def processUserList(self, userList, context=None):
            return _M_UserService.DynamicUserService._op_processUserList.invoke(
                self, ((userList,), context)
            )

        def processUserListAsync(self, userList, context=None):
            return _M_UserService.DynamicUserService._op_processUserList.invokeAsync(
                self, ((userList,), context)
            )

        def begin_processUserList(
            self, userList, _response=None, _ex=None, _sent=None, context=None
        ):
            return _M_UserService.DynamicUserService._op_processUserList.begin(
                self, ((userList,), _response, _ex, _sent, context)
            )

        def end_processUserList(self, _r):
            return _M_UserService.DynamicUserService._op_processUserList.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_UserService.DynamicUserServicePrx.ice_checkedCast(
                proxy, "::UserService::DynamicUserService", facetOrContext, context
            )

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_UserService.DynamicUserServicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return "::UserService::DynamicUserService"

    _M_UserService._t_DynamicUserServicePrx = IcePy.defineProxy(
        "::UserService::DynamicUserService", DynamicUserServicePrx
    )

    _M_UserService.DynamicUserServicePrx = DynamicUserServicePrx
    del DynamicUserServicePrx

    _M_UserService.DynamicUserService = Ice.createTempClass()

    class DynamicUserService(Ice.Object):

        def ice_ids(self, current=None):
            return ("::Ice::Object", "::UserService::DynamicUserService")

        def ice_id(self, current=None):
            return "::UserService::DynamicUserService"

        @staticmethod
        def ice_staticId():
            return "::UserService::DynamicUserService"

        def sayHello(self, current=None):
            raise NotImplementedError("servant method 'sayHello' not implemented")

        def addUser(self, userData, current=None):
            raise NotImplementedError("servant method 'addUser' not implemented")

        def getUsers(self, current=None):
            raise NotImplementedError("servant method 'getUsers' not implemented")

        def processUserList(self, userList, current=None):
            raise NotImplementedError(
                "servant method 'processUserList' not implemented"
            )

        def __str__(self):
            return IcePy.stringify(self, _M_UserService._t_DynamicUserServiceDisp)

        __repr__ = __str__

    _M_UserService._t_DynamicUserServiceDisp = IcePy.defineClass(
        "::UserService::DynamicUserService", DynamicUserService, (), None, ()
    )
    DynamicUserService._ice_type = _M_UserService._t_DynamicUserServiceDisp

    DynamicUserService._op_sayHello = IcePy.Operation(
        "sayHello",
        Ice.OperationMode.Normal,
        Ice.OperationMode.Normal,
        False,
        None,
        (),
        (),
        (),
        None,
        (),
    )
    DynamicUserService._op_addUser = IcePy.Operation(
        "addUser",
        Ice.OperationMode.Normal,
        Ice.OperationMode.Normal,
        False,
        None,
        (),
        (((), _M_UserService._t_UserData, False, 0),),
        (),
        None,
        (),
    )
    DynamicUserService._op_getUsers = IcePy.Operation(
        "getUsers",
        Ice.OperationMode.Normal,
        Ice.OperationMode.Normal,
        False,
        None,
        (),
        (),
        (),
        ((), _M_UserService._t_Users, False, 0),
        (),
    )
    DynamicUserService._op_processUserList = IcePy.Operation(
        "processUserList",
        Ice.OperationMode.Normal,
        Ice.OperationMode.Normal,
        False,
        None,
        (),
        (((), _M_UserService._t_Users, False, 0),),
        (),
        None,
        (),
    )

    _M_UserService.DynamicUserService = DynamicUserService
    del DynamicUserService

# End of module UserService
