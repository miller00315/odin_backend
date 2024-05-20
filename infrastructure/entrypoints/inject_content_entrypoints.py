from fastapi import APIRouter, Depends, Body

router = APIRouter()

@router.get("/get_inject_content")
async def get_inject_content(
    user_site_uuid: str
):
    print(user_site_uuid)

    return {"data": "console.log(\"Estes serão scripst a serem injetados.\")"}