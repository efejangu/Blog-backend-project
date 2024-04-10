from fastapi import APIRouter

router = APIRouter(
    prefix="/post",
    tags=["Post"],
)

#replace all the return statements in the functions below with pass statements

async def get_posts():
    pass

@router.get("/posts/{post_id}")
async def get_post(post_id: int):
    pass

@router.post("/posts/")
async def create_post():
    pass
