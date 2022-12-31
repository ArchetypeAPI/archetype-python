from __future__ import absolute_import, division, print_function

from archetypesdk.api_resources.api_resource import (
    CreatableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    RetrievableAPIResource,
)


class Product(
    CreatableAPIResource,
    RetrievableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "product"

    @classmethod
    def Retrieve(cls, product_id: str, version: int = 1):
        return super().Retrieve(id=product_id, version=version)

    @classmethod
    def All(cls, version: int = 1, **params):
        return super().All(version=version, **params)

    @classmethod
    def Create(cls, version: int = 1, **params):
        return super().Create(version=version, **params)

    @classmethod
    def Update(self, product_id: str, version: int = 1, **params):
        return super().Update(id=product_id, version=version, **params)
