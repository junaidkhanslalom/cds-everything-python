class Car:
    """
    Car models a car w/ tires and enginer
    """

    """
    When we create a new instance
    Instance of my car
    What needs to be passed in when we call car
    """
    def __init__(self, engine, tires):
        """
        Docstring describe the methods
        """
        self.engine = engine
        self.tires = tires
    
    def description(self):
        print(f"A car with an {self.engine} and {self.tires}")
    
    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0