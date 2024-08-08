"""
Silver Service Taxi - CP1404 Practical 9
Alex Williams
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Create a special taxi that includes flagfall and fancy pricing."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Create silver service instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Calculate fare price including flagfall."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return a string that shows the distance and flagfall price."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
