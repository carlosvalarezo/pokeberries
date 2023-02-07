import abc
from typing import Any


class FetchDataMethod(abc.ABC):
    @abc.abstractmethod
    def fetch_data(self, endpoints=[]) -> Any:
        raise NotImplementedError