import os
import requests
from .data_method import FetchDataMethod
from dataclasses import dataclass
from exceptions.endpoint_not_found import EndpointNotFoundException
from http import HTTPStatus
from typing import List, Any

LIMIT=os.getenv('BERRY_LIMIT', 20)
OFFSET=os.getenv('BERRY_OFFSET', 0)


@dataclass
class BerriesEndpoint:
    name: str
    url: str


class SyncMethod(FetchDataMethod):
    def fetch_data(self, endpoints=[]) -> List[BerriesEndpoint]:
        pokemon_uri = os.getenv('POKEMON_URI', None)
        if not pokemon_uri:
            raise EndpointNotFoundException('Missing POKEMON_URI',
                                            HTTPStatus.NOT_FOUND)
        url = f'{pokemon_uri}?offset={OFFSET}&limit={LIMIT}'
        while url:
            gen_response = list(self._fetch_data(url))
            url = gen_response[0].get('next')
            results = gen_response[0].get('results')
            endpoints.extend([BerriesEndpoint(result.get('name'),
                                              result.get('url')) for result in results])
        return endpoints


    def _fetch_data(self, uri) -> Any:
        yield requests.get(uri, headers={}).json()
