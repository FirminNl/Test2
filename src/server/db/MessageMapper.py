from server.db.Mapper import Mapper
from server.bo.MessageBO import Message

class MessageMapper(Mapper):
    """Mapper-Klasse für Message-Objekte"""

    def __init__(self):
        super().__init__()

    def insert(self, message):
        """ 
        Einfügen eines Nachrichten-Objekts in die Datenbank.
        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft
        und ggf. berichtigt.
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM message")
        tuples = cursor.fetchall()
        for maxid in tuples:
            if maxid[0] is not None:
                message.set_id(maxid[0] + 1)
            else:
                message.set_id(1)
        command = """
            INSERT INTO message (id, timestamp, chat_id, content, sender_id) VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(
            command, 
            (
                message.get_id(),
                message.get_timestamp(),
                message.get_chat_id(),
                message.get_content(),
                message.get_sender_id(),
            ),   
        )
        self._cnx.commit()
        cursor.close()

        return message
    
    def find_message_from_chat(self, chat_id):

        """
        Suchen einer Nachricht anhand Nachricht-ID. Es wird ein Nachrichten-Objekt ausgegeben, das der übergebenen ID enstpricht ist.

        """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, timestamp, chat_id, content, sender_id FROM message WHERE chat_id={}".format(chat_id))       
        tuples = cursor.fetchall()
    
        for (id, timestamp, chat_id, content, sender_id) in tuples:
            message = Message()
            message.set_id(id)
            message.set_timestamp(timestamp)
            message.set_chat_id(chat_id)
            message.set_content(content)
            message.set_sender_id(sender_id)
            result.append(message)

        
        self._cnx.commit()
        cursor.close()    
    
        return result
    def find_all(self):
        
        "Auslesen aller Message-Objekte aus der Datenbank"""

        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, timestamp, chat_id, content, sender_id FROM message")
        tuples = cursor.fetchall()

        for (id, timestamp, chat_id, content, sender_id) in tuples:
            message = Message()
            message.set_id(id)
            message.set_timestamp(timestamp)
            message.set_chat_id(chat_id)
            message.set_content(content)
            message.set_sender_id(sender_id)
            result.append(message)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):
        """Auslesen eines Message-Objekts aus der Datenbank anhand der ID"""

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, chat_id, content, sender_id FROM message WHERE id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, chat_id, content, sender_id) = tuples[0]
            message = Message()
            message.set_id(id)
            message.set_timestamp(timestamp)
            message.set_chat_id(chat_id)
            message.set_content(content)
            message.set_sender_id(sender_id)
            result = message
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update_by_id(self, message):
        """Aktualisieren eines Message-Objekts in der Datenbank"""

        cursor = self._cnx.cursor()

        command = "UPDATE message" + "SET timestamp=%s, chat_id=%s, content=%s, sender_id=%s WHERE id=%s"
        data = (message.get_timestamp(),
                message.get_chat_id(),
                message.get_content(), 
                message.get_sender_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return message

    def delete(self, message):
        """Löschen eines Message-Objekts aus der Datenbank"""

        cursor = self._cnx.cursor()

        command = "DELETE FROM message WHERE id={}".format(message.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
