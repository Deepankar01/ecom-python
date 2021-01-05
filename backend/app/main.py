import graphene
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import database
from starlette.graphql import GraphQLApp
from .graphql import schema

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

app.add_route("/gq", GraphQLApp(schema=schema))
