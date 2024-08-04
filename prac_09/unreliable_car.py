"""
Unreliable Car
CP1404 - Practical 9
Alex Williams
"""

import random
from car import Car


class UnreliableCar(Car):
    """Create an unreliable car."""
    def __init__(self, name, fuel, reliability):
        """Make an unreliable car instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive a car if it is reliable enough to start."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
