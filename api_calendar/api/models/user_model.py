from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from extensions import db, ma

#User Model
class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50))

#User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'password')

user_schema =  UserSchema()
users_schema = UserSchema(many=True)