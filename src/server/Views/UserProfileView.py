from server.Views.config import  api, datingapp
from flask_restx import Resource
from server.Views.Marshal import user_profile
from server.Administration.UserProfileAdm import Administration as UserProfileAdm
from server.bo.UserProfileBO import UserProfile
from  .SecurityDecorator import secured
from datetime import datetime



@datingapp.route('/user')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class UserProfileListOperations(Resource):


    @datingapp.marshal_list_with(user_profile)
    # @secured
    def get(self):
        """Auslesen aller User-Profile"""

        adm = UserProfileAdm()
        user = adm.get_all_user_profile()
        return user

    @datingapp.marshal_with(user_profile, code=200)
    # Wir erwarten ein user_profile-Objekt von Client-Seite.
    @datingapp.expect(user_profile)
    def post(self):
        """Anlegen eines User-Profils"""
        adm = UserProfileAdm()
        user_profile = UserProfile.from_dict(api.payload)
        if user_profile is not None:
            user_profile = adm.create_user_profile(
                email=user_profile.get_email(),
                google_user_id=user_profile.get_google_user_id(),
                firstname=user_profile.get_firstname(),
                surname=user_profile.get_surname(),
                about_me=user_profile.get_about_me(),
                )

            return user_profile, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@datingapp.route('/user-by-guid/<string:guid>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class UserProfileOperations(Resource):
    @datingapp.marshal_list_with(user_profile)
    @secured
    def get(self, guid):
        """Auslesen eines bestimmten User-Profils anhand Google-ID"""

        adm = UserProfileAdm()
        user_profile = adm.get_user_profile_by_guid(guid)
        return user_profile



@datingapp.route('/user/<int:id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class UserProfileByIdOperations(Resource):
    @datingapp.marshal_list_with(user_profile)
    def delete(self, id):
        """Löschen eines User-Profils anhand ID"""
        adm = UserProfileAdm()
        user=adm.get_user_profile_by_id(id)
        adm.delete_user_profile(user)
        return "", 200

    @datingapp.marshal_with(user_profile, code=200)
    @datingapp.expect(user_profile)
    def put(self, id):
        """ Update des User-Profils anhand ID"""

        user_profile = UserProfile.from_dict(api.payload)
        user_profile.set_id(id)
        user_profile.set_timestamp(datetime.now())
        adm = UserProfileAdm()
        adm.update_user_profile_by_id(user_profile)
        return user_profile, 200

    @datingapp.marshal_list_with(user_profile)
    def get(self, id):
        """Auslesen eines bestimmten User-Profils anhand ID"""

        adm = UserProfileAdm()
        user_profile = adm.get_user_profile_by_id(id)
        return user_profile