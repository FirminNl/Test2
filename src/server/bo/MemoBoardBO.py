from server.bo.BusinessObjectBO import BusinessObject

"""
Klasse Merkzettel mit einfachen Methoden zum Setzen der Klassenvariablen

"""


class MemoBoard(BusinessObject):
    """Klasse Merkzettel"""
    def __init__(self): 
        super().__init__()
        self._userprofile_id = 0
        self._saved_id = 0

    def set_userprofile_id(self, userprofile_id):
        """Setzen der userprofile id"""
        self._userprofile_id = userprofile_id

    def get_userprofile_id(self):
        """get the userprofile id"""
        return self._userprofile_id

    def set_saved_id(self, saved_id):
        """setzen Saved id"""
        self._saved_id = saved_id

    def get_saved_id(self):
        """auslesen Saved id"""
        return self._saved_id



    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "MemoBoard: {}, {}, {}".format(
            self.get_id(),
            self.get_timestamp(),
            self.get_userprofile_id(),
            self.get_saved_id(),
            
        
        )

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Merkzettel Profil Objekt()."""
        obj = MemoBoard()
        obj.set_id(dictionary["id"])
        obj.set_timestamp(dictionary["timestamp"])
        obj.set_userprofile_id(dictionary["userprofile_id"])
        obj.set_saved_id(dictionary["saved_id"])
        return obj
        


