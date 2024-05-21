from typing import Optional
from pydantic import BaseModel

class UserSiteScrapData(BaseModel):
    css_class: Optional[str] = None
    item_id: Optional[str] = None
    tag: str
    scrap_description: str
    function_on_the_page: str
    parent_uuid: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    user_site_route_uuid: str

class UserSiteScrapDataBody(BaseModel):
    user_site_route_uuid: str
    content: list[UserSiteScrapData]
