from server.Views.config import  api, datingapp
from flask_restx import Resource
from server.Views.Marshal import characteristic
from server.Administration.CharacteristicAdm import Administration as CharacteristicAdm
from server.bo.CharacteristicBO import Characteristic
from  .SecurityDecorator import secured
from datetime import datetime

@datingapp.route('/characteristic')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class CharacteristicListOperations(Resource):

    @datingapp.marshal_list_with(characteristic)
    # @secured
    def get(self):
        """Auslesen aller Eigenschaften"""
        adm = CharacteristicAdm()
        characteristic = adm.get_all_characteristic()
        return characteristic

    @datingapp.marshal_with(characteristic, code=200)
    @datingapp.expect(characteristic)
    def post(self):
        """Anlegen einer Eigenschaft"""
        adm = CharacteristicAdm()
        characteristic = Characteristic.from_dict(api.payload)
        if characteristic is not None:
            characteristic = adm.create_characteristic(
                name=characteristic.get_name(),
                description=characteristic.get_description(),
                is_selection=characteristic.get_is_selection(),
                author_id=characteristic.get_author_id(),
                is_standart=characteristic.get_is_standart()
                )

            return characteristic, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@datingapp.route('/characteristic/<int:characteristic_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class CharacteristicOperations(Resource):
    @datingapp.marshal_list_with(characteristic)
    @secured
    def get(self, characteristic_id):
        """Auslesen der Eigenschaft anhand Eigenschaft-ID"""

        adm = CharacteristicAdm()
        characteristic = adm.get_characteristic_by_id(characteristic_id)
        return characteristic
    
@datingapp.route('/default-characteristic')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class CharacteristicOperations(Resource):
    @datingapp.marshal_list_with(characteristic)
    @secured
    def get(self):
        """Auslesen der Eigenschaft anhand Eigenschaft-ID"""

        adm = CharacteristicAdm()
        characteristic = adm.get_all_characteristic_by_standart()
        return characteristic

@datingapp.route('/characteristic/<int:id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class CharacteristicByIdOperations(Resource):
    @datingapp.marshal_with(characteristic, code=200)
    @datingapp.expect(characteristic)
    def put(self, id):
        """ Update der Eigenschaft anhand ID"""
        characteristic = Characteristic.from_dict(api.payload)
        characteristic.set_id(id)
        characteristic.set_timestamp(datetime.now())
        adm = CharacteristicAdm()
        adm.update_characteristic_by_id(characteristic)
        return characteristic, 200

    @datingapp.marshal_list_with(characteristic)
    def delete(self, id):
        """Löschen einer Eigenschaft anhand ID"""
        adm = CharacteristicAdm()
        characteristic=adm.get_characteristic_by_id(id)
        adm.delete_characteristic(characteristic)
        return 'Eigenschaft gelöscht', 200
