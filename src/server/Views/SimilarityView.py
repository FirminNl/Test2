from server.Views.config import  api, datingapp
from flask_restx import Resource
from server.Views.Marshal import similarity
from server.Administration.SimilarityAdm import Administration as SimilarityAdm
from server.bo.SimilarityBO import Similarity
from  .SecurityDecorator import secured
from datetime import datetime

@datingapp.route('/similarity')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class SimilarityListOperations(Resource):
  
    @datingapp.marshal_list_with(similarity)
    # @secured
    def get(self):
        """Auslesen aller Scores"""
        adm = SimilarityAdm()
        similarity = adm.get_all_similarity()
        return similarity

    @datingapp.marshal_with(similarity, code=200)
    @datingapp.expect(similarity)
    def post(self):
        """Anlegen eines Scores"""
        adm = SimilarityAdm()
        similarity = Similarity.from_dict(api.payload)
        if similarity is not None:
            similarity = adm.create_similarity(
                matching_id=similarity.get_matching_id(),
                score=similarity.get_score(),

                )

            return similarity, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500
          
    @datingapp.route('/similarity/<int:matching_id>')
    @datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
    class SimilarityOperations(Resource):
        @datingapp.marshal_list_with(similarity)
        @secured
        def get(self, matching_id):
            """Auslesen eines bestimmten Scores anhand Matching-ID"""

            adm = SimilarityAdm()
            similarity = adm.get_similarity_by_matching_id(matching_id)
            return similarity
          
          
          
    @datingapp.route('/similarity/<int:id>')
    @datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
    class SimilarityByIdOperations(Resource):

        @datingapp.marshal_with(similarity, code=200)
        @datingapp.expect(similarity)
        def put(self, id):
            """ Update des Scores anhand ID"""

            similarity = Similarity.from_dict(api.payload)
            similarity.set_id(id)
            similarity.set_timestamp(datetime.now())
            adm = SimilarityAdm()
            adm.update_similarity_by_id(similarity)
            return similarity, 200


        @datingapp.marshal_list_with(similarity)
        def delete(self, id):
            """Löschen des Scores anhand ID"""
            adm = SimilarityAdm()
            similarity=adm.get_similarity_by_id(id)
            adm.delete_similarity(similarity)
            return 'Score gelöscht', 200
          
        @datingapp.marshal_list_with(similarity)
        def get(self, id):
            """Auslesen einer bestimmten Ähnlichkeit anhand ID"""
            adm = SimilarityAdm()
            selection = adm.get_similarity_by_id(id)
            return similarity
          
