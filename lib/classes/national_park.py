class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise Exception("Name cannot be changed!")
        else:
            self._name = value
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        pass
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        pass
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass

