from flask_restx import Api
from flask import Flask
from flask import request, redirect, url_for


app = Flask(__name__, static_folder='../../build', static_url_path='/')
app.config['ERROR_404_HELP'] = False
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def handle_404(e):
    if request.path.startswith('/HeyDateMe'):
        return "Fehler", 404
    else:
        return redirect(url_for('index'))
    
api = Api(app, version='1.0', title='HeyDateMe API', description='Eine API für die DatingApp-HeyDateMe.')
datingapp = api.namespace('HeyDateMe', description='Funktionen der DatingApp-HeyDateMe')