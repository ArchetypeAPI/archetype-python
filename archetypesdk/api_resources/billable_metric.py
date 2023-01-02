from __future__ import absolute_import, division, print_function

from archetypesdk.enums import Method
from archetypesdk.api_resources.api_resource import (
    CreatableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    RetrievableAPIResource,
)
from archetypesdk.api_requestor import APIRequestor
import asyncio
class BillableMetric(
    CreatableAPIResource,
    RetrievableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "billable-metric"

    @classmethod
    def Retrieve(cls, billable_metric_id: str, version: int = 1):
        return super().Retrieve(id=billable_metric_id, version=version)

    @classmethod
    def All(cls, version: int = 1, **params):
        return super().All(version=version, **params)

    @classmethod
    def Create(cls, version: int = 1, **params):
        return super().Create(version=version, **params)

    @classmethod
    def Update(self, billable_metric_id: str, version: int = 1, **params):
        return super().Update(id=billable_metric_id, version=version, **params)

    @classmethod
    def LogUsage(self, custom_uid: str, billable_metric_id: str, used_amount: float):
        data = {
            "custom_uid": custom_uid,
            "billable_metric_id": billable_metric_id,
            "used_amount": used_amount
        }
        api_requestor = APIRequestor()
        return api_requestor.create_request(
            Method.POST,
            '/sdk/v4/log-billable-metric-usage',
            data=data
        )
