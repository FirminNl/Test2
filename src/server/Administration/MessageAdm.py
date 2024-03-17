""" Dieser Code definiert eine Klasse namens UserProfileAdm.py Administration, die Methoden zum Ausführen von CRUD-Operationen
 an UserProfile-, MemoBoard-, BlockedProfile-, SearchProfile-, Characteristics-, Info-, Description-, Selection-, Similarity-, Matching-, Chat-, Message und Nachricht-Objekten enthält. 
und einen Matching-Algorithmus, um eine Person anhand ihres Suchprofils mit anderen potenziellen Profilemn abzugleichen. 
Jede Methode öffnet eine Verbindung zu einer entsprechenden Mapper-Klasse (z. B. UserProfileMapper, SearchProfileMapper), 
um mit der Datenbank zu interagieren und die erforderlichen Operationen durchzuführen."""

from server.bo.MessageBO import Message 
from server.db.MessageMapper import MessageMapper


class Administration:
    def __init__(self):
        pass
    
    def create_message(self, chat_id, content, sender_id):
        message = Message()
        message.set_chat_id(chat_id)
        message.set_content(content)
        message.set_sender_id(sender_id)

        with MessageMapper()as mapper:
            return mapper.insert(message)

    def get_message_by_id(self, id):
        with MessageMapper() as mapper:
            return mapper.find_by_id(id)
        
    def get_all_message(self):
        """Alle messages auslesen"""
        with MessageMapper() as mapper:
            return mapper.find_all
                                 
    def get_message_by_chat_id(self, chat_id):
        with MessageMapper() as mapper:
            return mapper.find_message_from_chat(chat_id)
        
    def get_all_messages(self):
        with MessageMapper() as mapper:
            return mapper.find_all()
        
    def update_message_by_id(self, message):
        with MessageMapper() as mapper:
            return mapper.update_by_id(message)

    def delete_message(self, message):
        with MessageMapper() as mapper:
            mapper.delete(message)

    
