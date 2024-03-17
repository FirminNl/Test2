""" Dieser Code definiert eine Klasse namens UserProfileAdm.py Administration, die Methoden zum Ausführen von CRUD-Operationen
 an UserProfile-, MemoBoard-, BlockedProfile-, SearchProfile-, Characteristics-, Info-, Description-, Selection-, Similarity-, Matching-, Chat-, Message und Nachricht-Objekten enthält. 
und einen Matching-Algorithmus, um eine Person anhand ihres Suchprofils mit anderen potenziellen Profilemn abzugleichen. 
Jede Methode öffnet eine Verbindung zu einer entsprechenden Mapper-Klasse (z. B. UserProfileMapper, SearchProfileMapper), 
um mit der Datenbank zu interagieren und die erforderlichen Operationen durchzuführen."""

from server.bo.UserProfileBO import UserProfile
from server.db.UserProfileMapper import UserProfileMapper
from server.Administration.ChatAdm import Administration as ChatAdm
from server.Administration.InfoAdm import Administration as InfoAdm
from server.Administration.DescriptionAdm import Administration as DescriptionAdm
from server.Administration.SearchProfileAdm import Administration as SearchProfileAdm

class Administration (object):
    def __init__(self):
        pass


    """
    UserProfile-spezifische Methoden
    """

    def get_all_user_profile(self):
        """Alle User Profile auslesen"""
        with UserProfileMapper() as mapper:
            return mapper.find_all()

    def create_user_profile(self,google_user_id, email, firstname, surname, about_me):
        user_profile = UserProfile()
        user_profile.set_google_user_id(google_user_id)
        user_profile.set_email(email)
        user_profile.set_firstname(firstname)
        user_profile.set_surname(surname)
        user_profile.set_about_me(about_me)

        with UserProfileMapper() as mapper:
            return mapper.insert(user_profile)

    def get_user_profile_by_guid(self, guid):
        with UserProfileMapper() as mapper:
            return mapper.find_by_guid(guid)
        
    def get_potential_userprofiles(self, userprofile_id):
        with UserProfileMapper() as mapper:
            return mapper.find_potential_userprofiles(userprofile_id)

    def get_user_profile_by_id(self, id):
        with UserProfileMapper() as mapper:
            return mapper.find_by_id(id)

    def update_user_profile(self, user_profile):
        """Einen User speichern"""
        with UserProfileMapper() as mapper:
            return mapper.update(user_profile)

    def update_user_profile_by_id(self, user_profile):
        """Einen User nach der ID speichern"""
        with UserProfileMapper() as mapper:
            return mapper.update_by_id(user_profile)

    def delete_user_profile(self, user_profile):
        from server.Administration.MatchingAdm import Administration as MatchingAdm
        """Den User löschen"""
        chat_adm = ChatAdm()
        desc_adm = DescriptionAdm()
        match_adm = MatchingAdm()
        info_adm = InfoAdm()
        search_prof_adm = SearchProfileAdm()
        all_chats = chat_adm.get_all_chats_by_user(user_profile.get_id())
        searchprofile = search_prof_adm.get_search_profile_by_userprofile_id(user_profile.get_id())
        for chat in all_chats:
            chat_adm.delete_chat(chat)
        all_user_info = info_adm.get_info_by_userprofile_id(user_profile.get_id())
        for info in all_user_info:
            if not info.get_is_selection():
                answer = desc_adm.get_description_by_id(info.get_answer_id())
                desc_adm.delete_description(answer)
            info_adm.delete_info(info)
        if(searchprofile is not None):
            all_search_info = info_adm.get_info_by_searchprofile_id(searchprofile.get_id())
            for info in all_search_info:
                if not info.get_is_selection():
                    answer = desc_adm.get_description_by_id(info.get_answer_id())
                    desc_adm.delete_description(answer)
                info_adm.delete_info(info)
            search_prof_adm.delete_search_profile(searchprofile)
        matches = match_adm.get_all_matches_by_userprofile_id(user_profile.get_id())
        for match in matches:
            match_adm.delete_matching(match)
        with UserProfileMapper() as mapper:
            mapper.delete(user_profile)