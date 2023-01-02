from __future__ import absolute_import, division, print_function

from archetypesdk.api_resources.api_resource import (
    CreatableAPIResource
)

class Token(
    CreatableAPIResource
):
    OBJECT_NAME = "token"


    @classmethod
    def Create(cls, custom_id: str, version: int = 1, **params):
        params["custom_id"] = custom_id
        return super().Create(version=version, **params)
