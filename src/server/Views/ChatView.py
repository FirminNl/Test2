from server.Views.config import api, datingapp
from flask_restx import Resource
from flask import request
from server.Views.Marshal import chat
from server.Administration.ChatAdm import Administration as ChatAdm
from server.bo.ChatBO import Chat
from  .SecurityDecorator import secured
from datetime import datetime



@datingapp.route('/chat')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ChatOperations(Resource):

    
    @datingapp.marshal_with(chat, code=200)
     # Wir erwarten ein chat-Objekt von Client-Seite.
    @datingapp.expect(chat)
    def post(self):
        """Anlegen eines Chats"""
        adm = ChatAdm()
        chat = Chat.from_dict(api.payload)
        if chat is not None:
            chat = adm.create_chat(
                sender_id=chat.get_sender_id(),
                receiver_id=chat.get_receiver_id(),
                accepted=chat.get_accepted(),
                is_open=chat.get_is_open(),
            )
            return chat, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return {"message": "Chat creation failed."}, 500
        
    @datingapp.marshal_with(chat, code=200)
    # Wir erwarten ein chat-Objekt von Client-Seite.
    def get(self):
        """Auslesen aller Chats"""
        adm = ChatAdm()
        chat = adm.get_all_chat()
        return chat
                


@datingapp.route('/chat/<int:id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ChatOperations(Resource):
        @datingapp.marshal_with(chat, code=200)
        @secured
    # Wir erwarten ein chat-Objekt von Client-Seite.
        def get(self, id):
            """Auslesen eines Chats anhand der ID"""
            adm = ChatAdm()
            chat = adm.get_chat_by_id(id)
            return chat, 200
            
    
        @datingapp.marshal_with(chat, code=200)
        # Wir erwarten ein chat-Objekt von Client-Seite.
        @datingapp.expect(chat)
        def put(self, id):
            """Update eines Chats anhand der ID"""
            chat = Chat.from_dict(api.payload)
            if  chat is not None:
                chat.set_id(id)
                chat.set_timestamp(datetime.now())  
                adm = ChatAdm()
                adm.update_chat(chat)
                return chat, 200
        
        def delete(self, id):
            """löschen eines Chats anhand der ID""" 
            adm = ChatAdm()
            chat = adm.get_chat_by_id(id)
            adm.delete_chat(chat)
            return 'konversation deleted', 200
        

    
@datingapp.route('/chat_invitation/<int:userprofile_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ChatOperations(Resource):
        @datingapp.marshal_list_with(chat, code=200)
        @secured
    # Wir erwarten ein chat-Objekt von Client-Seite.
        def get(self, userprofile_id):
            """Auslesen ankommender Chatanfragen anhand der ID"""
            adm = ChatAdm()
            chat = adm.get_chat_invitation(userprofile_id)
            return chat, 200
        
@datingapp.route('/chat_sent_invitation/<int:userprofile_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ChatOperations(Resource):
        @datingapp.marshal_list_with(chat, code=200)

        @secured
    # Wir erwarten ein chat-Objekt von Client-Seite.
        def get(self, userprofile_id):
            """Auslesen gesendeter Chatanfragen anhand der ID"""
            adm = ChatAdm()
            chat = adm.get_chat_sent_invitation(userprofile_id)
            return chat, 200
        
@datingapp.route('/chat_active/<int:userprofile_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ChatOperations(Resource):
        @datingapp.marshal_list_with(chat, code=200)
        @secured
    # Wir erwarten ein chat-Objekt von Client-Seite.
        def get(self, userprofile_id):
            """Auslesen aktiver Konversationen anhand der ID"""
            adm = ChatAdm()
            chat = adm.get_active_chats(userprofile_id)
            return chat, 200