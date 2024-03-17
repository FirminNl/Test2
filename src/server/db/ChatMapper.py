from server.db.Mapper import Mapper
from server.bo.ChatBO import Chat

class ChatMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_by_id(self, id):
        """Auslesen eines bestimmten Chats anhand bestimmten Chat-ID"""
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, sender_id, receiver_id, accepted, is_open FROM chat WHERE id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, sender_id, receiver_id, accepted, is_open) = tuples[0]
            chat = Chat()
            chat.set_id(id)
            chat.set_timestamp(timestamp)
            chat.set_sender_id(sender_id)
            chat.set_receiver_id(receiver_id)
            chat.set_accepted(accepted)
            chat.set_is_open(is_open)
            result = chat
        except IndexError:
            result = None
        self._cnx.commit()
        cursor.close()

        return result         

    
    def find_all(self):
        """
        Findet alle Chateinträge in  der Datenbak.
        Ausgabe: Eine Liste von Chat-Objekten oder einer leeren Liste ohne Einträge
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, sender_id, receiver_id, accepted, is_open FROM chat".format(self)
        tuples = cursor.fetchall()

        for (id, timestamp, sender_id, receiver_id, accepted, is_open) in tuples:
            chat = Chat()
            chat.set_id(id)
            chat.set_timestamp(timestamp)
            chat.set_sender_id(sender_id)
            chat.set_receiver_id(receiver_id)
            chat.set_accepted(accepted)
            chat.set_is_open(is_open)
            result.append(chat)
            
        self._cnx.commit()
        cursor.close()

        return result                                   
    

    def find_chat_invitation(self, userprofile_id):
        """Auslesen erhaltener Anfragen anhand der id"""
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, sender_id, receiver_id, accepted, is_open FROM chat WHERE receiver_id={} AND is_open=TRUE".format(userprofile_id)
        
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        for (id, timestamp, sender_id, receiver_id, accepted, is_open) in tuples:
            chat = Chat()
            chat.set_id(id)
            chat.set_timestamp(timestamp)
            chat.set_sender_id(sender_id)
            chat.set_receiver_id(receiver_id)
            chat.set_accepted(accepted)
            chat.set_is_open(is_open)
            result.append(chat)
        
        self._cnx.commit()
        cursor.close()
        
        return result
    
    def find_chat_sent_invitation(self, userprofile_id):
        """Auslesen gesendeter Anfragen anhand der id"""
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, sender_id, receiver_id, accepted, is_open FROM chat WHERE sender_id={} AND is_open=TRUE".format(userprofile_id)
        
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        for (id, timestamp, sender_id, receiver_id, accepted, is_open) in tuples:
            chat = Chat()
            chat.set_id(id)
            chat.set_timestamp(timestamp)
            chat.set_sender_id(sender_id)
            chat.set_receiver_id(receiver_id)
            chat.set_accepted(accepted)
            chat.set_is_open(is_open)
            result.append(chat)
        
        self._cnx.commit()
        cursor.close()
        
        return result
    
    def find_active_chats(self, userprofile_id):
        """Auslesen akzeptierter Anfragen anhand der id"""
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, sender_id, receiver_id, accepted, is_open FROM chat Where (sender_id={} OR receiver_id={}) AND (is_open=FALSE and accepted=TRUE)".format(userprofile_id, userprofile_id)
        
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        for (id, timestamp, sender_id, receiver_id, accepted, is_open) in tuples:
            chat = Chat()
            chat.set_id(id)
            chat.set_timestamp(timestamp)
            chat.set_sender_id(sender_id)
            chat.set_receiver_id(receiver_id)
            chat.set_accepted(accepted)
            chat.set_is_open(is_open)
            result.append(chat)
        
        self._cnx.commit()
        cursor.close()
        
        return result
    
    def find_all_chats_by_user(self, userprofile_id):
        """Auslesen akzeptierter Anfragen anhand der id"""
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, sender_id, receiver_id, accepted, is_open FROM chat Where (sender_id={} OR receiver_id={})".format(userprofile_id, userprofile_id)
        
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        for (id, timestamp, sender_id, receiver_id, accepted, is_open) in tuples:
            chat = Chat()
            chat.set_id(id)
            chat.set_timestamp(timestamp)
            chat.set_sender_id(sender_id)
            chat.set_receiver_id(receiver_id)
            chat.set_accepted(accepted)
            chat.set_is_open(is_open)
            result.append(chat)
        
        self._cnx.commit()
        cursor.close()
        
        return result

    def insert(self, chat):
        """Anlegen eines Chats"""
        cursor = self._cnx.cursor()

        cursor.execute("SELECT MAX(id) AS maxid FROM chat")
        tuples = cursor.fetchall()
        for (maxid) in tuples:
            if maxid[0] is not None:
                chat.set_id(maxid[0] + 1)
            else:
                chat.set_id(1)

        command = "INSERT INTO chat (id, timestamp, sender_id, receiver_id, accepted, is_open) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(
            command,
            (   
                chat.get_id(), 
                chat.get_timestamp(), 
                chat.get_sender_id(), 
                chat.get_receiver_id(), 
                chat.get_accepted(), 
                chat.get_is_open(),
            ),
                
        )
        self._cnx.commit()
        return chat

    def update(self, chat):
        """
        Aktualisieren eines Chat-Objekts in der Datenbank
        Das zu aktualisierende Objekt wird ausgegeben
        """
        cursor = self._cnx.cursor()

        command = "UPDATE chat SET timestamp=%s, sender_id=%s, receiver_id=%s, accepted=%s, is_open=%s WHERE id=%s"
        data = (chat.get_timestamp(), 
                chat.get_sender_id(), 
                chat.get_receiver_id(), 
                chat.get_accepted(), 
                chat.get_is_open(), 
                chat.get_id())
        
        cursor.execute(command, data)
        self._cnx.commit()
        cursor.close()
        return chat
    
    def delete(self, chat):
        """Löschen der Daten eines Chat-Objekts aus der Datenbank"""
        cursor = self._cnx.cursor()
        
        command = "DELETE FROM chat WHERE id={}".format(chat.get_id())
        cursor.execute(command)
        
        self._cnx.commit()
        cursor.close()
