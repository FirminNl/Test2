from server.db.Mapper import Mapper
from server.bo.BlockedProfileBO import BlockedProfile


class BlockedProfileMapper(Mapper):
    def __init__(self):
        super().__init__()


    def find_all(self):
        """
        Findet alle Blockierten Profil Einträge in  der Datenbak.
        Ausgabe: Eine Liste von Blockedprofilobjekten oder einer leeren Liste ohne Eintraege
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id, blockeduser_id FROM blockedprofile".format(self)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, userprofile_id, blockeduser_id) in tuples:
            blocked_profile = BlockedProfile()
            blocked_profile.set_id(id)
            blocked_profile.set_timestamp(timestamp)
            blocked_profile.set_userprofile_id(userprofile_id)
            blocked_profile.set_blockeduser_id(blockeduser_id)
            result.append(blocked_profile)


        self._cnx.commit()

        cursor.close()

        return result
    
    def find_by_userprofile_id(self, userprofile_id):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id, blockeduser_id FROM blockedprofile WHERE userprofile_id='{}'".format(userprofile_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, userprofile_id, blockeduser_id) in tuples:
            blocked_profile = BlockedProfile()
            blocked_profile.set_id(id)
            blocked_profile.set_timestamp(timestamp)
            blocked_profile.set_userprofile_id(userprofile_id)
            blocked_profile.set_blockeduser_id(blockeduser_id)
            result.append(blocked_profile)

        self._cnx.commit()

        cursor.close()

        return result
    
    def find_by_id(self, id):
        """Suchen eines BlockedProfiles mit vorgegebener ID"""
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id, blockeduser_id FROM blockedprofile WHERE id={}".format(
            id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, userprofile_id,blockeduser_id) = tuples[0]

            blocked_profile = BlockedProfile()
            blocked_profile.set_id(id)
            blocked_profile.set_timestamp(timestamp)
            blocked_profile.set_userprofile_id(userprofile_id)
            blocked_profile.set_blockeduser_id(blockeduser_id)


            result = blocked_profile

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten,
            wenn der vorherige SELECT-Aufruf keine Tupel liefert,
            sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result
    
    def insert(self, blocked_profile):
        """Einfügen eines BlockedProfile-Objekts in die Datenbank"""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM blockedprofile")
        tuples = cursor.fetchall()
        for maxid in tuples:
            if maxid[0] is not None:
                blocked_profile.set_id(maxid[0] + 1)
            else:
                blocked_profile.set_id(1)

        command = """ INSERT INTO blockedprofile (id, timestamp, userprofile_id, blockeduser_id) 
        VALUES (%s,%s,%s, %s)"""

        cursor.execute(
            command,
            (
                blocked_profile.get_id(),
                blocked_profile.get_timestamp(),
                blocked_profile.get_userprofile_id(),
                blocked_profile.get_blockeduser_id(),
            ),
        )
        self._cnx.commit()
        cursor.close()




    def update(self, blocked_profile):
        """Aktualisieren eines BlockedProfile-Objekts in der Datenbank"""

        cursor = self._cnx.cursor()

        command = "UPDATE blockedprofile SET timestamp=%s, userprofile_id=%s, blockeduser_id=%s WHERE id=%s"
        data = (blocked_profile.get_timestamp(),
                blocked_profile.get_userprofile_id(),
                blocked_profile.get_blockeduser_id(),
                blocked_profile.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return blocked_profile


    def update_by_id(self, blockedprofile):
        cursor = self._cnx.cursor()

        command = "UPDATE blockedprofile SET timestamp=%s, userprofile_id=%s, blockeduser_id=%s WHERE id=%s"

        data = (blockedprofile.get_timestamp(),
                blockedprofile.get_userprofile_id(),
                blockedprofile.get_blockeduser_id(),
                blockedprofile.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, blocked_profile):
        """Löschen der Daten eines gemerkten Profils aus der Datenbank"""
        cursor = self._cnx.cursor()
        command = "DELETE FROM blockedprofile WHERE id={}".format(blocked_profile.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
