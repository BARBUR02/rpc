from math import inf
import Ice
from servants.user_service import DynamicUserServiceI


with Ice.initialize() as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints(
        "SimplePrinterAdapter", "default -p 10000"
    )
    object = DynamicUserServiceI()
    adapter.add(object, communicator.stringToIdentity("DynamicUserService"))
    adapter.activate()
    communicator.waitForShutdown()
