from typing import Optional
from pydantic import BaseModel

class ExternalLinkData(BaseModel):
    uuid: Optional[str] = None
    link_url: str
    user_site_uuid: str
    link_description: str