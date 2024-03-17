from .BusinessObjectBO import BusinessObject

"""
Klasse Auswahl mit einfachen Methoden zum Setzen der Klassenvariablen

"""


class Selection(BusinessObject):
    """Klasse Auswahl"""
    def __init__(self): 
        super().__init__()
        self._characteristic_id = 0
        self.answer = ""
        
        
    def set_characteristic_id(self, characteristic_id):
        """setzen Eigenschafts id"""
        self._characteristic_id = characteristic_id
        
    def get_characteristic_id(self):
        """auslesen Eigenschafts id"""
        return self._characteristic_id
    
    def set_answer(self, answer):
        """setzen Antwort"""
        self._answer = answer
        
    def get_answer(self):
        """auslesen Antwort"""
        return self._answer
    
    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "Selection: {}, {}, {}, {}".format(
            self.get_id(),
            self.get_timestamp(),
            self.get_characteristic_id(),
            self.get_answer(),
        )

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Auswahl()."""
        obj = Selection()
        obj.set_id(dictionary["id"])
        obj.set_timestamp(dictionary["timestamp"])
        obj.set_characteristic_id(dictionary["characteristic_id"])
        obj.set_answer(dictionary["answer"])
        return obj
