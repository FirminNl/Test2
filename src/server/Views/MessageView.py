from server.Views.config import api, datingapp
from flask_restx import Resource
from flask import request
from server.Views.Marshal import message
from server.Administration.MessageAdm import Administration as MessageAdm
from server.bo.MessageBO import Message
from  .SecurityDecorator import secured
from datetime import datetime



@datingapp.route('/message')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ChatOperations(Resource):

    
    @datingapp.marshal_with(message, code=200)
     # Wir erwarten ein Nachrichten-Objekt von Client-Seite.
    @datingapp.expect(message)
    def post(self):
        """Anlegen einer Nachricht"""
        adm = MessageAdm()
        message = Message.from_dict(api.payload)
        if message is not None:
            message = adm.create_message(
                chat_id=message.get_chat_id(),
                content=message.get_content(),
                sender_id=message.get_sender_id(),
            )
            return message, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500
        

    @datingapp.marshal_list_with(message)
    # @secured
    def get(self):
        """Auslesen aller Nachrichten"""

        adm = MessageAdm()
        message = adm.get_all_messages()
        return message, 200
    
@datingapp.route('/message/<int:id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class MessageOperations(Resource):
    
        @datingapp.marshal_with(message,200)
        @secured
        # Wir erwarten ein chat-Objekt von Client-Seite.
        def get(self, id):
            """Auslesen einer bestimmten Nachrichten ID"""
            adm = MessageAdm()
            message = adm.get_message_by_id(id)
            return message

        @datingapp.marshal_with(message, code=200)
        @datingapp.expect(message)
        def put(self, id):
            """update Nachrichten anhand ID"""
        
            message = Message.from_dict(api.payload)
            message.set_id(id)
            message.set_timestamp(datetime.now())
            adm = MessageAdm()
            adm.update_message_by_id(message)
            return message, 200

        @datingapp.marshal_with(message, code=200)
        def delete(self, id):
            """Löschen einer Nachricht anhand ID"""
            adm = MessageAdm()
            message =adm.get_message_by_id(id)
            adm.delete_message(message)
            return "chat deleted", 200
        


@datingapp.route('/message_from_chat/<int:chat_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class MessageOperations(Resource):
    
        @datingapp.marshal_with(message,200)
        # Wir erwarten ein chat-Objekt von Client-Seite.
        def get(self, chat_id):
            """Auslesen einer bestimmten Nachrichten anhand Chat-ID"""
            adm = MessageAdm()
            message = adm.get_message_by_chat_id(chat_id)
            return message