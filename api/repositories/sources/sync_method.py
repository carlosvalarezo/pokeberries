import os
import requests
from .data_method import FetchDataMethod
from dataclasses import dataclass
from typing import Dict, List

LIMIT=20
OFFSET=0


@dataclass
class BerriesEndpoint:
    name: str
    url: str



class SyncMethod(FetchDataMethod):
    def fetch_data(self) -> List[BerriesEndpoint]:
        results = []
        pokemon_uri = os.getenv('POKEMON_URI', '')
        uri = f'{pokemon_uri}?offset={OFFSET}&limit={LIMIT}'
        while uri:
            gen_response = list(self._fetch_data(uri))
            uri = gen_response[0].get('next')
            _results = gen_response[0].get('results')
            results.extend([BerriesEndpoint(result.get('name'), result.get('url')) for result in _results])
        return results

    def _fetch_data(self, uri):
        yield requests.get(uri, headers={}).json()
