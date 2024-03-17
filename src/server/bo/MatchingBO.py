from server.bo.BusinessObjectBO import BusinessObject

"""
Klasse Vorschlag mit einfachen Methoden zum Setzen der Klassenvariablen

"""


class Matching(BusinessObject):
    """Klasse Vorschlag"""
    def __init__(self): 
        super().__init__()
        self._userprofile_id = 0
        self._candidateprofile_id = 0
        self._unseen_profile = False
        
    
    def set_userprofile_id(self, userprofile_id):
        """setzen Nutzerprofile id"""
        self._userprofile_id = userprofile_id
        
    def get_userprofile_id(self):
        """auslesen Nutzerprofile id"""
        return self._userprofile_id
    
    def set_candidateprofile_id(self, candidateprofile_id):
        """setzen Kandidatenprofile"""
        self._candidateprofile_id = candidateprofile_id
        
    def get_candidateprofile_id(self):
        """auslesen Kandidatenprofil id"""
        return self._candidateprofile_id
    
    def set_unseen_profile(self, unseen_profile):
        """setzen nicht angesehene Profile"""
        self._unseen_profile = unseen_profile
        
    def get_unseen_profile(self):
        """auslesen nicht angesehene Profile"""
        return self._unseen_profile
    
    

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "MemoBoard: {}, {}, {}, {}, {}".format(
            self.get_id(),
            self.get_timestamp(),
            self.get_userprofile_id(),
            self.get_candidateprofile_id(),
            self.get_unseen_profile()
        
        )

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Vorschlag Objekt()."""
        obj = Matching()
        obj.set_id(dictionary["id"])
        obj.set_timestamp(dictionary["timestamp"])
        obj.set_userprofile_id(dictionary["userprofile_id"])
        obj.set_candidateprofile_id(dictionary["candidateprofile_id"])
        obj.set_unseen_profile(dictionary["unseen_profile"])
        return obj
        


