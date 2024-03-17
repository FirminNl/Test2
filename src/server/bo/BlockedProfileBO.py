from server.bo.BusinessObjectBO import BusinessObject

"""
Klasse geblockte Profile mit einfachen Methoden zum Setzen der Klassenvariablen

"""

class BlockedProfile(BusinessObject):
    """Klasse Blocked Profile"""
    def __init__(self): 
        super().__init__()
        self._userprofile_id = 0
        self._blockeduser_id = 0

    def set_userprofile_id(self, userprofile_id):
        """Setzen der userprofile id"""
        self._userprofile_id = userprofile_id

    def get_userprofile_id(self):
        """get the userprofile id"""
        return self._userprofile_id

    def set_blockeduser_id(self, blockeduser_id):
        """Setzen der blockeduser id"""
        self._blockeduser_id = blockeduser_id

    def get_blockeduser_id(self):
        """get the blockeduser id"""
        return self._blockeduser_id

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "BlockedProfile: {}, {}, {}, {}".format(
            self.get_id(),
            self.get_timestamp(),
            self.get_userprofile_id(),
            self.get_blockeduser_id(),
        )

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein geblocktes Profil Objekt()."""
        obj = BlockedProfile()
        obj.set_id(dictionary["id"])
        obj.set_timestamp(dictionary["timestamp"])
        obj.set_userprofile_id(dictionary["userprofile_id"])
        obj.set_blockeduser_id(dictionary["blockeduser_id"])
        return obj
        


