from server.db.Mapper import Mapper
from server.bo.SimilarityBO import Similarity

class SimilarityMapper(Mapper):
    def __init__(self):
        super().__init__()
    """
    Mapper-Klasse, die Similarity-Objekte auf einer relationalen Datenbank abbildet.
    """

    def find_all(self):
        """
        Auslesen aller Similarity-Objekte aus der Datenbank.
        :return Eine Liste mit Similarity-Objekten
        """
        result = []

        cursor = self._cnx.cursor()

        command = "SELECT id, timestamp, matching_id, score FROM similarity"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, matching_id, score) in tuples:
            similarity = Similarity()
            similarity.set_id(id)
            similarity.set_timestamp(timestamp)
            similarity.set_matching_id(matching_id)
            similarity.set_score(score)
            result.append(similarity)

        self._cnx.commit()
        cursor.close()

        return result
    
    def find_by_matching_id(self, matching_id):
        """
        Suchen eines Similarity-Objekts nach der übergebenen Matching Id.

        :param id Primärschlüsselattribut eines Matching-Objekts.
        :return Ein passendes Matching-Objekt, falls gefunden, sonst None.
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, matching_id, score FROM similarity WHERE matching_id={}".format(matching_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, matching_id, score) = tuples[0]
            similarity = Similarity()
            similarity.set_id(id)
            similarity.set_timestamp(timestamp)
            similarity.set_matching_id(matching_id)
            similarity.set_score(score)
            result = similarity
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):
        """
        Suchen eines Similarity-Objekts , anhand der zu übergebenden ID.
        Ausgabe soll das gefundene Similarity-Objekt oder None wiedergeben, wenn kein Objekt mit dieser ID gefunden wurde
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, matching_id, score FROM similarity WHERE id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, matching_id, score) = tuples[0]
            similarity = Similarity()
            similarity.set_id(id)
            similarity.set_timestamp(timestamp)
            similarity.set_matching_id(matching_id)
            similarity.set_score(score)
            result = similarity
        
        except IndexError:
            """Falls kein Nutzerprofil mit der angegebenen Similarity gefunden werden konnte,
            wird hier None als Rückgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, similarity):
        """
        Einfügen eines Similarity-Objekts in die Datenbank.
        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf. aktualisiert.
        :param similarity: Das zu speichernde Similarity-Objekt
        :return Das bereits übergebene Similarity-Objekt, jedoch mit ggf. aktualisierten Daten (id)
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM similarity")
        tuples = cursor.fetchall()

        for maxid in tuples:
            if maxid[0] is not None:
                similarity.set_id(maxid[0] + 1)
            else:
                similarity.set_id(1)

        command = "INSERT INTO similarity (id, timestamp, matching_id, score) VALUES (%s,%s,%s,%s)"
        data = (similarity.get_id(),
                similarity.get_timestamp(),
                similarity.get_matching_id(), 
                similarity.get_score())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return similarity

    
    
    
    def update_by_id(self, similarity):

        cursor = self._cnx.cursor()

        command = "UPDATE similarity SET timestamp=%s, matching_id=%s, " \
                  "score=%s WHERE id=%s"
        data = (similarity.get_timestamp(),
                similarity.get_matching_id(),
                similarity.get_score(),
                similarity.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        
        
    def delete(self, similarity):
        cursor = self._cnx.cursor()

        command = "DELETE FROM similarity WHERE id={}".format(similarity.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
