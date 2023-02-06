import os
from .data_method import FetchDataMethod
from typing import List

# LIMIT=20
# OFFSET=0

class AsyncMethod(FetchDataMethod):
    def fetch_data(self) -> List:
        pass
        # pokemon_uri = os.getenv('POKEMON_URI', '')
        # self.uri = f'{pokemon_uri}?offset={OFFSET}&limit={LIMIT}'
    
    # async def get_berries(self):
    #     async with aiohttp.ClientSession() as session:
    #         response = await session.get(self.uri, ssl=False)
    # asyncio.run(get_berries())
        