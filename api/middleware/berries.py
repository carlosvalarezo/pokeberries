from repositories.sources.context import ContextData
from repositories.sources.sync_method import SyncMethod
from dataclasses import dataclass
from typing import List

@dataclass
class BerriesEnpoint:
    next: str
    previous: str
    results: List

def fetch_data_from_berries_data_source():
    context = ContextData(SyncMethod())
    return context.fetch_data()


