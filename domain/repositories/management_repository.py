from abc import ABC, abstractmethod

from infrastructure.dtos.user_site import UserSite
from infrastructure.dtos.user_site_route import UserSiteRoute
from infrastructure.dtos.user_style_sheet import UserStyleSheet
from infrastructure.dtos.user_site_route_scrap import UserSiteRouteScrap
from presentation.related_sites_data import RelatedSitesData
from presentation.user_site_scrap_data import UserSiteScrapDataBody
from presentation.create_site_route_data import CreateSiteRouteData

class ManagementRepository(ABC):
    @abstractmethod
    async def create_user_site(self, content: UserSite) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def create_site_route(self, ucontent: CreateSiteRouteData) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def list_sites(self, user_uuid: str) -> list[object]:
        raise NotImplementedError()
    
    @abstractmethod
    async def create_site_relation(self, content: RelatedSitesData) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def list_site_relations(self, site_uuid: str) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def delete_site_relation(self, relation_uuid: str) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def list_routes(self, user_site_uuid: str) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def list_chat_by_site(self, user_site_uuid: str) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def create_api_key(self, user_uuid: str) ->  object:
        raise NotImplementedError()
    
    @abstractmethod
    async def list_api_keys(self, user_uuid: str) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def scrap_user_site_route(self, content: UserSiteScrapDataBody) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def list_scrap_by_user_site_route (self, user_site_route_uuid: str) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def get_user_site_route_uuid_by_url(self, url: str) -> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def delete_site_route(self, uuid: str) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def delete_site_route_scrap(self, uuid: str) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def delete_style_sheet(self, uuid: str) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def update_site(self, user_site: UserSite)-> object:
        raise NotImplementedError()

    @abstractmethod
    async def update_site_route(self, user_site_route: UserSiteRoute)-> object:
        raise NotImplementedError()
    
    @abstractmethod
    async def update_site_style_sheet(self, user_site_style_sheet: UserStyleSheet)-> object:
        raise NotImplementedError()

    @abstractmethod
    async def update_site_route_scrap(self, user_site_route_scrap: UserSiteRouteScrap)-> object:
        raise NotImplementedError()