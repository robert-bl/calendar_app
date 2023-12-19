from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv

from settings import db_url

load_dotenv()

app=Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)
ma=Marshmallow(app)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()