from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import structure

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


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


@app.get("/")
async def main():
    return {"message": "Backend works"}


# app.include_router(
#     auth.router,
#     prefix="/auth",
#     tags=["Auth"],
# )

app.include_router(
    structure.router,
    prefix="/report",
    tags=["structures"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "no structures"}},
)
