from server.db.Mapper import Mapper
from server.bo.SelectionBO import Selection


class SelectionMapper(Mapper):
    """Mapper-Klasse, die Selection-Objekte auf relationale DB abbildet"""

    def __init__(self):
        super().__init__()

    def find_by_characteristic_id(self, characteristic_id):
        """Suchen einer Auswahl anhand der Eigenschaft ID."""

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, characteristic_id, answer FROM selection WHERE characteristic_id='{}'".format(characteristic_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, characteristic_id, answer) in tuples:
            selection = Selection()
            selection.set_id(id)
            selection.set_timestamp(timestamp)
            selection.set_characteristic_id(characteristic_id)
            selection.set_answer(answer)

            result.append(selection)


        self._cnx.commit()

        cursor.close()

        return result

    def find_by_id(self, id):
        """Auslesen eines Selection-Objekts anhand der ID"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, characteristic_id, answer FROM selection WHERE id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, characteristic_id,answer) = tuples[0]

            selection = Selection()
            selection.set_id(id)
            selection.set_timestamp(timestamp)
            selection.set_characteristic_id(characteristic_id)
            selection.set_answer(answer)

            result = selection
        
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten,
            wenn der vorherige SELECT-Aufruf keine Tupel liefert,
            sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result
    def insert(self, selection):
        """Einfügen eines Selection-Objekts in die DB. Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft
        und ggf. berichtigt."""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM selection")
        tuples = cursor.fetchall()
        for maxid in tuples:
            if maxid[0] is not None:
                selection.set_id(maxid[0] + 1)
            else:
                selection.set_id(1)

        command = "INSERT INTO selection (id, timestamp, characteristic_id, answer) VALUES (%s,%s,%s,%s)"
        data = (
            selection.get_id(),
            selection.get_timestamp(),
            selection.get_characteristic_id(),
            selection.get_answer(),
        )

        cursor.execute(command, data)
        self._cnx.commit()
        cursor.close()

        return selection

    def find_all(self):
        """Auslesen aller Selection-Objekte aus der DB"""

        result = []
        cursor = self._cnx.cursor()

        command = "SELECT id, timestamp, characteristic_id, answer FROM selection"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, characteristic_id, answer) in tuples:
            selection = Selection()
            selection.set_id(id)
            selection.set_timestamp(timestamp)
            selection.set_characteristic_id(characteristic_id)
            selection.set_answer(answer)
            result.append(selection)

        self._cnx.commit()
        cursor.close()

        return result



    def update_by_id(self, selection):
        """Updaten eines Selection-Objekts in der DB"""

        cursor = self._cnx.cursor()
        command = "UPDATE selection " + "SET characteristic_id=%s,answer=%s WHERE id=%s"
        data = (
            selection.get_characteristic_id(),
            selection.get_answer(),
            selection.get_id(),
        )

        cursor.execute(command, data)
        self._cnx.commit()
        cursor.close()

        return selection

    def delete(self, selection):
        """Löschen der Daten einer Auswahl aus der Datenbank."""
        cursor = self._cnx.cursor()

        command = "DELETE FROM selection WHERE id={}".format(selection.get_id())

        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
