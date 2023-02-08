from collections import Counter
from typing import List
from statistics import mean, median, variance

def get_min_growth_time(data: List):
    return min(data, key=lambda x: x.get('growth_time'))

def get_max_growth_time(data: List):
    return max(data, key=lambda x: x.get('growth_time'))

def get_mean_growth_time(data: List):
    return mean([item.get('growth_time') for item in data])

def get_median_growth_time(data: List):
    return median([item.get('growth_time') for item in data])

def get_variance_growth_time(data: List):
    return variance([item.get('growth_time') for item in data])

def get_frecuency_growth_time(data: List):
    return Counter([item.get('growth_time') for item in data])

def get_names_of_the_berries(data: List):
    return [item.get('name') for item in data]


