from server.bo.BusinessObjectBO import BusinessObject

"""
Klasse Chat mit einfachen Methoden zum Setzen der Klassenvariablen

"""


class Chat(BusinessObject):
    """Klasse Chat"""
    def __init__(self): 
        super().__init__()
        self._sender_id = 0
        self._receiver_id = 0
        self._accepted = False
        self._is_open = False
    
    def set_sender_id(self, sender_id):
        """setzen Absender der Nachricht"""
        self._sender_id = sender_id
        
    def get_sender_id(self):
        """auslesen Absender der Nachricht"""
        return self._sender_id

    def set_receiver_id(self, receiver_id):
        """setzen Empfaenger der Nachricht"""
        self._receiver_id = receiver_id
        
    def get_receiver_id(self):
        """auslesen Empfaenger der Nachricht"""
        return self._receiver_id
    
    def set_accepted(self, accepted):
        """setzen Bestaetigungsstatus Anfrage"""
        self._accepted = accepted
        
    def get_accepted(self):
        """auslesen Bestaetigungsstatus Anfrage"""
        return self._accepted
    
    def set_is_open(self, is_open):
        """setzen Einladungsstatus"""
        self._is_open = is_open
        
    def get_is_open(self):
        """auslesen Einladungsstatus"""
        return self._is_open
     

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "Chat: {}, {}, {}, {}, {}, {}".format(
            self.get_id(),
            self.get_timestamp(),
            self.get_sender_id(),
            self.get_receiver_id(),
            self.get_accepted(),
            self.get_is_open()
        
        )

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Chat Objekt()."""
        obj = Chat()
        obj.set_id(dictionary["id"])
        obj.set_timestamp(dictionary["timestamp"])
        obj.set_sender_id(dictionary["sender_id"])
        obj.set_receiver_id(dictionary["receiver_id"])
        obj.set_accepted(dictionary["accepted"])
        obj.set_is_open(dictionary["is_open"])
        return obj
        


