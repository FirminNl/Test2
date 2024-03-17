from flask_restx import fields
from .config import api

bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines Business Object'),
    'timestamp': fields.String(attribute='_timestamp', description='Ein Erstellungsdatum'),
})

user_profile = api.inherit('user_profile', bo, {
    'google_user_id': fields.String(attribute='_google_user_id', description='Google User ID eines Benutzers'),
    'email': fields.String(attribute='_email', description='E-Mail-Adresse eines Benutzers'),
    'firstname': fields.String(attribute='_firstname', description='Vorname eines Benutzers'),
    'surname': fields.String(attribute='_surname', description='Nachname eines Benutzers'),
    'about_me': fields.String(attribute='_about_me', description='Profilbeschreibung eines Benutzers'),
})

search_profile = api.inherit('search_profile', bo, {
    'userprofile_id': fields.Integer(attribute='_userprofile_id', description='Nutzerprofil ID eines Benutzers'),
})

info = api.inherit('info', bo, {
    'userprofile_id': fields.Integer(attribute='_userprofile_id', description='Die ID des Benutzerprofils'),
    'answer_id': fields.Integer(attribute='_answer_id', description='Die ID der Antwort'),
    'is_selection': fields.Boolean(attribute='_is_selection', description='Gibt an, ob die Info eine Auswahlmöglichkeit ist'),
    'is_searchprofile': fields.Boolean(attribute='_is_searchprofile', description='Gibt an, ob die Info in Suchprofile gespeichert wird'),
})

characteristic = api.inherit('characteristic', bo, {
    'name': fields.String(attribute='_name', description='Der Name der Eigenschaft'),
    'description': fields.String(attribute='_description', description='Der Name der Eigenschaft'),
    'is_selection': fields.Boolean(attribute='_is_selection', description='Gibt an, ob die Eigenschaft eine Auswahlmöglichkeit ist'),
    'author_id': fields.Integer(attribute='_author_id', description='Die ID des Erstellers'),
    'is_standart': fields.Boolean(attribute='_is_standart', description='Der Standardwert der Eigenschaft'),
})

description = api.inherit('Description', bo, {
    'characteristic_id': fields.Integer(attribute='_characteristic_id', description='Die ID der Eigenschaft, auf die sich die Beschreibung bezieht'),
    'answer': fields.String(attribute='_answer', description='Die Antwort auf die Beschreibung'),
    'max_answer': fields.String(attribute='_max_answer', description='Die maximale Antwort auf die Beschreibung'),
})

selection = api.inherit('Selection', bo, {
    'characteristic_id': fields.Integer(attribute='_characteristic_id', description='Die ID der Eigenschaft, auf die sich die Auswahl bezieht'),
    'answer': fields.String(attribute='_answer', description='Die Antwort auf die Auswahl'),
})

memo_board = api.inherit('MemoBoard', bo, {
    'userprofile_id': fields.Integer(required=True, attribute='_userprofile_id', description='Die ID des Benutzerprofils'),
    'saved_id': fields.Integer(required=True, attribute='_saved_id', description='Die ID des gespeicherten Profils'),

})

blocked_profile = api.inherit('BlockedProfile', bo, {
    'userprofile_id': fields.Integer(required=True, attribute='_userprofile_id', description='Die ID des Benutzerprofils'),
    'blockeduser_id': fields.Integer(required=True, attribute='_blockeduser_id', description='Die ID des blockierten Profils'),

})


message = api.inherit('Message', bo, {
    'chat_id': fields.Integer(required=True, attribute='_chat_id', description='Die ID des Chats'),
    'content': fields.String(attribute='_content', description='Der Inhalt der Nachricht'),
    'sender_id': fields.Integer(required=True, attribute='_sender_id', description='Die ID des Absenders'),
})

chat = api.inherit('Chat', bo, {
    'sender_id': fields.Integer(required=True, attribute='_sender_id', description='Die ID des Absenders'),
    'receiver_id': fields.Integer(required=True, attribute='_receiver_id', description='Die ID des Empfängers'),
    'accepted': fields.Boolean(attribute='_accepted', description='Ein Boolean, der angibt, ob der Chat akzeptiert wurde'),
    'is_open': fields.Boolean(attribute='_is_open', description='Ein Boolean, der angibt, ob der Chat geöffnet ist'),
})

similarity = api.inherit('Similarity', bo, {
    'matching_id': fields.Integer(required=True, attribute='_matching_id', description='Die ID des Matchings'),
    'score': fields.Integer(required=True, attribute='_score', description='Die ID des Scores'),
})

matching = api.inherit('Matching', bo, {
    'userprofile_id': fields.Integer(required=True, attribute='_userprofile_id', description='Die ID des Nutzerprofils'),
    'candidateprofile_id': fields.Integer(required=True, attribute='_candidateprofile_id', description='Die ID des Kandidatenprofils'),
    'unseen_profile': fields.Boolean(attribute='_unseen_profile', description='Ein Boolean, der angibt, ob das Kandidatenprofil gesehen wurde'),
})