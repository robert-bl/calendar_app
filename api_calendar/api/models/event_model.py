from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
import datetime

from extensions import db, ma

#Event Model
class Event(db.Model):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String)
    start_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


#Event Schema
class EventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'start_time', 'end_time', 'timestamp')

event_schema =  EventSchema()
events_schema = EventSchema(many=True)

