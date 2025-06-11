from .client import KaspiClient

client = KaspiClient()

async def list_products(page: int = 1, page_size: int = 50):
    return await client.get("/products", params={"page": page, "pageSize": page_size})

async def get_product(sku: str):
    return await client.get(f"/products/{sku}")

async def create_product(data: dict):
    return await client.post("/products", json=data)

async def update_product(sku: str, data: dict):
    return await client.put(f"/products/{sku}", json=data)

async def delete_product(sku: str):
    return await client.delete(f"/products/{sku}")
