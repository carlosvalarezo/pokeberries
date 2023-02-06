from flask import Blueprint, jsonify

berries_endpoint = Blueprint('berries', __name__)

@berries_endpoint.route('/allBerryStats')
def berries_stats():
    return jsonify({'the_result': 'the_stats'})

