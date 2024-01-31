from fastapi import APIRouter

router = APIRouter(
    prefix='/articles',
    tags=['article'],
)


@router.get('/')
def get_articles():
    return {
        'articles': [],
    }
