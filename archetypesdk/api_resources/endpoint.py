from __future__ import absolute_import, division, print_function

from archetypesdk.api_resources.api_resource import (
    CreatableAPIResource,
    RetrievableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    DeletableAPIResource,
)


class Endpoint(
    CreatableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    DeletableAPIResource,
    RetrievableAPIResource,
):
    OBJECT_NAME = "endpoint"

    @classmethod
    def Retrieve(cls, endpoint_id: str, version: int = 1):
        return super().Retrieve(id=endpoint_id, version=version)

    @classmethod
    def All(cls, version: int = 1, **params):
        return super().All(version=version, **params)

    @classmethod
    def Create(cls, version: int = 1, **params):
        return super().Create(version=version, **params)

    @classmethod
    def Update(self, endpoint_id: str, version: int = 1, **params):
        return super().Update(id=endpoint_id, version=version, **params)

    @classmethod
    def Delete(self, endpoint_id: str, version: int = 1, **params):
        return super().Delete(id=endpoint_id, version=version, **params)
