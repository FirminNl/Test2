from .BusinessObjectBO import BusinessObject

"""
Klasse Eigenschaft mit einfachen Methoden zum Setzen der Klassenvariablen

"""


class Characteristic(BusinessObject):
    """Class Eigenschaft mit einfachen Methoden zum"""
    def __init__(self): 
        super().__init__()
        self._name = ""  
        self._description = ""
        self._is_selection = False
        self._author_id = 0
        self._is_standart = False
        
        
    def set_characteristic_id(self, email):
        """Setzen der Eigenschafts id"""
        self._email = email
        
    def get_characteristic_id(self):
        """auslesen Eigenschafts id"""
        return self._characteristic_id
    
    def set_name(self, name):
        """setzen Name"""
        self._name = name
        
    def get_name(self):
        """auslesen Name"""
        return self._name
    
    
    def set_description(self, description):
        """setzen default"""
        self._description = description
        
    def get_description(self):
        """auslesen default"""
        return self._description

    def set_is_selection(self, is_selection):
        """setzen ist_Auswahl"""
        self._is_selection = is_selection

    def get_is_selection(self):
        """auslesen ist_Auswahl"""
        return self._is_selection

    def set_author_id(self, author_id):
        """Setzen der author id"""
        self._author_id = author_id

    def get_author_id(self):
        """get the author id"""
        return self._author_id
    
    def set_is_standart(self, is_standart):
        """Setzen der author id"""
        self._is_standart = is_standart

    def get_is_standart(self):
        """get the author id"""
        return self._is_standart


    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "characteristic: {}, {}, {}, {}, {}, {}".format(
            self.get_id(),
            self.get_timestamp(),
            self.get_name(),
            self.get_description(),
            self.get_is_selection(),
            self.get_author_id(),
            self.get_is_standart(),
        )

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Eigenschaftsobjekt()."""
        obj = Characteristic()
        obj.set_id(dictionary["id"])
        obj.set_timestamp(dictionary["timestamp"])
        obj.set_name(dictionary["name"])
        obj.set_description(dictionary["description"])
        obj.set_is_selection(dictionary["is_selection"])
        obj.set_author_id(dictionary["author_id"])
        obj.set_is_standart(dictionary["is_standart"])
        
        return obj
        




