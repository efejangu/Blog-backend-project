# set up fastapi with uvicorn
from fastapi import FastAPI
from router import user,auth,post, likes
import uvicorn
import models
from db_engine import engine
from starlette.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination




app = FastAPI()
add_pagination(app)

origins = [ "http://127.0.0.1:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT"],
    allow_headers=["Content-Type"],
)


app.include_router(user.router)
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(likes.router)
models.Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

