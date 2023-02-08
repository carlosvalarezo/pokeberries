from service.statistics_operations import get_min_growth_time, get_max_growth_time
from service.statistics_operations import get_mean_growth_time, get_median_growth_time
from service.statistics_operations import get_variance_growth_time, get_frecuency_growth_time
from service.statistics_operations import get_names_of_the_berries

def mock_list_of_berries():
    return[{'name': 'cheri-berry', 'growth_time': 3},
           {'name': 'oran-berry', 'growth_time': 4},
           {'name': 'lum-berry', 'growth_time': 12},
           {'name': 'sitrus-berry', 'growth_time': 8},
           {'name': 'figy-berry', 'growth_time': 5}]


def test_returns_the_min_number_and_berries_name_given_a_list():
    list_of_berries = mock_list_of_berries()
    min_value = get_min_growth_time(list_of_berries)
    assert min_value == {'name': 'cheri-berry', 'growth_time': 3}


def test_returns_the_max_number_and_berries_name_given_a_list():
    list_of_berries = mock_list_of_berries()
    max_value = get_max_growth_time(list_of_berries)
    assert max_value == {'name': 'lum-berry', 'growth_time': 12}


def test_returns_the_median_number_given_a_list():
    list_of_berries = mock_list_of_berries()
    _median = get_median_growth_time(list_of_berries)
    assert _median == 5


def test_returns_the_mean_number_given_a_list():
    list_of_berries = mock_list_of_berries()
    _mean = get_mean_growth_time(list_of_berries)
    assert _mean == 6.4


def test_returns_the_variance_number_given_a_list():
    list_of_berries = mock_list_of_berries()
    _variance = get_variance_growth_time(list_of_berries)
    assert _variance == 13.3

    
def test_returns_the_frecuency_of_the_elements_of_a_list():
    list_of_berries = mock_list_of_berries()
    frecuency = get_frecuency_growth_time(list_of_berries)
    assert frecuency == {3: 1, 4: 1, 12: 1, 8: 1, 5: 1}

    
def test_returns_the_names_of_the_elements_of_a_list():
    list_of_berries = mock_list_of_berries()
    names = get_names_of_the_berries(list_of_berries)
    assert names == ['cheri-berry', 'oran-berry', 'lum-berry',  'sitrus-berry', 'figy-berry']