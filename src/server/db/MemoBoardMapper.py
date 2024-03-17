from server.db.Mapper import Mapper
from server.bo.MemoBoardBO import MemoBoard


class MemoBoardMapper(Mapper):
    """Mapper-Klasse, die MemoBoard-Objekte auf eine relationale Datenbank abbildet"""

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller MemoBoard-Objekte aus der Datenbank"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id, saved_id FROM memoboard".format(self)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, userprofile_id, saved_id) in tuples:
            memo_board = MemoBoard()
            memo_board.set_id(id)
            memo_board.set_timestamp(timestamp)
            memo_board.set_userprofile_id(userprofile_id)
            memo_board.set_saved_id(saved_id)
            result.append(memo_board)

        self._cnx.commit()
        cursor.close()
        return result


    def find_by_userprofile_id(self, userprofile_id):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, timestamp, userprofile_id, saved_id FROM memoboard WHERE userprofile_id='{}'".format(userprofile_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, timestamp, userprofile_id, saved_id) in tuples:
            memo_board = MemoBoard()
            memo_board.set_id(id)
            memo_board.set_timestamp(timestamp)
            memo_board.set_userprofile_id(userprofile_id)
            memo_board.set_saved_id(saved_id)
            result.append(memo_board)

        self._cnx.commit()

        cursor.close()

        return result

    def insert(self, memo_board):
        """Einfügen eines MemoBoard-Objekts in die Datenbank"""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM memoboard")
        tuples = cursor.fetchall()
        for maxid in tuples:
            if maxid[0] is not None:
                memo_board.set_id(maxid[0] + 1)
            else:
                memo_board.set_id(1)
        command = """INSERT INTO memoboard (id, timestamp, userprofile_id, saved_id) 
        VALUES (%s,%s,%s,%s)"""

        cursor.execute(
            command,
            (
                memo_board.get_id(),
                memo_board.get_timestamp(),
                memo_board.get_userprofile_id(),
                memo_board.get_saved_id()
            ),
        )
        self._cnx.commit()

        return memo_board

    def find_by_id(self, id):
        """Suchen eines MemoBoard-Objekts mit gegebener ID"""

        cursor = self._cnx.cursor()

        command = "SELECT id, timestamp, userprofile_id, saved_id FROM " \
                  "memoboard WHERE id={}".format(id)

        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, timestamp, userprofile_id, saved_id) = tuples[0]
            memo_board = MemoBoard()
            memo_board.set_id(id)
            memo_board.set_timestamp(timestamp)
            memo_board.set_userprofile_id(userprofile_id)
            memo_board.set_saved_id(saved_id)

            result = memo_board
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def update_by_id(self, memo_board):

        cursor = self._cnx.cursor()

        command = "UPDATE memoboard SET timestamp=%s, userprofile_id=%s, saved_id=%s WHERE id=%s"

        data = (memo_board.get_timestamp(),
                memo_board.get_userprofile_id(),
                memo_board.get_saved_id(),
                memo_board.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, memo_board):
        """Löschen eines MemoBoard-Objekts aus der Datenbank"""

        cursor = self._cnx.cursor()

        command = """DELETE FROM memoboard WHERE id={}""".format(memo_board.get_id())
        cursor.execute(command)
        
        self._cnx.commit()
        cursor.close()
