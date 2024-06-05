from presentation.related_sites_data import RelatedSitesData
from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt
import uuid

class RelatedSites(SQLModel, table=True):
    __tablename__ = "related_sites"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    user_site_primary_uuid: str
    user_site_secondary_uuid: str
    relation_description: str
    created_at: Optional[datetime] = Field(default=datetime.now(dt.UTC))

    def __init__(
                self,
                uuid: str,
                user_site_primary_uuid: str,
                user_site_secondary_uuid: str,
                relation_description: str
            ):
        self.uuid = uuid
        self.user_site_primary_uuid = user_site_primary_uuid
        self.user_site_secondary_uuid = user_site_secondary_uuid
        self.relation_description = relation_description

    @staticmethod
    def fromEntity(
            uuid_data: Optional[str],
            related_site_data: RelatedSitesData
        ):
        
        return RelatedSites(
            uuid = uuid_data if uuid_data else uuid.uuid4(),
            user_site_primary_uuid = related_site_data.user_site_primary_uuid,
            user_site_secondary_uuid = related_site_data.user_site_secondary_uuid,
            relation_description = related_site_data.relation_description
        )