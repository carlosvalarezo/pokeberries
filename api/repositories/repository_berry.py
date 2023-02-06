import os
from api.repositories.sources.data_method import AbstractRepository
from api.repositories.sources.async_method import APIMethod
from sources.context import ContextData


class APIRepositoryBerry(AbstractRepository):
    def get(self):
        context = ContextData(APIMethod)
        return context.format_data()


