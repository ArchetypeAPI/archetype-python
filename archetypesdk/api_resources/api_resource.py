from __future__ import absolute_import, division, print_function
from typing import List

from archetypesdk.api_requestor import APIRequestor
from archetypesdk.enums import Method

api_requestor = APIRequestor()
class CreatableAPIResource:
    @classmethod
    def Create(cls, version: int = 1, **params):
        object_name = cls.OBJECT_NAME
        path = f"/api/v{version}/create-{object_name}"
        api_resource = api_requestor.create_request(
            request_method=Method.POST,
            path=path,
            object=object_name,
            data=params,
            intent=f"Create {object_name}"
        )

        return api_resource


class RetrievableAPIResource:
    @classmethod
    def Retrieve(
        cls,
        id: str,
        version: int = 1,
    ):
        object_name = cls.OBJECT_NAME
        path = f"/api/v{version}/{object_name}/{id}"
        api_resource = api_requestor.create_request(
            request_method=Method.GET,
            path=path,
            object=object_name,
            intent=f"Retrieve {object_name}: {id}",
        )
        return api_resource


class ListableAPIResource:
    @classmethod
    def All(
        cls,
        version: int = 1,
    ):
        path = f"/api/v{version}/{cls.OBJECT_NAME}s"
        api_requestor = APIRequestor()
        billable_metrics = api_requestor.create_request(
            request_method=Method.GET,
            path=path,
            object=cls.OBJECT_NAME,
            intent=f"Retrieve List of {cls.OBJECT_NAME}",
        )

        return billable_metrics


class UpdateableAPIResource:
    @classmethod
    def Update(cls, id: str, version: int = 1, **params):
        object_name = cls.OBJECT_NAME
        path = f"/api/v{version}/{object_name}/{id}"
        api_requestor = APIRequestor()
        api_resource = api_requestor.create_request(
            request_method=Method.PUT,
            path=path,
            object=object_name,
            data=params,
            intent=f"Update {object_name}: {id}",
        )
        return api_resource


class DeletableAPIResource:
    @classmethod
    def Delete(cls, id: str, version: int = 1, **params):
        object_name = cls.OBJECT_NAME
        path = f"/api/v{version}/{object_name}/{id}"
        api_requestor = APIRequestor()
        api_resource = api_requestor.create_request(
            request_method=Method.DELETE,
            path=path,
            object=object_name,
            data=params,
            intent=f"Delete {object_name} {id}",
        )
        return api_resource
