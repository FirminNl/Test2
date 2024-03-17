from server.Views.config import  api, datingapp
from flask_restx import Resource
from server.Views.Marshal import description
from server.Administration.DescriptionAdm import Administration as DescriptionAdm
from server.bo.DescriptionBO import Description
from  .SecurityDecorator import secured
from datetime import datetime

@datingapp.route('/description')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class DescriptionListOperations(Resource):

    @datingapp.marshal_list_with(description)
    # @secured
    def get(self):
        """Auslesen aller Beschreibungsantworten"""
        adm = DescriptionAdm()
        description = adm.get_all_description()
        return description

    @datingapp.marshal_with(description, code=200)
    @datingapp.expect(description)
    def post(self):
        """Anlegen einer Beschreibungsantwort"""
        adm = DescriptionAdm()
        description = Description.from_dict(api.payload)
        if description is not None:
            description = adm.create_description(
                characteristic_id=description.get_characteristic_id(),
                answer=description.get_answer(),
                max_answer=description.get_max_answer(),
                )

            return description, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500

@datingapp.route('/description-by-char/<int:characteristic_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class DescriptionOperations(Resource):
    @datingapp.marshal_list_with(description)
    # @secured 
    def get(self, characteristic_id):
        """Auslesen einer bestimmten (freien) Antwort anhand Eigenschaft-ID"""

        adm = DescriptionAdm()
        description = adm.get_description_by_characteristic_id(characteristic_id)
        return description

@datingapp.route('/description-default')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class DescriptionOperations(Resource):
    @datingapp.marshal_list_with(description)
    # @secured 
    def get(self):
        """Auslesen einer bestimmten (freien) Antwort anhand Eigenschaft-ID"""

        adm = DescriptionAdm()
        description = adm.get_description_default()
        return description

@datingapp.route('/description/<int:id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class DescriptionByIdOperations(Resource):

    @datingapp.marshal_list_with(description)
    # @secured 
    def get(self, id):
        """Auslesen einer bestimmten (freien) Antwort anhand Eigenschaft-ID"""

        adm = DescriptionAdm()
        description = adm.get_description_by_id(id)
        return description

    @datingapp.marshal_with(description, code=200)
    @datingapp.expect(description)
    def put(self, id):
        """ Update einer bestimmten (freien) Antwort anhand ID"""

        description = Description.from_dict(api.payload)
        description.set_id(id)
        description.set_timestamp(datetime.now())
        adm = DescriptionAdm()
        adm.update_description_by_id(description)
        return description, 200


    @datingapp.marshal_list_with(description)
    def delete(self, id):
        """Löschen einer bestimmten (freien) Antwort anhand ID"""
        adm = DescriptionAdm()
        description=adm.get_description_by_id(id)
        adm.delete_description(description)
        return "", 200
    
    @datingapp.marshal_list_with(description)
    def get(self, id):
        """Auslesen einer bestimmten textuellen Beschreibung anhand ID"""

        adm = DescriptionAdm()
        description = adm.get_description_by_id(id)
        return description
