import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from rest_introduction_app.api.challenges.challenge_primer import challenge_primer

app = FastAPI(
    title='Challenge primer',
    description="Application to show how Capture The Flag challenges work",
    version="0.1",
    docs_url="/",
    redoc_url=None
)

app.include_router(router=challenge_primer.router,
                   tags=[challenge_primer.challenge_tag])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=9012)
