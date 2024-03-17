from server.bo.BusinessObjectBO import BusinessObject

"""
Klasse SearchProfile mit einfachen Methoden zum Setzen der Klassenvariablen

"""


class SearchProfile(BusinessObject):
    """Class for SearchProfile"""

    def __init__(self):
        super().__init__()
        self._userprofile_id = 0

    def set_userprofile_id(self, userprofile_id):
        """Setzen der userprofile id"""
        self._userprofile_id = userprofile_id

    def get_userprofile_id(self):
        """get the userprofile id"""
        return self._userprofile_id

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "UserProfile: {}, {}, {}".format(
            self.get_id(),
            self.get_timestamp(),
            self.get_userprofile_id(),
        )

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein UserProfile()."""
        obj = SearchProfile()
        obj.set_id(dictionary["id"])
        obj.set_timestamp(dictionary["timestamp"])
        obj.set_userprofile_id(dictionary["userprofile_id"])
        return obj





