
from typing import Any
from .data_method import FetchDataMethod


class ContextData():

    def __init__(self,
                 fetch_data_method: FetchDataMethod) -> None:
        
        self._fetch_data_method = fetch_data_method

    @property
    def fetch_data_method(self) -> FetchDataMethod:
        return self._fetch_data_method

    @fetch_data_method.setter
    def fetch_data_method(self,
                          fetch_data_method: FetchDataMethod) -> None:
        """This setter provides a way to change the source of data at runtime."""
        self._fetch_data_method = fetch_data_method

    def fetch_data(self, endpoints=[]) -> Any:
        return self.fetch_data_method.fetch_data(endpoints=endpoints)
