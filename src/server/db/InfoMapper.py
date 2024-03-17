from server.db.Mapper import Mapper
from server.bo.InfoBO import Info


class InfoMapper(Mapper):
    """
    Mapper-Klasse, die Info-Objekte auf einer relationalen Datenbank abbildet.
    """
    def __init__(self):
        super().__init__()


    def find_all_by_char(self, characteristic_id, is_selection):
        """
        Suchen von Infos anhand der übergebenen userprofile_id und eine Sammlung mit Infos, die sämtliche Infos des betreffenden Benutzers repräsentieren.
        """
        result = []
        cursor = self._cnx.cursor()
        if is_selection:
            command = """SELECT id, timestamp, userprofile_id, answer_id, is_selection, is_searchprofile FROM info
              WHERE (answer_id in (SELECT id FROM selection WHERE characteristic_id={})) AND (is_selection is True)""".format(characteristic_id)
        else:   
            command = """SELECT id, timestamp, userprofile_id, answer_id, is_selection, is_searchprofile FROM info
              WHERE (answer_id in (SELECT id FROM description WHERE characteristic_id={})) AND (is_selection is False)""".format(characteristic_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, userprofile_id, answer_id, is_selection, is_searchprofile) in tuples:
            info = Info()
            info.set_id(id)
            info.set_timestamp(timestamp)
            info.set_userprofile_id(userprofile_id)
            info.set_answer_id(answer_id)
            info.set_is_selection(is_selection)
            info.set_is_searchprofile(is_searchprofile)
            result.append(info)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_userprofile_id(self, userprofile_id):
        """
        Suchen von Infos anhand der übergebenen userprofile_id und eine Sammlung mit Infos, die sämtliche Infos des betreffenden Benutzers repräsentieren.
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id, answer_id, is_selection, is_searchprofile FROM info WHERE is_searchprofile=false AND userprofile_id='{}'".format(userprofile_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, userprofile_id, answer_id, is_selection, is_searchprofile) in tuples:
            info = Info()
            info.set_id(id)
            info.set_timestamp(timestamp)
            info.set_userprofile_id(userprofile_id)
            info.set_answer_id(answer_id)
            info.set_is_selection(is_selection)
            info.set_is_searchprofile(is_searchprofile)
            result.append(info)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_searchprofile_id(self, searchprofile_id):
        """
        Suchen von Infos anhand der übergebenen searchprofile_id und eine Sammlung mit Infos, die sämtliche Infos des betreffenden Benutzers repräsentieren.
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id, answer_id, is_selection, is_searchprofile FROM info WHERE is_searchprofile=true AND userprofile_id='{}'".format(searchprofile_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, userprofile_id, answer_id, is_selection, is_searchprofile) in tuples:
            info = Info()
            info.set_id(id)
            info.set_timestamp(timestamp)
            info.set_userprofile_id(userprofile_id)
            info.set_answer_id(answer_id)
            info.set_is_selection(is_selection)
            info.set_is_searchprofile(is_searchprofile)
            result.append(info)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):

        """
        Suchen eines Infoobjekts anhand Info-ID. Es wird ein Info-Objekt ausgegeben, das der übergebenen ID enstpricht ist.

        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id, answer_id, is_selection, is_searchprofile " \
                  "FROM info WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, userprofile_id, answer_id, is_selection, is_searchprofile) = tuples[0]
            info = Info()
            info.set_id(id)
            info.set_timestamp(timestamp)
            info.set_userprofile_id(userprofile_id)
            info.set_answer_id(answer_id)
            info.set_is_selection(is_selection)
            info.set_is_searchprofile(is_searchprofile)

            result = info

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten,
            wenn der vorherige SELECT-Aufruf keine Tupel liefert,
            sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result


    def insert(self, info):
        """
        Einfügen einer Info-Instanz in die Datenbank.
        Dabei wird auch der Primärschlüssel der übergebenen Instanz geprüft und ggf. berichtigt.
        außerdem wird die Info des zu speichernden UserProfil Objekt eingetragen. Ausgabe: das bereits übergebene Info Objekt, jedoch mit ggf. korrigierter ID.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM info")
        tuples = cursor.fetchall()
        for maxid in tuples:
            if maxid[0] is not None:
                info.set_id(maxid[0] + 1)
            else:
                info.set_id(1)
        command = """ INSERT INTO info (id, timestamp, userprofile_id, answer_id, is_selection, is_searchprofile) VALUES (%s,%s,%s,%s,%s,%s)"""
        
        cursor.execute(
            command, 
            (
                info.get_id(),
                info.get_timestamp(),
                info.get_userprofile_id(),
                info.get_answer_id(),
                info.get_is_selection(),
                info.get_is_searchprofile()
,
          ),
        )
        self._cnx.commit()
        return info

    def update_by_id(self, info):

        cursor = self._cnx.cursor()

        command = "UPDATE info SET timestamp=%s, userprofile_id=%s, answer_id=%s, is_selection=%s, is_searchprofile=%s  WHERE id=%s"
        data = (info.get_timestamp(),
                info.get_userprofile_id(),
                info.get_answer_id(),
                info.get_is_selection(),
                info.get_is_searchprofile(),
                info.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, info):
        cursor = self._cnx.cursor()

        command = "DELETE FROM info WHERE id={}".format(info.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()