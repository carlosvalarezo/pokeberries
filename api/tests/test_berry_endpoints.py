import pytest
import requests
from api.repositories.sources.context import ContextData
from api.repositories.sources.sync_method import SyncMethod
from faker import Faker

fake = Faker()

def mock_valid_name():
    return fake.name()

def mock_valid_uri():
    return fake.uri()

name = mock_valid_name()
uri = mock_valid_uri()

class MockResponse:
    @staticmethod
    def json():
        response = {"next": None,
                    "results": [{'name': name,
                                 'uri': uri}]}
        return response
        

@pytest.fixture
def mock_get_request(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


@pytest.fixture
def mock_not_get_request(monkeypatch):
    monkeypatch.delattr(requests, "get", raising=True)


@pytest.fixture
def mock_pokemon_endpoint(monkeypatch):
    monkeypatch.setenv("POKEMON_URI", fake.uri())


def test_request_berries_data(mock_get_request,
                              mock_pokemon_endpoint):
    sync_context = ContextData(SyncMethod())
    berry_endpoints = sync_context.fetch_data()
    assert name == berry_endpoints[0].name
    assert None == berry_endpoints[0].url
