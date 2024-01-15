from fastapi import FastAPI

from starlette.staticfiles import StaticFiles

from blueprints.explain import explain_router
from blueprints.landing import landing_router

app = FastAPI()

app.include_router(explain_router)
app.include_router(landing_router)
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
