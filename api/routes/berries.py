from flask import (Blueprint,
                   jsonify,
                   render_template)
from middleware.berries import fetch_data_from_berries_data_source
from service.berries import parse_raw_data_to_berries
from service.statistics_operations import get_min_growth_time, get_max_growth_time
from service.statistics_operations import get_mean_growth_time, get_median_growth_time
from service.statistics_operations import get_variance_growth_time, get_frecuency_growth_time
from service.statistics_operations import get_names_of_the_berries


class MyBlueprint(Blueprint):
    berries_data = []
    def set_data(self, data):
        self.berries_data = parse_raw_data_to_berries(data=data)

berries_endpoint = MyBlueprint('berries', __name__)

@berries_endpoint.before_request
def fetch_data():
    data = fetch_data_from_berries_data_source()
    berries_endpoint.set_data(data=data)

@berries_endpoint.after_request
def add_header(response):
    response.headers['Content-Type'] = 'application/json'
    return response

@berries_endpoint.route('/allBerryStats')
def berries_stats():
    return jsonify({'berries_names': get_names_of_the_berries(berries_endpoint.berries_data),
                    'min_growth_time': get_min_growth_time(berries_endpoint.berries_data),
                    'median_growth_time':  round(get_median_growth_time(berries_endpoint.berries_data), 2),
                    'max_growth_time': get_max_growth_time(berries_endpoint.berries_data),
                    'variance_growth_time': round(get_variance_growth_time(berries_endpoint.berries_data), 2),
                    'mean_growth_time': round(get_mean_growth_time(berries_endpoint.berries_data), 2),
                    'frequency_growth_time': get_frecuency_growth_time((berries_endpoint.berries_data))})


@berries_endpoint.route('/histogram')
def render_histogram():
    return render_template('histogram.html', berries=berries_endpoint.berries_data)
