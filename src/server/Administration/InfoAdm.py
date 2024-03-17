from server.bo.InfoBO import Info
from server.db.InfoMapper import InfoMapper

class Administration:
    def __init__(self):
        pass
    def get_all_info_by_char(self, characteristic_id, is_selection):
        with InfoMapper() as mapper:
            return mapper.find_all_by_char(characteristic_id, is_selection)

    def get_info_by_id(self,id):
        with InfoMapper() as mapper:
            return mapper.find_by_id(id)

    def get_info_by_userprofile_id(self,userprofile_id):
        with InfoMapper() as mapper:
            return mapper.find_by_userprofile_id(userprofile_id)
    def get_info_by_searchprofile_id(self,searchprofile_id):
        with InfoMapper() as mapper:
            return mapper.find_by_searchprofile_id(searchprofile_id)

    def create_info(self, userprofile_id, answer_id, is_selection, is_searchprofile):
        info = Info()
        info.set_userprofile_id(userprofile_id)
        info.set_answer_id(answer_id)
        info.set_is_selection(is_selection)
        info.set_is_searchprofile(is_searchprofile)

        with InfoMapper() as mapper:
            return mapper.insert(info)

    def update_info_by_id(self, info):
        with InfoMapper() as mapper:
            return mapper.update_by_id(info)

    def delete_info(self, info):
        with InfoMapper() as mapper:
            mapper.delete(info)