from fastapi import FastAPI, HTTPException
from kaspi_api import orders, products

app = FastAPI(title="Kaspi Shop Manager")

@app.get("/orders")
async def api_list_orders(page: int = 1):
    try:
        return await orders.list_orders(page)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/orders/{order_id}/accept")
async def api_accept_order(order_id: str):
    try:
        return await orders.accept_order(order_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/products")
async def api_list_products(page: int = 1):
    try:
        return await products.list_products(page)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
