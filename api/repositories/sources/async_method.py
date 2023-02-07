import asyncio
import aiohttp
from .data_method import FetchDataMethod

from typing import Dict, List, Any


class AsyncMethod(FetchDataMethod):
    def fetch_data(self, endpoints) -> Any:
        return asyncio.run(self._fetch_data(endpoints=endpoints))

    def get_sessions(self, session: aiohttp.ClientSession, endpoints) -> List[aiohttp.ClientSession]:
        return [asyncio.ensure_future(self.get_berry(session, endpoint.url)) for endpoint in endpoints]

    async def _fetch_data(self, endpoints: List) -> Any:
        async with aiohttp.ClientSession() as session:
            sessions = self.get_sessions(session=session, endpoints=endpoints)
            return await asyncio.gather(*sessions)
    
    async def get_berry(self, session, url) -> Dict:
        async with session.get(url) as resp:
            return await resp.json()
