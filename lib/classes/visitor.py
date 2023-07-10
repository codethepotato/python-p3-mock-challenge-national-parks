class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise Exception("Name must be between 1 and 15 characters.")
        self._name = value

    def trips(self, new_trip=None):
        from classes.trip import Trip
        pass
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        pass