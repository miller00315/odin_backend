from typing import Optional
from pydantic import BaseModel

class UserStyleSheetData(BaseModel):
    style_sheet_url: Optional[str] = None
    style_sheet_name: str
    style_sheet_description: Optional[str] = None
    style_sheet_content: Optional[str] = None
    user_site_uuid: str