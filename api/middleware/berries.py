from repositories.sources.context import ContextData
from repositories.sources.sync_method import SyncMethod
from repositories.sources.async_method import AsyncMethod
from typing import Any


def fetch_data_from_berries_data_source() -> Any:
    sync_context = ContextData(SyncMethod())
    berry_endpoints = sync_context.fetch_data()
    async_context = ContextData(AsyncMethod())
    return async_context.fetch_data(endpoints=berry_endpoints)
