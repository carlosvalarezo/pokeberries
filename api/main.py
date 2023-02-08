import os
from flask import Flask
from flask_cors import CORS
from routes.health import health_endpoint
from routes.berries import berries_endpoint

app = Flask(__name__)
app.register_blueprint(health_endpoint)
app.register_blueprint(berries_endpoint)

CORS(app, resources={r"/*": {"origins": '*'}})

if __name__ == '__main__':
    port = int(os.getenv('APP_PORT', 5000))
    app.run(debug=bool(os.getenv('FLASK_DEBUG')), host='0.0.0.0', port=port)