from flask import Blueprint, jsonify
from middleware.berries import fetch_data_from_berries_data_source
from service.berries import parse_raw_data_to_berries
from functools import wraps


class MyBlueprint(Blueprint):
    berries_data = []
    def set_data(self, data):
        self.berries_data = parse_raw_data_to_berries(data=data)

berries_endpoint = MyBlueprint('berries', __name__)

@berries_endpoint.before_request
def fetch_data():
    data = fetch_data_from_berries_data_source()
    berries_endpoint.set_data(data=data)

@berries_endpoint.route('/allBerryStats')
def berries_stats():
    return jsonify({'the_result': 'the_stats'})

