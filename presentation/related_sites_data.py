from typing import Optional
from pydantic import BaseModel

class RelatedSitesData(BaseModel):
    user_site_primary_uuid: str
    user_site_secondary_uuid: str
    relation_description: str