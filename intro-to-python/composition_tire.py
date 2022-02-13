import math

class Tire:
    """
    Tire represents a tire that would be used with an automobile
    """

    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction 
    
    def circumference(self):
        """
        The circumference of the tire of the inches
        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        slide_wall_inches = (self.width * (self.ratio / 100)) / 25.4
        total_diameter = slide_wall_inches * 2 + self.diameter
        return round(total_diameter * math.pi, 1)


    def __repr__(self):
        """
        Represent the tire information in the standard notation present
        on the side of the tire. Example: 'p215/65r15'
        """

        return (f"{self.tire_type}{self.width}/{self.ratio}"
                + f"{self.construction}{self.diameter}")


    