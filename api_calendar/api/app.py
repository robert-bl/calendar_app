from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from extensions import db
from settings import db_url
from models import User, Event


load_dotenv()

app=Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()