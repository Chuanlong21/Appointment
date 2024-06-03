# routes register list
from routes.indexRoutes import indexRoutes
from routes.appointmentRoutes import appointmentRoutes


def register_blueprints(app):
    app.register_blueprint(indexRoutes)
    app.register_blueprint(appointmentRoutes)
