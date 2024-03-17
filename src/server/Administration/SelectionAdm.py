""" Dieser Code definiert eine Klasse namens SelectionAdm.py die Methoden zum Ausführen von CRUD-Operationen
 an Selection--Objekten enthält. Die Selection dient dazu die Eigenschfts-Info als Auswahl zu ergänzen, um den Nutzer eine auswählbare Antwort zur Verrfügung zu stellen. 
Jede Methode öffnet eine Verbindung zu einer entsprechenden Mapper-Klasse (z. B. UserProfileMapper, SearchProfileMapper etc.), um mit der Datenbank zu interagieren und die erforderlichen Operationen durchzuführen."""

from server.bo.SelectionBO import Selection
from server.db.SelectionMapper import SelectionMapper

class Administration:
    def __init__(self):
        pass
    
    def create_selection(self, characteristic_id, answer):
        selection = Selection()
        selection.set_characteristic_id(characteristic_id)
        selection.set_answer(answer)
        
        with SelectionMapper() as mapper:
            return mapper.insert(selection)
         
    def get_selection_by_id(self, id):
        with SelectionMapper() as mapper:
            return mapper.find_by_id(id)
        
    def get_all_selection(self):
        with SelectionMapper() as mapper:
            return mapper.find_all()

    def get_selection_by_characteristic_id(self,characteristic_id):
        with SelectionMapper() as mapper:
            return mapper.find_by_characteristic_id(characteristic_id)

    def update_selection_by_id(self, selection):
        with SelectionMapper() as mapper:
            return mapper.update_by_id(selection)

    def delete_selection(self, selection):
        with SelectionMapper() as mapper:
            mapper.delete(selection)
