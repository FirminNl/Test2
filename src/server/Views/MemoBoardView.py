from server.Views.config import api, datingapp
from flask_restx import Resource
from server.Views.Marshal import memo_board
from server.Administration.MemoBoardAdm import Administration as MemoBoardAdm
from server.bo.MemoBoardBO import MemoBoard
from  .SecurityDecorator import secured
from datetime import datetime

@datingapp.route('/memoboard')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class MemoBoardListOperations(Resource):

    @datingapp.marshal_list_with(memo_board)
    # @secured
    def get(self):
        """Auslesen aller Merkzettel Einträge"""
        adm = MemoBoardAdm()
        memo = adm.get_all_memo_board()
        return memo

    @datingapp.marshal_with(memo_board, code=200)
    @datingapp.expect(memo_board)
    def post(self):
        """Anlegen eines Merkzettel-Eintrags"""
        adm = MemoBoardAdm()
        memo_board = MemoBoard.from_dict(api.payload)
        if memo_board is not None:
            memo_board = adm.create_memo_board(
                userprofile_id=memo_board.get_userprofile_id(),
                saved_id=memo_board.get_saved_id(),
                )

            return memo_board, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500

@datingapp.route('/memoboard/<int:userprofile_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class SearchProfileOperations(Resource):
    @datingapp.marshal_list_with(memo_board)
    @secured
    def get(self, userprofile_id):
        """Auslesen eines bestimmten Merkeztteleintrags anhand User-ID"""

        adm = MemoBoardAdm()
        memo_board = adm.get_memo_board_by_userprofile_id(userprofile_id)
        return memo_board

@datingapp.route('/memoboard/<int:id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class BlockedProfileByIdOperations(Resource):
    @datingapp.marshal_with(memo_board, code=200)
    @datingapp.expect(memo_board)
    def put(self, id):
        """ Update des Merkzetteleintrags anhand ID"""
        memo_board = MemoBoard.from_dict(api.payload)
        memo_board.set_id(id)
        memo_board.set_timestamp(datetime.now())
        adm = MemoBoardAdm()
        adm.update_memo_board_by_id(memo_board)
        return memo_board, 200

    @datingapp.marshal_list_with(memo_board)
    def delete(self, id):
        """Löschen eines Merkzetteleintrags anhand ID"""
        adm = MemoBoardAdm()
        memo_board=adm.get_memo_board_by_id(id)
        adm.delete_memo_board(memo_board)
        return "", 200
