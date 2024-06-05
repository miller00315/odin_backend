from presentation.external_link_data import ExternalLinkData
from sqlmodel import Field, SQLModel # type: ignore
from typing import Optional
from datetime import datetime
import datetime as dt
import uuid

class ExternalLink(SQLModel, table=True):
    __tablename__ = "external_link"

    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    link_url: str
    user_site_uuid: str
    link_description: str
    created_at: Optional[datetime] = Field(default=datetime.now(dt.UTC))

    def __init__(
            self,
            uuid: str,
            user_site_uuid: str,
            link_description: str
        ):

        self.uuid = uuid
        self.user_site_uuid = user_site_uuid
        self.link_description = link_description

    @staticmethod
    def fromEntity(
        uuid: Optional[str],
        external_link_data: ExternalLinkData
    ):
        return ExternalLink(
            uuid = uuid if uuid else uuid.uuid4(),
            link_url = external_link_data.link_url,
            user_site_uuid = external_link_data.user_site_uuid,
            link_description = external_link_data.link_description
        )
