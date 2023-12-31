from fastapi import FastAPI
from .database import engine
from .database import Base
from .routers import vote, post, user, auth
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


# Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def login():
    return {"message": "Hello!!"}
