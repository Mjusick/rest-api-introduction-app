import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from rest_introduction_app.api.challenges.challenge_6 import challenge_6

app = FastAPI(
    title='Excursion od Diatlov Pass',
    description="Prepare your backback, you're gonna need it!",
    version="0.1",
    docs_url="/",
    redoc_url=None
)

app.include_router(router=challenge_6.router,
                   tags=[challenge_6.challenge_tag])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=9014)