from server.Views.config import  api, datingapp
from flask_restx import Resource
from server.Views.Marshal import selection
from server.Administration.SelectionAdm import Administration as SelectionAdm
from server.bo.SelectionBO import Selection
from  .SecurityDecorator import secured
from datetime import datetime

@datingapp.route('/selection')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class SelectionListOperations(Resource):

    @datingapp.marshal_list_with(selection)
    # @secured
    def get(self):
        """Auslesen aller Auswahlen"""
        adm = SelectionAdm()
        selection = adm.get_all_selection()
        return selection

    @datingapp.marshal_with(selection, code=200)
    @datingapp.expect(selection)
    def post(self):
        """Anlegen einer Auswahl"""
        adm = SelectionAdm()
        selection = Selection.from_dict(api.payload)
        if selection is not None:
            selection = adm.create_selection(
                characteristic_id=selection.get_characteristic_id(),
                answer=selection.get_answer(),
                )

            return selection, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500

@datingapp.route('/selection-by-char/<int:characteristic_id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class SelectionOperations(Resource):
    @datingapp.marshal_list_with(selection)
    @secured
    def get(self, characteristic_id):
        """Auslesen einer bestimmten Auswahl anhand Eigenschaft-ID"""

        adm = SelectionAdm()
        selection = adm.get_selection_by_characteristic_id(characteristic_id)
        return selection
@datingapp.route('/selection/<int:id>')
@datingapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class SelectionByIdOperations(Resource):

    @datingapp.marshal_list_with(selection)
    @secured
    def get(self,id):
        """Auslesen einer bestimmten Auswahl anhand Eigenschaft-ID"""

        adm = SelectionAdm()
        selection = adm.get_selection_by_id(id)
        return selection
    
    @datingapp.marshal_with(selection, code=200)
    @datingapp.expect(selection)
    def put(self, id):
        """ Update einer bestimmten Auswahl anhand ID"""

        selection = Selection.from_dict(api.payload)
        selection.set_id(id)
        selection.set_timestamp(datetime.now())
        adm = SelectionAdm()
        adm.update_selection_by_id(selection)
        return selection, 200


    @datingapp.marshal_list_with(selection)
    def delete(self, id):
        """Löschen einer bestimmten Auswahl anhand ID"""
        adm = SelectionAdm()
        selection=adm.get_selection_by_id(id)
        adm.delete_selection(selection)
        return 'Auswahl gelöscht', 200
    
    @datingapp.marshal_list_with(selection)
    def get(self, id):
        """Auslesen einer bestimmten Auswahl anhand ID"""

        adm = SelectionAdm()
        selection = adm.get_selection_by_id(id)
        return selection
