from .client import KaspiClient

client = KaspiClient()

async def list_orders(page: int = 1, page_size: int = 20):
    return await client.get("/orders", params={"page": page, "pageSize": page_size})

async def get_order(order_id: str):
    return await client.get(f"/orders/{order_id}")

async def accept_order(order_id: str):
    return await client.post(f"/orders/{order_id}/accept", json={})

async def cancel_order(order_id: str, reason: str):
    return await client.post(f"/orders/{order_id}/cancel", json={"reason": reason})
