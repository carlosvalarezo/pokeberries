import os
import requests
from .data_method import FetchDataMethod
from typing import List

LIMIT=20
OFFSET=0


class SyncMethod(FetchDataMethod):
    def fetch_data(self) -> List:
        berries_endpoints = []
        pokemon_uri = os.getenv('POKEMON_URI', '')
        uri = f'{pokemon_uri}?offset={OFFSET}&limit={LIMIT}'
        return requests.get(uri, headers={}).json()
