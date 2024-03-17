from server.db.Mapper import Mapper
from server.bo.SearchProfileBO import SearchProfile


class SearchProfileMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_by_userprofile_id(self, userprofile_id):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id FROM searchprofile WHERE userprofile_id={}".format(userprofile_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, userprofile_id) = tuples[0]
            search_profile = SearchProfile()
            search_profile.set_id(id)
            search_profile.set_timestamp(timestamp)
            search_profile.set_userprofile_id(userprofile_id)

            result = search_profile

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_id(self, id):
        """
        Suchen eines Suchprofil-Eintrags anhand der Suchprofil-ID.
        Parameter key = Suchprofil-ID

        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id FROM searchprofile WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, userprofile_id) = tuples[0]
            search_profile = SearchProfile()
            search_profile.set_id(id)
            search_profile.set_timestamp(timestamp)
            search_profile.set_userprofile_id(userprofile_id)
            
            result = search_profile

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_all(self):
        """
        Findet alle Suchprofileintraege in  der Datenbak.
        Ausgabe: Eine Liste von Suchprofilobjekten oder einer leeren Liste ohne Eintraege
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id FROM searchprofile".format(self)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, userprofile_id) in tuples:
            search_profile = SearchProfile()
            search_profile.set_id(id)
            search_profile.set_timestamp(timestamp)
            search_profile.set_userprofile_id(userprofile_id)
            result.append(search_profile)


        self._cnx.commit()

        cursor.close()

        return result
    

    def insert(self, search_profile):
        """
        Einfügen eines neuen Suchprofil-Eintrags in die Datenbank.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM searchprofile")
        tuples = cursor.fetchall()
        for maxid in tuples:
            if maxid[0] is not None:
                search_profile.set_id(maxid[0] + 1)
            else:
                search_profile.set_id(1)

        command = """INSERT INTO searchprofile (id, timestamp, userprofile_id) VALUES ( %s, %s, %s)"""
        
        cursor.execute(
            command,
            (
                search_profile.get_id(),
                search_profile.get_timestamp(),
                search_profile.get_userprofile_id(),
            ),
        )
        self._cnx.commit()
        return search_profile
        
        
    def update(self, search_profile):
        """
        aktualisiert einen bestehenden Suchprofil-Eintrag in der Datenbank.
        Ausgegeben wird das aktualisierte SearchProfile-Objekt
        """
        cursor = self._cnx.cursor()
        command = "UPDATE searchprofile SET timestamp=%s, userprofile_id=%s WHERE id=%s"
        data = (search_profile.get_userprofile_id(),
                search_profile.get_id())
        cursor.execute(command, data)
        self._cnx.commit()
        cursor.close() 
        return search_profile

    def update_by_id(self, search_profile):

        cursor = self._cnx.cursor()

        command = "UPDATE searchprofile SET timestamp=%s, userprofile_id=%s WHERE id=%s"

        data = (search_profile.get_timestamp(),
                search_profile.get_userprofile_id(),
                search_profile.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()


    def delete(self, search_profile):
        cursor = self._cnx.cursor()

        command = "DELETE FROM searchprofile WHERE id={}".format(search_profile.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()