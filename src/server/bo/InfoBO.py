from .BusinessObjectBO import BusinessObject

"""
Klasse Info-Objekt mit einfachen Methoden zum Setzen der Klassenvariablen

"""


class Info(BusinessObject):
    """Klasse Info"""

    def __init__(self):
        super().__init__()
        self._userprofile_id = 0
        self._answer_id = 0
        self._is_selection = False
        self._is_searchprofile = False

    def set_userprofile_id(self, userprofile_id):
        self._userprofile_id = userprofile_id

    def get_userprofile_id(self):
        return self._userprofile_id

    def set_answer_id(self, answer_id):
        """setzen Antwort"""
        self._answer_id = answer_id

    def get_answer_id(self):
        """auslesen Antwort"""
        return self._answer_id

    def set_is_selection(self, is_selection):
        """setzen ist_Auswahl"""
        self._is_selection = is_selection

    def get_is_selection(self):
        """auslesen ist_Auswahl"""
        return self._is_selection

    def set_is_searchprofile(self, is_searchprofile):
        """setzen ist_Suchprofil"""
        self._is_searchprofile = is_searchprofile

    def get_is_searchprofile(self):
        """auslesen ist_Suchprofile"""
        return self._is_searchprofile

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "Description: {}, {}, {}, {}, {}, {}".format(
            self.get_id(),
            self.get_timestamp(),
            self.get_userprofile_id(),
            self.get_answer_id(),
            self.get_is_selection,
            self.get_is_searchprofile()
        )

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Info-Objekt()."""
        obj = Info()
        obj.set_id(dictionary["id"])
        obj.set_timestamp(dictionary["timestamp"])
        obj.set_userprofile_id(dictionary["userprofile_id"])
        obj.set_answer_id(dictionary["answer_id"])
        obj.set_is_selection(dictionary["is_selection"])
        obj.set_is_searchprofile(dictionary["is_searchprofile"])
        return obj





