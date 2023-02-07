from flask import Blueprint, jsonify
from middleware.berries import fetch_data_from_berries_data_source

berries_endpoint = Blueprint('berries', __name__)

data = []

@berries_endpoint.before_request
def fetch_data():
    data = fetch_data_from_berries_data_source()

@berries_endpoint.route('/allBerryStats')
def berries_stats():
    return jsonify({'the_result': 'the_stats'})

