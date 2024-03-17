from server.db.Mapper import Mapper
from server.bo.CharacteristicBO import Characteristic

class CharacteristicMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_by_id(self, id):
        """
        Findet eine Eigenschaft anhand der ID.
        Ausgegeben wird Characteristic-Objekt oder None
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, name, description, is_selection, author_id, is_standart FROM characteristic WHERE id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, name, description, is_selection, author_id, is_standart) = tuples[0]
            characteristic = Characteristic()
            characteristic.set_id(id)
            characteristic.set_timestamp(timestamp)
            characteristic.set_name(name)
            characteristic.set_description(description)
            characteristic.set_is_selection(is_selection)
            characteristic.set_author_id(author_id)
            characteristic.set_is_standart(is_standart)

            result = characteristic
        
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_all(self):
        """
        Liest alle Eigenschaften aus und gibt Liste mit Characteristic-Objekten wieder.
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, name, description, is_selection, author_id, is_standart FROM characteristic where is_standart = FALSE".format(self)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, name, description, is_selection, author_id, is_standart) in tuples:
            characteristic = Characteristic()
            characteristic.set_id(id)
            characteristic.set_timestamp(timestamp)
            characteristic.set_name(name)
            characteristic.set_description(description)
            characteristic.set_is_selection(is_selection)
            characteristic.set_author_id(author_id)
            characteristic.set_is_standart(is_standart)
            result.append(characteristic)

        self._cnx.commit()
        cursor.close()
        return result
    
    def find_all_by_standart(self):
        """
        Liest alle Eigenschaften aus und gibt Liste mit Characteristic-Objekten wieder.
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, name, description, is_selection, author_id, is_standart FROM characteristic where is_standart = TRUE".format(self)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, name, description, is_selection, author_id, is_standart) in tuples:
            characteristic = Characteristic()
            characteristic.set_id(id)
            characteristic.set_timestamp(timestamp)
            characteristic.set_name(name)
            characteristic.set_description(description)
            characteristic.set_is_selection(is_selection)
            characteristic.set_author_id(author_id)
            characteristic.set_is_standart(is_standart)
            result.append(characteristic)

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, characteristic):
        """
        Speichert ein neues Characteristic-Objekt in der Datenbank.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM characteristic")
        tuples = cursor.fetchall()
        for maxid in tuples:
            if maxid[0] is not None:
                characteristic.set_id(maxid[0] + 1)
            else:
                characteristic.set_id(1)
        command = """INSERT INTO characteristic (id, timestamp, name, description, is_selection, author_id, is_standart)
         VALUES (%s,%s,%s,%s, %s, %s, %s)"""

        cursor.execute(
            command,
            (
                characteristic.get_id(),
                characteristic.get_timestamp(),
                characteristic.get_name(),
                characteristic.get_description(),
                characteristic.get_is_selection(),
                characteristic.get_author_id(),
                characteristic.get_is_standart(),

            ),
        )
        self._cnx.commit()

        return characteristic

    def update(self, characteristic):
        cursor = self._cnx.cursor()
        """
        Aktualisiert eine Eigenschaft in der Datenbank.
        :param characteristic: Das zu aktualisierende Characteristic-Objekt.
        :return: Das aktualisierte Characteristic-Objekt.
        """
        

        command = "UPDATE characteristic SET timestamp=%s, name=%s, description=%s, " \
                  "is_selection=%s, author_id=%s, is_standart=%s WHERE id=%s"
        data = (
                characteristic.get_timestamp(),
                characteristic.get_name(),
                characteristic.get_description(),
                characteristic.get_is_selection(),
                characteristic.get_author_id(),
                characteristic.get_is_standart(),
                characteristic.get_id(),
                )

        cursor.execute(command, data)
        self._cnx.commit()
        cursor.close() 
        return characteristic

    def delete(self, characteristic):
        """Löschen der Daten einer Eigenschaft aus der Datenbank"""
        cursor = self._cnx.cursor()
        command = "DELETE FROM characteristic WHERE id={}".format(characteristic.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
