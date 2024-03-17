""" Dieser Code definiert eine Klasse namens BlockedProfile.py Administration, die Methoden zum Ausführen von CRUD-Operationen
 an BlockedProfile-Objekt enthält. Jede Methode öffnet eine Verbindung zu einer entsprechenden Mapper-Klasse (z. B. BlockedProfile, UserProfileMapper, SearchProfileMapper etc.) 
uum mit der Datenbank zu interagieren und die erforderlichen Operationen durchzuführen."""

from server.bo.BlockedProfileBO import BlockedProfile
from server.db.BlockedProfileMapper import BlockedProfileMapper

class Administration:
    def __init__(self):
        pass
    
    def create_blocked_profile(self, userprofile_id, blockeduser_id):
        blocked_profile = BlockedProfile()
        blocked_profile.set_userprofile_id(userprofile_id)
        blocked_profile.set_blockeduser_id(blockeduser_id)

        with BlockedProfileMapper() as mapper:
            return mapper.insert(blocked_profile)
         
    def get_blocked_profile_by_id(self, id):
        with BlockedProfileMapper() as mapper:
            return mapper.find_by_id(id)
        
    def get_all_blocked_profile(self):
        with BlockedProfileMapper() as mapper:
            return mapper.find_all()
       
    def get_blocked_profile_by_userprofile_id(self,userprofile_id):
        with BlockedProfileMapper() as mapper:
            return mapper.find_by_userprofile_id(userprofile_id)
       
    def update_blocked_profile_by_id(self, blocked_profile):
        """Ein geblocktes Profil nach der ID speichern"""
        with BlockedProfileMapper() as mapper:
            return mapper.update_by_id(blocked_profile)
    
    def delete_blocked_profile(self, blocked_profile):
        with BlockedProfileMapper() as mapper:
            mapper.delete(blocked_profile)
