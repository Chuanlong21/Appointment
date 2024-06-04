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
