from flask import request
from google.auth.transport import requests
import google.oauth2.id_token

from server.Administration.UserProfileAdm import Administration as UserAdm
from server.Administration.CharacteristicAdm import Administration as CharAdm
from server.Administration.InfoAdm import Administration as InfoAdm
from server.Administration.SelectionAdm import Administration as SelecAdm
from server.Administration.DescriptionAdm import Administration as DescAdm


def secured(function):
    """Decorator zur Google Firebase-basierten Authentifizierung von Benutzern
    POLICY: Die hier demonstrierte Policy ist, dass jeder, der einen durch Firebase akzeptierten
    Account besitzt, sich an diesem System anmelden kann. Bei jeder Anmeldung werden Klarname,
    Mail-Adresse sowie die Google User ID in unserem System gespeichert bzw. geupdated. Auf diese
    Weise könnte dann für eine Erweiterung des Systems auf jene Daten zurückgegriffen werden.
    """
    firebase_request_adapter = requests.Request()

    def wrapper(*args, **kwargs):
        # Verify Firebase auth.
        id_token = request.cookies.get("token")
        error_message = None
        claims = None
        objects = None

        if id_token:
            try:
                # Verify the token against the Firebase Auth API. This example
                # verifies the token on each page load. For improved performance,
                # some applications may wish to cache results in an encrypted
                # session store (see for instance
                # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
                claims = google.oauth2.id_token.verify_firebase_token(
                    id_token, firebase_request_adapter
                )

                if claims is not None:

                    google_user_id = claims.get("user_id")
                    email = claims.get("email")

                    adm = UserAdm()
                    c_adm = CharAdm()
                    i_adm = InfoAdm()
                    s_adm = SelecAdm()
                    d_adm = DescAdm()
                    user_profile = adm.get_user_profile_by_guid(guid=google_user_id)
                    if user_profile is not None:
                        """Fall: Der Benutzer ist unserem System bereits bekannt.
                        Wir gehen davon aus, dass die google_user_id sich nicht ändert.
                        Wohl aber können sich der zugehörige Klarname (name) und die
                        E-Mail-Adresse ändern. Daher werden diese beiden Daten sicherheitshalber
                        in unserem System geupdated."""
                        user_profile.set_email(email)
                        user_profile.set_google_user_id(google_user_id)
                        adm.update_user_profile_by_id(user_profile=user_profile)

                        standart_char_user = c_adm.get_all_standart_by_user(user_profile.get_id())
                        all_standart_char = c_adm.get_all_characteristic_by_standart()
                        missing_char = [obj for obj in all_standart_char if obj.get_id() not in [b.get_id() for b in standart_char_user]]
                        for char in missing_char:
                            answer=None
                            if(char.get_is_selection()):
                                answer=s_adm.get_selection_by_characteristic_id(char.get_id())[0]
                            else:
                                answer=d_adm.create_description(characteristic_id=char.get_id(), answer="0", max_answer="")
                            i_adm.create_info(userprofile_id=user_profile.get_id(), answer_id=answer.get_id(), is_selection=char.get_is_selection(), is_searchprofile=False)
                        print("missing char", missing_char)
                    else:
                        """Fall: Der Benutzer war bislang noch nicht eingelogged.
                        Wir legen daher ein neues User-Objekt an, um dieses ggf. später
                        nutzen zu können.
                        """
                        user=adm.create_user_profile(
                           google_user_id,  email,  "", "", ""
                        )
                        all_standart_char = c_adm.get_all_characteristic_by_standart()

                        for char in all_standart_char:
                            print("char", all_standart_char)
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
                            i_adm.create_info(userprofile_id=user.get_id(), answer_id=answer.get_id(), is_selection=char.get_is_selection(), is_searchprofile=False)

                    print(request.method, request.path, "angefragt durch:", email)

                    objects = function(*args, **kwargs)
                    return objects
                else:
                    return "", 401  # UNAUTHORIZED !!!
            except ValueError as exc:
                # This will be raised if the token is expired or any other
                # verification checks fail.
                error_message = str(exc)
                return exc, 401  # UNAUTHORIZED !!!

        return "", 401  # UNAUTHORIZED !!!

    return wrapper