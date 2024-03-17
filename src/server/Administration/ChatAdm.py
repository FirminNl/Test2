""" Dieser Code definiert eine Klasse namens UserProfileAdm.py Administration, die Methoden zum Ausführen von CRUD-Operationen
 an UserProfile-, MemoBoard-, BlockedProfile-, SearchProfile-, Characteristics-, Info-, Description-, Selection-, Similarity-, Matching-, Chat-, Message und Nachricht-Objekten enthält. 
und einen Matching-Algorithmus, um eine Person anhand ihres Suchprofils mit anderen potenziellen Profilemn abzugleichen. 
Jede Methode öffnet eine Verbindung zu einer entsprechenden Mapper-Klasse (z. B. UserProfileMapper, SearchProfileMapper), 
um mit der Datenbank zu interagieren und die erforderlichen Operationen durchzuführen."""

from server.bo.ChatBO import Chat
from server.db.ChatMapper import ChatMapper
from server.Administration.MessageAdm import Administration as MessageAdm

class Administration (object):
    def __init__(self):
        pass

    """
    Chat-spezifische Methoden
    """

    def create_chat(self, sender_id, receiver_id, accepted, is_open):
        chat = Chat()
        chat.set_sender_id(sender_id)
        chat.set_receiver_id(receiver_id)
        chat.set_accepted(accepted)
        chat.set_is_open(is_open)
        with ChatMapper() as mapper:
            return mapper.insert(chat)
    
    def get_all_chat(self):
        #Alle Chats auslesen
        with ChatMapper() as mapper:
            return mapper.find_all()

    def get_chat_by_id(self, id):
        with ChatMapper() as mapper:
            return mapper.find_by_id(id)
        
    def get_chat_invitation(self, userprofile_id):
        #Erhaltene Chatanfragen von der Person mit der gegebenen ID auslesen
        with ChatMapper() as mapper:
            return mapper.find_chat_invitation(userprofile_id)
        
    def get_chat_sent_invitation(self, userprofile_id):
        #Erhaltene Chatanfragen von der Person mit der gegebenen ID auslesen
        with ChatMapper() as mapper:
            return mapper.find_chat_sent_invitation(userprofile_id)
        
    def get_active_chats(self, userprofile_id):
        # Aktuellen Chat von der Person mit der gegebenen ID auslesen
        with ChatMapper() as mapper:
            return mapper.find_active_chats(userprofile_id)
        
    def get_all_chats_by_user(self, userprofile_id):
        # Aktuellen Chat von der Person mit der gegebenen ID auslesen
        with ChatMapper() as mapper:
            return mapper.find_all_chats_by_user(userprofile_id)

    def update_chat(self, chat):
        with ChatMapper() as mapper:
            return mapper.update(chat)

    def delete_chat(self, chat):
        """Den Chat löschen"""
        message_adm = MessageAdm()
        messages_by_chat = message_adm.get_message_by_chat_id(chat.get_id())
        for message in messages_by_chat:
            message_adm.delete_message(message)
        with ChatMapper() as mapper:
            mapper.delete(chat)