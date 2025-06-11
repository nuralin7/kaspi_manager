import os
from typing import Any, Dict
import httpx
from dotenv import load_dotenv

load_dotenv()

class KaspiClient:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.token = os.getenv("KASPI_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        self.client = httpx.AsyncClient(base_url=self.base_url, headers=self.headers)

    async def get(self, path: str, params: Dict[str, Any] = None):
        resp = await self.client.get(path, params=params)
        resp.raise_for_status()
        return resp.json()

    async def post(self, path: str, json: Dict[str, Any]):
        resp = await self.client.post(path, json=json)
        resp.raise_for_status()
        return resp.json()

    async def put(self, path: str, json: Dict[str, Any]):
        resp = await self.client.put(path, json=json)
        resp.raise_for_status()
        return resp.json()

    async def delete(self, path: str):
        resp = await self.client.delete(path)
        resp.raise_for_status()
        return resp.json()
