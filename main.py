from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from driving.api_rest.router import add_routers
from driving.api_rest.containers import add_containers

app = FastAPI()
origins = [
    "http://localhost:3000",
    "https://tickets.rudo.es"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
add_routers(app)
add_containers(app)
