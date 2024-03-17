from server.bo.CharacteristicBO import Characteristic
from server.db.CharacteristicMapper import CharacteristicMapper
from server.Administration.InfoAdm import Administration as InfoAdm 
from server.Administration.SelectionAdm import Administration as SelectionAdm 
from server.Administration.DescriptionAdm import Administration as DescriptionAdm 


class Administration:
    """Klasse für die Administration von Characteristic-Objekten"""

    def get_all_characteristic(self):
        with CharacteristicMapper() as mapper:
            return mapper.find_all()
        
    def get_all_characteristic_by_standart(self):
        with CharacteristicMapper() as mapper:
            return mapper.find_all_by_standart()
    
    def get_all_standart_by_user(self, user_id):
        infoAdm = InfoAdm()
        selecAdm = SelectionAdm()
        descAdm = DescriptionAdm()
        result = []
        all_info_objs = infoAdm.get_info_by_userprofile_id(user_id)
        for info in all_info_objs:
            if info.get_is_selection():
                answer = selecAdm.get_selection_by_id(info.get_answer_id())
                char = self.get_characteristic_by_id(answer.get_characteristic_id())
                if char.get_is_standart():
                    result.append(char)
            else:
                answer = descAdm.get_description_by_id(info.get_answer_id())
                char = self.get_characteristic_by_id(answer.get_characteristic_id())
                if char.get_is_standart():
                    result.append(char)
        return result

    def get_characteristic_by_id(self, characteristic_id):
        with CharacteristicMapper() as mapper:
            return mapper.find_by_id(characteristic_id)

    def create_characteristic(self, name, description, is_selection, author_id, is_standart):
        characteristic = Characteristic()
        characteristic.set_name(name)
        characteristic.set_description(description)
        characteristic.set_is_selection(is_selection)
        characteristic.set_author_id(author_id)
        characteristic.set_is_standart(is_standart)

        with CharacteristicMapper() as mapper:
            return mapper.insert(characteristic)

    def update_characteristic_by_id(self, characteristic):
        """Eine Eigenschaft nach der ID speichern"""
        with CharacteristicMapper() as mapper:
            return mapper.update(characteristic)

    def delete_characteristic(self, characteristic):
        """Die Eigenschaft löschen"""
        info_adm = InfoAdm()
        desc_adm = DescriptionAdm()
        selec_adm = SelectionAdm()
        all_connected_infos = info_adm.get_all_info_by_char(characteristic.get_id(), characteristic.get_is_selection())
        for info in all_connected_infos:
            if not characteristic.get_is_selection():
                desc_list = desc_adm.get_description_by_characteristic_id(characteristic.get_id())
                if desc_list is not  []:
                    for desc in desc_list:
                        desc_adm.delete_description(desc)
            else:
                selec_list = selec_adm.get_selection_by_characteristic_id(characteristic.get_id())
                if selec_list is not  []:
                    for selec in selec_list:
                        selec_adm.delete_selection(selec)
            info_adm.delete_info(info)
        with CharacteristicMapper() as mapper:
            mapper.delete(characteristic)
