from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c786ae2529594d'
app.config['UPLOAD_FOLDER_WAVE'] = 'static/images/wave'
app.config['UPLOAD_FOLDER_SPIRAL'] = 'static/images/spiral'

from Files import route