from server.db.Mapper import Mapper
from server.bo.UserProfileBO import UserProfile



class UserProfileMapper(Mapper):
    def __init__(self):
        super().__init__()


    def find_all(self):
        """Auslesen aller User Profile aus der Datenbank
        :return Alle UserProfile Objekte im System
        """
        result = []

        cursor = self._cnx.cursor()

        command = "SELECT id, timestamp, google_user_id, email, firstname, " \
                  "surname, about_me FROM userprofile"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, google_user_id, email, firstname, surname, about_me) in tuples:
            user_profile = UserProfile()
            user_profile.set_id(id)
            user_profile.set_timestamp(timestamp)
            user_profile.set_google_user_id(google_user_id)
            user_profile.set_email(email)
            user_profile.set_firstname(firstname)
            user_profile.set_surname(surname)
            user_profile.set_about_me(about_me)
            result.append(user_profile)

        self._cnx.commit()
        cursor.close()

        return result

    def find_potential_userprofiles(self, userprofile_id):
        """Auslesen aller User Profile aus der Datenbank
        :return Alle UserProfile Objekte im System
        """
        result = []

        cursor = self._cnx.cursor()

        command = """
        SELECT id, timestamp, google_user_id, email, firstname, surname, about_me  FROM userprofile
        WHERE id !={} AND id NOT IN (
        SELECT receiver_id FROM chat
            WHERE sender_id = {}
                AND (
                    is_open=True OR accepted=True
                )
        UNION
        SELECT sender_id FROM chat
            WHERE receiver_id = {}
                AND (
                    is_open=True OR accepted=True
                )
        UNION
        SELECT saved_id FROM memoboard
            WHERE userprofile_id = {}
        UNION
        SELECT blockeduser_id FROM blockedprofile
            WHERE userprofile_id = {}
        )
        """.format(userprofile_id, userprofile_id, userprofile_id, userprofile_id, userprofile_id)

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, google_user_id, email, firstname, surname, about_me) in tuples:
            user_profile = UserProfile()
            user_profile.set_id(id)
            user_profile.set_timestamp(timestamp)
            user_profile.set_google_user_id(google_user_id)
            user_profile.set_email(email)
            user_profile.set_firstname(firstname)
            user_profile.set_surname(surname)
            user_profile.set_about_me(about_me)
            result.append(user_profile)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):

        """
        Suchen eines Nutzerprofils anhand Profil-ID. Es wird ein UserProfile-Objekt ausgegeben, das der übergebenen ID enstpricht ist.

        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, google_user_id, email, firstname, " \
                  "surname, about_me FROM userprofile WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, google_user_id, email, firstname, surname, about_me) = tuples[0]
            user_profile = UserProfile()
            user_profile.set_id(id)
            user_profile.set_timestamp(timestamp)
            user_profile.set_google_user_id(google_user_id)
            user_profile.set_email(email)
            user_profile.set_firstname(firstname)
            user_profile.set_surname(surname)
            user_profile.set_about_me(about_me)

            result = user_profile

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten,
            wenn der vorherige SELECT-Aufruf keine Tupel liefert,
            sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_guid(self, guid):
        
        """
        Suchen eines Nutzerprofils anhand Profil-ID. Es wird ein UserProfile-Objekt ausgegeben, das der übergebenen ID enstpricht ist.
        
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, google_user_id, email, firstname, " \
                  "surname, about_me FROM userprofile WHERE google_user_id='{}'".format(guid)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, google_user_id, email, firstname, surname, about_me) = tuples[0]
            user_profile = UserProfile()
            user_profile.set_id(id)
            user_profile.set_timestamp(timestamp)
            user_profile.set_google_user_id(google_user_id)
            user_profile.set_email(email)
            user_profile.set_firstname(firstname)
            user_profile.set_surname(surname)
            user_profile.set_about_me(about_me)

            result = user_profile

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten,
            wenn der vorherige SELECT-Aufruf keine Tupel liefert,
            sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, user_profile):
        """
        Einfügen eines Suchprofil-Objekts in die Datenbank.
        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft
        und ggf. berichtigt.
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM userprofile")
        tuples = cursor.fetchall()
        for maxid in tuples:
            if maxid[0] is not None:
                user_profile.set_id(maxid[0] + 1)
            else:
                user_profile.set_id(1)
        command = """
            INSERT INTO userprofile (
                id, timestamp, google_user_id, email, firstname, surname, about_me 
            ) VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        
        cursor.execute(
            command, 
            (
                user_profile.get_id(),
                user_profile.get_timestamp(),
                user_profile.get_google_user_id(),
                user_profile.get_email(),
                user_profile.get_firstname(),
                user_profile.get_surname(),
                user_profile.get_about_me(),
                
            ),
        )
        self._cnx.commit()

        return user_profile

    def update(self, user_profile):
        """
        Aktualisieren eines Nutzerprofils in der Datenbank.
        Das zu aktualisierende Objekt wird ausgegeben
        """
        cursor = self._cnx.cursor()


        command = "UPDATE userprofile " + "SET timestamp =%s, google_user_id=%s, email =%s, firstname=%s, surname=%s, about_me=%s WHERE id=%s"
        data = (user_profile.get_timestamp(),
                user_profile.get_google_user_id(),
                user_profile.get_email(),
                user_profile.get_firstname(),
                user_profile.get_surname(),
                user_profile.get_about_me(),
                user_profile.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close() 
        return user_profile

    def update_by_id(self, user_profile):

        cursor = self._cnx.cursor()

        command = "UPDATE userprofile SET timestamp=%s, google_user_id=%s, email=%s, " \
                  "firstname=%s , surname=%s , about_me=%s   WHERE id=%s"
        data = (user_profile.get_timestamp(),
                user_profile.get_google_user_id(),
                user_profile.get_email(),
                user_profile.get_firstname(),
                user_profile.get_surname(),
                user_profile.get_about_me(),
                user_profile.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, user_profile):
        cursor = self._cnx.cursor()

        command = "DELETE FROM userprofile WHERE id={}".format(user_profile.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()