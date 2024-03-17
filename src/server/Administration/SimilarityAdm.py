""" Dieser Code definiert eine Klasse namens SimilarityAdm.py, die Methoden zum Ausführen von CRUD-Operationen
 an Similarity-Objekten enthält und einen Matching-Algorithmus, um eine Person anhand ihres Suchprofils mit anderen potenziellen Profilen abzugleichen. 
Jede Methode öffnet eine Verbindung zu einer entsprechenden Mapper-Klasse (z. B. UserProfileMapper, SearchProfileMapper etc.), um mit der Datenbank zu interagieren und die erforderlichen Operationen durchzuführen."""
from server.bo.SimilarityBO import Similarity
from server.db.SimilarityMapper import SimilarityMapper

class Administration (object):
    def __init__(self):
        pass
    """
    Similarity-spezifische Methoden
    """
    class SimilarityAdministration:
        def __init__(self):
            pass
    
    def get_all_similarity(self):
        with SimilarityMapper() as mapper:
            return mapper.find_all()
       
    def get_similarity_by_matching_id(self, matching_id):
        with SimilarityMapper() as mapper:
            return mapper.find_by_matching_id(matching_id)
        
    def get_similarity_by_id(self, id):
        with SimilarityMapper() as mapper:
            return mapper.find_by_id(id)

    def create_similarity(self, matching_id, score):
        similarity = Similarity()
        similarity.set_matching_id(matching_id)
        similarity.set_score(score)

        with SimilarityMapper() as mapper:
            return mapper.insert(similarity)

    def update_similarity_by_id(self, similarity):
        with SimilarityMapper() as mapper:
            return mapper.update_by_id(similarity)

    def delete_similarity(self, similarity):
        with SimilarityMapper() as mapper:
            mapper.delete(similarity)
        
