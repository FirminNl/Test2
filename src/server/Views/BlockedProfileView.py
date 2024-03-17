from server.Views.config import  api, datingapp
from flask_restx import Resource
from server.Views.Marshal import blocked_profile
from server.Administration.BlockedProfileAdm import Administration as BlockedProfileAdm
from server.bo.BlockedProfileBO import BlockedProfile
from  .SecurityDecorator import secured
from datetime import datetime

@datingapp.route('/blockedprofile')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class BlockedProfileListOperations(Resource):

    @datingapp.marshal_list_with(blocked_profile)
    # @secured
    def get(self):
        """Auslesen aller blockierten Profile"""
        adm = BlockedProfileAdm()
        blocked = adm.get_all_blocked_profile()
        return blocked

    @datingapp.marshal_with(blocked_profile, code=200)
    # Wir erwarten ein user_profile-Objekt von Client-Seite.
    @datingapp.expect(blocked_profile)
    def post(self):
        """Anlegen einer Blockierung"""
        adm = BlockedProfileAdm()
        blocked_profile = BlockedProfile.from_dict(api.payload)
        if blocked_profile is not None:
            blocked_profile = adm.create_blocked_profile(
                userprofile_id=blocked_profile.get_userprofile_id(),
                blockeduser_id=blocked_profile.get_blockeduser_id(),
                )

            return blocked_profile, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500



@datingapp.route('/blockedprofile/<int:userprofile_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class BlockedProfileOperations(Resource):
    @datingapp.marshal_list_with(blocked_profile)
    @secured
    def get(self, userprofile_id):
        """Auslesen der blockierten Profile anhand User-ID"""

        adm = BlockedProfileAdm()
        blocked_profile = adm.get_blocked_profile_by_userprofile_id(userprofile_id)
        return blocked_profile

@datingapp.route('/blockedprofile/<int:id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class BlockedProfileByIdOperations(Resource):
    @datingapp.marshal_with(blocked_profile, code=200)
    @datingapp.expect(blocked_profile)
    def put(self, id):
        """ Update des Blocked-Profils anhand ID"""
        blocked_profile = BlockedProfile.from_dict(api.payload)
        blocked_profile.set_id(id)
        blocked_profile.set_timestamp(datetime.now())
        adm = BlockedProfileAdm()
        adm.update_blocked_profile_by_id(blocked_profile)
        return blocked_profile, 200

    @datingapp.marshal_list_with(blocked_profile)
    def delete(self, id):
        """Löschen einer Blockierung anhand ID"""
        adm = BlockedProfileAdm()
        blocked_profile=adm.get_blocked_profile_by_id(id)
        adm.delete_blocked_profile(blocked_profile)
        return "", 200

