from flask import Blueprint, jsonify

health_endpoint = Blueprint('api', __name__)


@health_endpoint.route('/health')
def health_check():
    return jsonify({'status': 'up'})

@health_endpoint.after_request
def add_header(response):
    response.headers['Content-Type'] = 'application/json'
    return response