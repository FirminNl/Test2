from server.db.Mapper import Mapper
from server.bo.DescriptionBO import Description

class DescriptionMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_by_characteristic_id(self, characteristic_id):
        """Suchen einer Auswahl anhand der Eigenschaft ID."""
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, characteristic_id, answer, max_answer FROM description WHERE characteristic_id={}".format(characteristic_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, characteristic_id, answer, max_answer) in tuples:
            description = Description()
            description.set_id(id)
            description.set_timestamp(timestamp)
            description.set_characteristic_id(characteristic_id)
            description.set_answer(answer)
            description.set_max_answer(max_answer)
            result.append(description)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Suchen einer Auswahl anhand der ID."""
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, characteristic_id, answer, max_answer " \
                  "FROM description WHERE id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, characteristic_id, answer, max_answer) = tuples[0]
            description = Description()
            description.set_id(id)
            description.set_timestamp(timestamp)
            description.set_characteristic_id(characteristic_id)
            description.set_answer(answer)
            description.set_max_answer(max_answer)
            result = description
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_all(self):
        """Auslesen aller Auswahlen."""
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, characteristic_id, answer, max_answer FROM description"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, characteristic_id, answer, max_answer) in tuples:
            description = Description()
            description.set_id(id)
            description.set_timestamp(timestamp)
            description.set_characteristic_id(characteristic_id)
            description.set_answer(answer)
            description.set_max_answer(max_answer)
            result.append(description)

        self._cnx.commit()
        cursor.close()
        return result

    

    def insert(self, description):
        """Einfügen einer neuen Auswahl."""
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM description")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                description.set_id(maxid[0]+1)
            else:
                description.set_id(1)

        command = "INSERT INTO description (id, timestamp, characteristic_id, answer, max_answer) " \
                  "VALUES (%s,%s,%s,%s,%s)"
        data = (description.get_id(), description.get_timestamp(), description.get_characteristic_id(),
                description.get_answer(), description.get_max_answer())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return description

    def update_by_id(self, description):
        """Überschreiben / Aktualisieren einer Auswahl."""
        cursor = self._cnx.cursor()

        command = "UPDATE description SET characteristic_id=%s, answer=%s, max_answer=%s WHERE id=%s"
        data = (description.get_characteristic_id(), description.get_answer(),
                description.get_max_answer(),description.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return description

    def delete(self, description):
        """Löschen der Daten einer Auswahl aus der Datenbank."""
        cursor = self._cnx.cursor()

        command = "DELETE FROM description WHERE id={}".format(description.get_id())

        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
