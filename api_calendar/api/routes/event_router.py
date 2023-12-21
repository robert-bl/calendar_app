from flask import Blueprint, request, jsonify
from sqlalchemy import select

from extensions import db
from models import Event, event_schema, events_schema

event_routes = Blueprint('event', __name__, url_prefix='/event')

@event_routes.route('/create', methods=['POST'])
def create_event():
    name = request.json['name']
    description = request.json['description']
    start_time = request.json['start_time']
    end_time = request.json['end_time']

    new_event = Event(name=name, description=description, start_time=start_time, end_time=end_time)

    db.session.add(new_event)
    db.session.commit()

    return event_schema.jsonify(new_event)

# @event_routes.route('get/<id>', methods=['GET'])
# def get_by_id(id):
#     event = select(Event).where(Event.id == id)

#     return event_schema.jsonify(event)

@event_routes.route('/get_date/<date>', methods=['GET'])
def get_by_date(date):
    events = Event.query