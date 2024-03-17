from server.Views.config import  api, datingapp
from flask_restx import Resource
from server.Views.Marshal import search_profile
from server.Administration.SearchProfileAdm import Administration as SearchProfileAdm
from server.bo.SearchProfileBO import SearchProfile
from  .SecurityDecorator import secured
from datetime import datetime
from server.Administration.CharacteristicAdm import Administration as CharacteristicAdm
from server.Administration.InfoAdm import Administration as InfoAdm
from server.Administration.SelectionAdm import Administration as SelectionAdm
from server.Administration.DescriptionAdm import Administration as DescriptionAdm
@datingapp.route('/searchprofile')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class SearchProfileListOperations(Resource):

    @datingapp.marshal_list_with(search_profile)
    # @secured
    def get(self):
        """Auslesen aller Such-Profile"""
        adm = SearchProfileAdm()
        search = adm.get_all_search_profile()
        return search

    @datingapp.marshal_with(search_profile, code=200)
    @datingapp.expect(search_profile)
    def post(self):
        """Anlegen eines Such-Profils"""
        adm = SearchProfileAdm()
        search_profile = SearchProfile.from_dict(api.payload)
        if search_profile is not None:
            search_profile = adm.create_search_profile(
                userprofile_id=search_profile.get_userprofile_id(),
                )
            c_adm = CharacteristicAdm()
            i_adm = InfoAdm()
            s_adm = SelectionAdm()
            d_adm = DescriptionAdm()
            all_standart_char = c_adm.get_all_characteristic_by_standart()
            for char in all_standart_char:
                answer=None
                if(char.get_is_selection()):
                    answer=s_adm.get_selection_by_characteristic_id(char.get_id())[0]
                else:
                     system_desc = d_adm.get_description_by_characteristic_id(char.get_id())[0]
                     if system_desc.get_max_answer() != "":
                         max_answer="-"
                     else:
                         max_answer=""
                     answer=d_adm.create_description(characteristic_id=char.get_id(), answer="", max_answer=max_answer)
                i_adm.create_info(userprofile_id=search_profile.get_id(), answer_id=answer.get_id(), is_selection=char.get_is_selection(), is_searchprofile=True)
            return search_profile, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@datingapp.route('/searchprofile/<int:userprofile_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class SearchProfileOperations(Resource):
    @datingapp.marshal_list_with(search_profile)
    @secured
    def get(self, userprofile_id):
        """Auslesen eines bestimmten Such-Profils anhand User-ID"""

        adm = SearchProfileAdm()
        search_profile = adm.get_search_profile_by_userprofile_id(userprofile_id)
        return search_profile

@datingapp.route('/searchprofile/<int:id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class SearchProfileByIdOperations(Resource):

    @datingapp.marshal_with(search_profile, code=200)
    @datingapp.expect(search_profile)
    def put(self, id):
        """ Update des Such-Profils anhand ID"""

        search_profile = SearchProfile.from_dict(api.payload)
        search_profile.set_id(id)
        search_profile.set_timestamp(datetime.now())
        adm = SearchProfileAdm()
        adm.update_search_profile_by_id(search_profile)
        return search_profile, 200


    @datingapp.marshal_list_with(search_profile)
    def delete(self, id):
        """Löschen eines Such-Profils anhand ID"""
        adm = SearchProfileAdm()
        searchprofile=adm.get_search_profile_by_id(id)
        adm.delete_search_profile(searchprofile)
        return "", 200