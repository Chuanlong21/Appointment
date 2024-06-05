from flask import Blueprint, render_template, request, jsonify
from controllers.addEventController import add

appointmentRoutes = Blueprint('appointmentRoutes', __name__)


@appointmentRoutes.route('/appointment')
def appointment():
    return render_template('appointment.html')


@appointmentRoutes.route('/addEvent', methods=['POST'])
def add_event():
    data = request.get_json()
    event = add(data)
    print(event)
    return jsonify(event)


@appointmentRoutes.route('/employee', methods=['GET'])
def get_events():
    events = [
        {
            'title': 'Event 1',
            'start': '2024-06-05T10:00:00',
            'end': '2024-06-05T11:00:00'
        },
        {
            'title': 'Event 2',
            'start': '2024-06-06T12:00:00',
            'end': '2024-06-06T13:00:00'
        }
        # Add more events as needed
    ]

    return jsonify(events)
