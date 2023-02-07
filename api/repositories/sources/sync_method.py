import os
import requests
from .data_method import FetchDataMethod
from dataclasses import dataclass
from typing import Dict, List, Any

LIMIT=20
OFFSET=0


@dataclass
class BerriesEndpoint:
    name: str
    url: str


class SyncMethod(FetchDataMethod):
    def fetch_data(self, endpoints=[]) -> List[BerriesEndpoint]:
        pokemon_uri = os.getenv('POKEMON_URI', '')
        uri = f'{pokemon_uri}?offset={OFFSET}&limit={LIMIT}'
        while uri:
            gen_response = list(self._fetch_data(uri))
            uri = gen_response[0].get('next')
            results = gen_response[0].get('results')
            endpoints.extend([BerriesEndpoint(result.get('name'), result.get('url')) for result in results])
        return endpoints

    def _fetch_data(self, uri) -> Any:
        yield requests.get(uri, headers={}).json()
