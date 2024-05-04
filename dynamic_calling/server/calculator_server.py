from math import inf
import Ice
from servants.calculator_service import DynamicCalculatorI


with Ice.initialize() as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints(
        "DynamicCalculatorAdapter", "default -p 10000"
    )
    object = DynamicCalculatorI()
    adapter.add(object, communicator.stringToIdentity("DynamicCalculatorAdapter"))
    adapter.activate()
    communicator.waitForShutdown()
