from fastapi import FastAPI

from app.article.api.routes import router as article_routes
from app.user.api.routes import router as user_routes

app = FastAPI()

routes = [
    user_routes,
    article_routes,
]

[app.include_router(router) for router in routes]
