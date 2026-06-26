from fastapi import FastAPI
from .routes import api, auth

app = FastAPI()

# Include the API and auth routes
app.include_router(api.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to RouteIQ!"}
