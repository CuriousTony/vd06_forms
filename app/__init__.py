from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'youll-never-know'

from app import routes
