from generated import Demo


class DynamicCalculatorI(Demo.Calc):
    def add(self, a, b, current=None):
        print("inside add")
        return a + b

    def subtract(self, a, b, current=None):
        print("inside subtract")
        return a - b

    def avg(self, a: list[float], current=None):
        print("inside avg")
        avg = sum(a) / (len(a) if a else 1)
        return avg
