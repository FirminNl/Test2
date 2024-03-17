from server.bo.MemoBoardBO import MemoBoard
from server.db.MemoBoardMapper import MemoBoardMapper

class Administration:
    def __init__(self):
        pass
    def get_all_memo_board(self):
        with MemoBoardMapper() as mapper:
            return mapper.find_all()

    def get_memo_board_by_id(self, id):
        with MemoBoardMapper() as mapper:
            return mapper.find_by_id(id)

    def create_memo_board(self, userprofile_id, saved_id):
        memo_board = MemoBoard()
        memo_board.set_userprofile_id(userprofile_id)
        memo_board.set_saved_id(saved_id)
        
        with MemoBoardMapper() as mapper:
            return mapper.insert(memo_board)

    def get_memo_board_by_userprofile_id(self,userprofile_id):
        with MemoBoardMapper() as mapper:
            return mapper.find_by_userprofile_id(userprofile_id)

    def update_memo_board_by_id(self, memo_board):
        with MemoBoardMapper() as mapper:
            return mapper.update_by_id(memo_board)

    def delete_memo_board(self, memo_board):
        with MemoBoardMapper() as mapper:
            mapper.delete(memo_board)
