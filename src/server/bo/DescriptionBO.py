from .BusinessObjectBO import BusinessObject

"""
Klasse Beschreibung mit einfachen Methoden zum Setzen der Klassenvariablen

"""


class Description(BusinessObject):
    """Class for Beschreibungs"""
    def __init__(self): 
        super().__init__()
        self._characteristic_id = 0
        self._answer = ""
        self._max_answer = ""

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

    def set_max_answer(self, max_answer):
        """setzen Antwort"""
        self._max_answer = max_answer

    def get_max_answer(self):
        """auslesen Antwort"""
        return self._max_answer


    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "Description: {}, {}, {}, {}, {} , {}".format(
            self.get_id(),
            self.get_timestamp(),
            self.get_characteristic_id(),
            self.get_answer(),
            self.get_max_answer(),
        )

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Beschreibung()."""
        obj = Description()
        obj.set_id(dictionary["id"])
        obj.set_timestamp(dictionary["timestamp"])
        obj.set_characteristic_id(dictionary["characteristic_id"])
        obj.set_answer(dictionary["answer"])
        obj.set_max_answer(dictionary["max_answer"])
        return obj
        




