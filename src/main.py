from flask_cors import CORS
from server.Views.config import app


CORS(app, resources=r'/HeyDateMe/*', supports_credentials=True)

from server.Views.UserProfileView import *
from server.Views.SearchProfileView import *
from server.Views.BlockedProfileView import *
from server.Views.ChatView import *
from server.Views.MemoBoardView import *
from server.Views.CharacteristicView import *
from server.Views.DescriptionView import *
from server.Views.SelectionView import *
from server.Views.InfoView import *
from server.Views.MessageView import *
from server.Views.MatchingView import *
from server.Views.SimilarityView import *

if __name__ == '__main__':
    app.run(debug=True)

    #note for me starting app main.py
