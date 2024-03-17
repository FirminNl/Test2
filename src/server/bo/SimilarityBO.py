from .BusinessObjectBO import BusinessObject

"""
Klasse Profilaeehnlichkeit mit einfachen Methoden zum Setzen der Klassenvariablen

"""


class Similarity(BusinessObject):
    """Klasse Profilaehnlichkeit"""
    def __init__(self): 
        super().__init__()
        self._matching_id = 0
        self._score = 0

        
    def set_matching_id(self, matching_id):
        """setzen Vorschlag id"""
        self._matching_id = matching_id
        
    def get_matching_id(self):
        """auslesen Vorschlag id"""
        return self._matching_id
    
    
    def set_score(self, score):
        """setzen score der Vorschlag Profile"""
        self._score = score
        
    def get_score(self):
        """auslesen score der Vorschlagprofile"""
        return self._score
    
    
    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "Similarity: {}, {}, {}, {}".format(
            self.get_id(),
            self.get_timestamp(),
            self.get_matching_id(),
            self.get_score()
        
        )
    
    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Aehnlichkeit Objekt()."""
        obj = Similarity()
        obj.set_id(dictionary["id"])
        obj.set_timestamp(dictionary["timestamp"])
        obj.set_matching_id(dictionary["matching_id"])
        obj.set_score(dictionary["score"])
        return obj
