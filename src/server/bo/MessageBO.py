from .BusinessObjectBO import BusinessObject

"""
Klasse Nachricht mit einfachen Methoden zum Setzen der Klassenvariablen

"""


class Message(BusinessObject):
    """Klasse Nachricht"""
    def __init__(self): 
        super().__init__()
        self._chat_id = 0
        self._content = ""
        self._sender_id = 0
        
    def set_chat_id(self, chat_id):
        """setzen Chat id"""
        self._chat_id = chat_id
        
    def get_chat_id(self):
        """auslesen Chat id"""
        return self._chat_id

    def set_content(self, content):
        """setzen Inhalt der Nachricht"""
        self._content = content
        
    def get_content(self):
        """auslesen Inhalt der Nachricht"""
        return self._content
    
    
    def set_sender_id(self, sender_id):
        """setzen Absender der Nachricht"""
        self._sender_id = sender_id
        
    def get_sender_id(self):
        """auslesen Absender der Nachricht"""
        return self._sender_id
     

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "Message: {}, {}, {}, {}, {}".format(
            self.get_id(),
            self.get_timestamp(),
            self.get_chat_id(),
            self.get_content(),
            self.get_sender_id(),
        
        )
    
    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Nachrichten Objekt()."""
        obj = Message()
        obj.set_id(dictionary["id"])
        obj.set_timestamp(dictionary["timestamp"])
        obj.set_chat_id(dictionary["chat_id"])
        obj.set_content(dictionary["content"])
        obj.set_sender_id(dictionary["sender_id"])
        return obj
