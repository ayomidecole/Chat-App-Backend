from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.send_messages import router as send_messages_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(send_messages_router)