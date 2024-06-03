from flask import Flask
from routesConfig import register_blueprints

app = Flask(__name__)

# Register blueprints
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
