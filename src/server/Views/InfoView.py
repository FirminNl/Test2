from server.Views.config import  api, datingapp
from flask_restx import Resource
from server.Views.Marshal import info
from server.Administration.InfoAdm import Administration as InfoAdm
from server.bo.InfoBO import Info
from  .SecurityDecorator import secured
from datetime import datetime

@datingapp.route('/info')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class InfoListOperations(Resource):


    @datingapp.marshal_with(info, code=200)
    @datingapp.expect(info)
    def post(self):
        """Anlegen einer Antwort"""
        adm = InfoAdm()
        info = Info.from_dict(api.payload)
        if info is not None:
            info = adm.create_info(
                userprofile_id=info.get_userprofile_id(),
                answer_id=info.get_answer_id(),
                is_selection=info.get_is_selection(),
                is_searchprofile=info.get_is_searchprofile()
            )

            return info, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@datingapp.route('/info-userprofile/<int:userprofile_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class InfoOperations(Resource):
    @datingapp.marshal_list_with(info)
    @secured
    def get(self, userprofile_id):
        """Auslesen einer bestimmten Antwort anhand UserProfil-ID"""

        adm = InfoAdm()
        info = adm.get_info_by_userprofile_id(userprofile_id)
        return info

@datingapp.route('/info-searchprofile/<int:searchprofile_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class InfoOperations(Resource):
    @datingapp.marshal_list_with(info)
    @secured
    def get(self, searchprofile_id):
        """Auslesen einer bestimmten Antowrt anhand Suchprofil-ID"""

        adm = InfoAdm()
        info = adm.get_info_by_searchprofile_id(searchprofile_id)
        return info


@datingapp.route('/info/<int:id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class InfoByIdOperations(Resource):

    @datingapp.marshal_with(info, code=200)
    @datingapp.expect(info)
    def put(self, id):
        """ Update einer bestimmten Antwort anhand ID"""

        info = Info.from_dict(api.payload)
        info.set_id(id)
        info.set_timestamp(datetime.now())
        adm = InfoAdm()
        adm.update_info_by_id(info)
        return info, 200

    @datingapp.marshal_list_with(info)
    def delete(self, id):
        """Löschen einer bestimmten Antwort anhand ID"""
        adm = InfoAdm()
        info = adm.get_info_by_id(id)
        adm.delete_info(info)
        return 'Antwort gelöscht', 200
    
    @datingapp.marshal_list_with(info)
    def get(self, id):
        """Auslesen einer bestimmten Info anhand ID"""

        adm = InfoAdm()
        info = adm.get_info_by_id(id)
        return info