""" Dieser Code definiert eine Klasse namens UserProfileAdm.py Administration, die Methoden zum Ausführen von CRUD-Operationen
 an UserProfile-, MemoBoard-, BlockedProfile-, SearchProfile-, Characteristics-, Info-, Description-, Selection-, Similarity-, Matching-, Chat-, Message und Nachricht-Objekten enthält. 
und einen Matching-Algorithmus, um eine Person anhand ihres Suchprofils mit anderen potenziellen Profilemn abzugleichen. 
Jede Methode öffnet eine Verbindung zu einer entsprechenden Mapper-Klasse (z. B. UserProfileMapper, SearchProfileMapper), 
um mit der Datenbank zu interagieren und die erforderlichen Operationen durchzuführen."""

from server.bo.SearchProfileBO import SearchProfile
from server.db.SearchProfileMapper import SearchProfileMapper

class Administration (object):
    def __init__(self):
        pass


    """
    SearchProfile-spezifische Methoden
    """
    def get_all_search_profile(self):
        with SearchProfileMapper() as mapper:
            return mapper.find_all()

    def get_search_profile_by_id(self,  id):
        with SearchProfileMapper() as mapper:
            return mapper.find_by_id(id)

    def get_search_profile_by_userprofile_id(self,userprofile_id):
        with SearchProfileMapper() as mapper:
            return mapper.find_by_userprofile_id(userprofile_id)

    def create_search_profile(self, userprofile_id):
        search_profile = SearchProfile()
        search_profile.set_userprofile_id(userprofile_id)

        with SearchProfileMapper() as mapper:
            return mapper.insert(search_profile)

    def update_search_profile_by_id(self, search_profile):
        """Ein Suchprofil nach der ID speichern"""
        with SearchProfileMapper() as mapper:
            return mapper.update_by_id(search_profile)

    def delete_search_profile(self, search_profile):
        """Das Suchprofil löschen"""
        with SearchProfileMapper() as mapper:
            mapper.delete(search_profile)