"""hit the Tidal API"""
import httpx


class Tidal:
    """Tidal API client"""

    def __init__(self, token):
        self.token = token
        self.client = httpx.AsyncClient()

    async def _call(self, endpoint, **params):
        if "token" not in params:
            params["token"] = self.token
        if "countryCode" not in params:
            params["countryCode"] = "CA"
        url = f"https://api.tidalhifi.com/v1/{endpoint}"
        resp = await self.client.get(url, params=params)
        return resp.json()

    async def search(self, query):
        return await self._call("search", query=query)


async def main():
    import os

    tidal = Tidal(token=os.environ["TIDAL_TOKEN"])
    print(await tidal.search(query="herbi"))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())