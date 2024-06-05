from domain.repositories.management_repository import ManagementRepository
from infrastructure.datasource.management_data_source import ManagementDataSource
from infrastructure.dtos.user_style_sheet import UserStyleSheet
from infrastructure.dtos.user_site import UserSite
from infrastructure.dtos.user_site_route import UserSiteRoute
from infrastructure.dtos.user_site_route_scrap import UserSiteRouteScrap
from infrastructure.dtos.related_sites import RelatedSites
from infrastructure.dtos.external_link import ExternalLink
from presentation.external_link_data import ExternalLinkData
from presentation.related_sites_data import RelatedSitesData
from presentation.create_site_route_data import CreateSiteRouteData
from presentation.user_site_scrap_data import UserSiteScrapDataBody

class ManagementRepositoryImpl(ManagementRepository):

    def __init__(self, managementDataSource: ManagementDataSource) -> None:
        self.managementDataSource = managementDataSource


    async def create_site_route(self, content: CreateSiteRouteData) -> object:
        return await self.managementDataSource.create_site_route(UserSiteRoute.from_entity(content, None))
    
    async def create_user_site(self, content: UserSite) -> object:
        return await self.managementDataSource.create_user_site(content)
    
    async def list_routes(self, user_site_uuid: str) -> object:
        return await self.managementDataSource.list_routes(user_site_uuid)
    
    async def list_sites(self, user_uuid: str) -> list[object]:
        return await self.managementDataSource.list_sites(user_uuid)
   
    async def list_chat_by_site(self, user_site_uuid: str) -> object:
        return await self.managementDataSource.list_chat_by_site(user_site_uuid)
    
    async def create_api_key(self, user_uuid: str) ->  object:
        return await self.managementDataSource.create_api_key(user_uuid)
    
    async def list_api_keys(self, user_uuid: str) -> object:
        return await self.managementDataSource.list_api_keys(user_uuid)
    
    async def scrap_user_site_route(self, content: UserSiteScrapDataBody) -> object:
        return await self.managementDataSource.scrap_user_site_route(content)
    
    async def list_scrap_by_user_site_route(self, user_site_route_uuid: str) -> object:
        return await self.managementDataSource.list_scrap_by_user_site_route(user_site_route_uuid)
    
    async def get_user_site_route_uuid_by_url(self, url: str) -> object:
        return await self.managementDataSource.get_user_site_route_uuid_by_url(url)
    
    async def delete_site_route(self, uuid: str) -> None:
        await self.managementDataSource.delete_site_route(uuid)

    async def delete_site_route_scrap(self, uuid: str) -> None:
        await self.managementDataSource.delete_site_route_scrap(uuid)

    async def create_user_style_sheet(self, user_style_sheet: UserStyleSheet) -> object:
        return await self.managementDataSource.create_user_style_sheet(user_style_sheet)
    
    async def list_user_style_sheets(self, user_uuid: str) -> object:
        return await self.managementDataSource.list_user_style_sheets(user_uuid)
    
    async def delete_style_sheet(self, uuid: str) -> None:
        return await self.managementDataSource.delete_style_sheet(uuid)
    
    async def update_site(self, user_site: UserSite) -> object:
        return await self.managementDataSource.update_site(user_site)
    
    async def update_site_route(self, user_site_route: UserSiteRoute) -> object:
        return await self.managementDataSource.update_site_route(user_site_route)
    
    async def update_site_route_scrap(self, user_site_route_scrap: UserSiteRouteScrap) -> object:
        return await self.managementDataSource.update_site_route_scrap(user_site_route_scrap)
    
    async def update_site_style_sheet(self, user_site_style_sheet: UserStyleSheet) -> object:
        return await self.managementDataSource.update_site_style_sheet(user_site_style_sheet)
    
    async def create_site_relation(self, content: RelatedSitesData) -> object:
        return await self.managementDataSource.create_site_relation(RelatedSites.fromEntity(
                uuid_data=None,
                related_site_data=content
            ))
    
    async def list_site_relations(self, site_uuid: str) -> object:
        return await self.managementDataSource.list_site_relations(site_uuid)
    
    async def delete_site_relation(self, relation_uuid: str) -> None:
        return await self.managementDataSource.delete_site_relation(relation_uuid)
    
    async def create_external_link(self, content: ExternalLinkData) -> object:
        return await self.managementDataSource.create_external_link(
            ExternalLink.fromEntity(
                uuid=None, 
                external_link_data=content
            ))
    
    async def list_external_links_by_site_uuid(self, site_uuid: str) -> object:
        return await self.managementDataSource.list_external_links_by_site_uuid(site_uuid)
    
    async def delete_external_link(self, external_link_uuid: str) -> None:
        return await self.managementDataSource.delete_external_link(external_link_uuid)