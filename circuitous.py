''' Circuitous(tm) -- An Advanced Circle Analytics Company '''

from math import pi, tan, radians, sqrt  # Modules are a tool for code re-use
from collections import namedtuple # Tool for self-documenting tuples

Version = namedtuple('Version', ['major', 'minor'])

class Circle(object):            # Inherit capabilities of new-style classes (property, staticmethod, classmethod)
    'An advanced circle analytics toolkit'      # Document as you go.

    __slots__ = ['diameter']     # Implement the Flyweight Design Pattern by suppressing the instance dictionary to save space

    version = Version(0, 11)     # Class variables stored in the dict, shared by all instances

    def __init__(self, radius):  # Parameter names are use visible, so make the clear
        self.radius = radius     # Instance variable -- the data should be unique to the instance

    def area(self):              # Regular method has "self" as the first argument
        'Perform quadrature for planar shape of uniform revolution'
        p = self.__perimeter()    # Self could a Tire, so this COULD call the WRONG perimeter, so we use the backup copy
        radius = p / 2.0 / pi
        return pi * radius ** 2.0

    def perimeter(self):
        'Compute the closed line integral for the 2-D locus of points equidistant from a given point'
        return 2.0 * pi * self.radius

    __perimeter = perimeter      # Name mangle the backup copy to _Circle__perimeter, class local references

    def __repr__(self):          # "self" means you OR your children
        return '%s(%r)' % (self.__class__.__name__, self.radius)

    @staticmethod               # Reprograms the dot to NOT add "self" as the first argument
    def angle_to_grade(angle):  # use case for staticmethods is to add regular functions to classes to improve findability
        'Convert an inclinometer reading in degrees to a percent grade'
        return tan(radians(angle)) * 100.0    

    @classmethod                # Reprogams the dot to add "cls" as the first argument
    def from_bbd(cls, bbd):     # use for classmethod is to provide alternative constructors
        'Construct a circle from a bounding box diagonal'
        radius = bbd / 2.0 / sqrt(2.0)
        return cls(radius)    

    @property                   # Reprograms the dot convert attribute access into method access
    def radius(self):           # Use case is computed fields
        'Computed field which half of the diameter'
        return self.diameter / 2.0

    @radius.setter              # Reprograms the dot to convert attribute updates to setter calls
    def radius(self, radius):   # Use case is managed attributes
        self.diameter = radius * 2.0
