class Track:
    """
    Class representing a track
    """

    def __init__(self, name: str, city: str, country: str, length_km: float):
        """
        Initialize a Track instance.

        :param name: Name of the track
        :type name: str
        :param city: City where the track is located
        :type city: str
        :param length_km: Length of the track in kilometers
        :type length_km: float
        """
        self.name: str = name
        self.city: str = city
        self.country: str = country
        self.length_km: float = length_km
