from repositories.sources.context import ContextData
from repositories.sources.sync_method import SyncMethod
from typing import List


def fetch_data_from_berries_data_source():
    context = ContextData(SyncMethod())
    data = context.fetch_data()
    return data
    # return _format_data_from_berries_endpoint(data)


def _format_data_from_berries_endpoint(data):
    pass


