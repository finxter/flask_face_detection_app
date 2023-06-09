from flask import Flask
from secrets import token_hex


UPLOAD_FOLDER = 'app/static/uploads'
SECRET_KEY = token_hex(16)


app = Flask(__name__)

app.config['SEND_FILE_MAXIMUM_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY


from app import main
