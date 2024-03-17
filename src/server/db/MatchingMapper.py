from server.db.Mapper import Mapper
from server.bo.MatchingBO import Matching


class MatchingMapper(Mapper):
    """
    Mapper-Klasse, die Matching-Objekte auf einer relationalen Datenbank abbildet.
    """
    def __init__(self):
        super().__init__()

    def find_all(self):
        """
        Auslesen aller Matching-Objekte.
        Gibt als Ausgabe eine Sammlung mit Matching-Objekten.
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id, candidateprofile_id, unseen_profile FROM matching"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try: 
            (id, timestamp, userprofile_id, candidateprofile_id, unseen_profile) = tuples[0]
            matching = Matching()
            matching.set_id(id)
            matching.set_timestamp(timestamp)
            matching.set_userprofile_id(userprofile_id)
            matching.set_candidateprofile_id(candidateprofile_id)
            matching.set_unseen_profile(unseen_profile)
            result = matching
        
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None
        self._cnx.commit()
        cursor.close()

        return result

    def find_all_by_userprofile_id(self, userprofile_id):
        """
        Suchen eines Matching-Objekts nach der übergebenen Id.

        :param id Primärschlüsselattribut eines Matching-Objekts.
        :return Ein passendes Matching-Objekt, falls gefunden, sonst None.
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id, candidateprofile_id, unseen_profile FROM matching WHERE userprofile_id={}".format(userprofile_id)
        cursor.execute(command)
        tuples = cursor.fetchall()


        for (id, timestamp, userprofile_id, candidateprofile_id, unseen_profile) in tuples:
            matching = Matching()
            matching.set_id(id)
            matching.set_timestamp(timestamp)
            matching.set_userprofile_id(userprofile_id)
            matching.set_candidateprofile_id(candidateprofile_id)
            matching.set_unseen_profile(unseen_profile)
            result.append(matching)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_userprofile_id(self, userprofile_id):

        """
        Suchen eines Matching-Objekts nach der übergebenen Id.

        :param id Primärschlüsselattribut eines Matching-Objekts.
        :return Ein passendes Matching-Objekt, falls gefunden, sonst None.
        """


        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id, candidateprofile_id, unseen_profile FROM matching WHERE userprofile_id={}".format(userprofile_id)
        cursor.execute(command)
        tuples = cursor.fetchall()


        for (id, timestamp, userprofile_id, candidateprofile_id, unseen_profile) in tuples:
            matching = Matching()
            matching.set_id(id)
            matching.set_timestamp(timestamp)
            matching.set_userprofile_id(userprofile_id)
            matching.set_candidateprofile_id(candidateprofile_id)
            matching.set_unseen_profile(unseen_profile)
            result.append(matching)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):
        """
        Suchen eines Matching-Objekts nach der übergebenen Id.

        :param id Primärschlüsselattribut eines Matching-Objekts.
        :return Ein passendes Matching-Objekt, falls gefunden, sonst None.
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id, candidateprofile_id, unseen_profile FROM matching WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, userprofile_id, candidateprofile_id, unseen_profile) = tuples[0]
            matching = Matching()
            matching.set_id(id)
            matching.set_timestamp(timestamp)
            matching.set_userprofile_id(userprofile_id)
            matching.set_candidateprofile_id(candidateprofile_id)
            matching.set_unseen_profile(unseen_profile)
            result = matching
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, matching):
        """
        Einfügen eines Matching-Objekts in die Datenbank.
        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt. Als Ausgabe wird bereits das übergebene Matching-Objekt mit ggf. korrigierter `id` zurückgegeben.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM matching")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                matching.set_id(maxid[0] + 1)
            else:
                matching.set_id(1)

        command = "INSERT INTO matching (id, timestamp, userprofile_id, candidateprofile_id, unseen_profile) VALUES (%s,%s,%s,%s,%s)"
        data = (matching.get_id(), matching.get_timestamp(), matching.get_userprofile_id(), matching.get_candidateprofile_id(), matching.get_unseen_profile())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return matching

    def update_by_id(self, matching):

        cursor = self._cnx.cursor()

        command = "UPDATE matching SET timestamp=%s, userprofile_id=%s, " \
                  "candidateprofile_id=%s, unseen_profile=%s WHERE id=%s"
        data = (matching.get_timestamp(),
                matching.get_userprofile_id(),
                matching.get_candidateprofile_id(),
                matching.get_unseen_profile(),
                matching.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, matching):
        cursor = self._cnx.cursor()

    # Dann wird das Matching-Objekt aus der Tabelle `matching` gelöscht
        command = "DELETE FROM matching WHERE id={}".format(matching.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
