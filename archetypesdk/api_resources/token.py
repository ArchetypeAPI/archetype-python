from __future__ import absolute_import, division, print_function

from archetypesdk.api_resources.api_resource import (
    CreatableAPIResource
)

class Token(
    CreatableAPIResource
):
    OBJECT_NAME = "token"


    @classmethod
    def Create(cls, custom_uid: str, version: int = 1, **params):
        params["custom_uid"] = custom_uid
        return super().Create(version=version, **params)
