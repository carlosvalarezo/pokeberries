import os

from flask import Flask
from routes.health import health_endpoint
from routes.berries import berries_endpoint
from middleware.berries import fetch_data_from_berries_data_source

app = Flask(__name__)
app.before_request_funcs = {'berries': [fetch_data_from_berries_data_source]}
app.register_blueprint(health_endpoint)
app.register_blueprint(berries_endpoint)

if __name__ == '__main__':
    port = int(os.getenv('APP_PORT', 5000))
    app.run(debug=bool(os.getenv('FLASK_DEBUG')), host='0.0.0.0', port=port)