from server.Views.config import  api, datingapp
from flask_restx import Resource
from server.Views.Marshal import matching
from server.Administration.MatchingAdm import Administration as MatchingAdm
from server.bo.MatchingBO import Matching
from  .SecurityDecorator import secured
from datetime import datetime

@datingapp.route('/matching')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class MatchingListOperations(Resource):

    @datingapp.marshal_list_with(matching)
    # @secured
    def get(self):
        """Auslesen aller Vorschläge"""
        adm = MatchingAdm()
        matching = adm.get_all_matching()
        return matching

    @datingapp.marshal_with(matching, code=200)
    @datingapp.expect(matching)
    def post(self):
        """Anlegen eines Vorschlags"""
        adm = MatchingAdm()
        matching = Matching.from_dict(api.payload)
        if matching is not None:
            matching = adm.create_matching(
                userprofile_id=matching.get_userprofile_id(),
                candidateprofile_id=matching.get_candidateprofile_id(),
                unseen_profile=matching.get_unseen_profile()
                )

            return matching, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@datingapp.route('/matching/<int:userprofile_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class MatchingOperations(Resource):
    @datingapp.marshal_list_with(matching)
    def get(self, userprofile_id):
        """Auslesen eines bestimmten Vorschlags anhand User-ID"""

        adm = MatchingAdm()
        matching = adm.matching(userprofile_id)
        return matching

@datingapp.route('/matching/<int:id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class MatchingByIdOperations(Resource):

    @datingapp.marshal_with(matching, code=200)
    @datingapp.expect(matching)
    def put(self, id):
        """ Update des Vorschlags anhand ID"""

        matching = Matching.from_dict(api.payload)
        matching.set_id(id)
        matching.set_timestamp(datetime.now())
        adm = MatchingAdm()
        adm.update_matching_by_id(matching)
        return matching, 200


    @datingapp.marshal_list_with(matching)
    def delete(self, id):
        """Löschen eines Vorschlags anhand ID"""
        adm = MatchingAdm()
        matching=adm.get_matching_by_id(id)
        adm.delete_matching(matching)
        return 'Vorschlag gelöscht', 200
