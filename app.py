from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from auth.jwt_bearer import JWTBearer
from config.config import Settings, initiate_database
from routes.admin import router as AdminRouter
from routes.pokemon import router as PokemonRouter
from routes.load import router as LoadRouter

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load Mongo DB
    await initiate_database()
    yield
    # todo clean mongodb


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[Settings().ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

token_listener = JWTBearer()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}

app.include_router(PokemonRouter,tags=["Pokemon"],prefix="/pokemon")
app.include_router(LoadRouter,tags=["Load"],prefix="/load",dependencies=[Depends(token_listener)],)
app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
