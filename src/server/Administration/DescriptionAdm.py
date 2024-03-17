from server.bo.DescriptionBO import Description
from server.db.DescriptionMapper import DescriptionMapper

"""
Description-spezifische Methoden
"""
class Administration:
    def __init__(self):
        pass
    
    def create_description(self, characteristic_id, answer, max_answer):
        description = Description()
        description.set_characteristic_id(characteristic_id)
        description.set_answer(answer)
        description.set_max_answer(max_answer)
        with DescriptionMapper() as mapper:
            return mapper.insert(description)
                                 
    def get_description_by_id(self, id):
        with DescriptionMapper() as mapper:
            return mapper.find_by_id(id)
    
    def get_description_by_characteristic_id(self,characteristic_id):
        with DescriptionMapper() as mapper:
            return mapper.find_by_characteristic_id(characteristic_id)

    def get_all_description(self):
        with DescriptionMapper() as mapper:
            return mapper.find_all()

    def update_description_by_id(self, description):
        with DescriptionMapper() as mapper:
            return mapper.update_by_id(description)

    def delete_description(self, description):
        with DescriptionMapper() as mapper:
            mapper.delete(description)
