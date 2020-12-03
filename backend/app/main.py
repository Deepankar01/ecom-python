from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import database
from app.db.database import database
from .routers import products, sellers, user

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# async def get_token_header(x_token: str = Header(...)):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-Token header invalid")


@app.get("/")
async def main():
    return {"message": "Backend works"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# app.include_router(
#     auth.router,
#     prefix="/auth",
#     tags=["Auth"],
# )

app.include_router(
    products.router,
    prefix="/product",
    tags=["products"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "no products"}},
)

app.include_router(
    sellers.router,
    prefix="/seller",
    tags=["sellers"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "no sellers"}},
)
app.include_router(
    user.router,
    prefix="/user",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "no users"}},
)
