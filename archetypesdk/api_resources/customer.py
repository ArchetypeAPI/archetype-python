from __future__ import absolute_import, division, print_function

from archetypesdk.api_resources.api_resource import (
    ListableAPIResource,
    UpdateableAPIResource,
    RetrievableAPIResource,
)
from archetypesdk.api_requestor import APIRequestor
from archetypesdk.enums import Method


class Customer(ListableAPIResource, RetrievableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "user"

    @classmethod
    def Retrieve(self, custom_uid: str, version: int = 1):
        return super().Retrieve(id=custom_uid, version=version)

    @classmethod
    def All(cls, version: int = 1, **params):
        
        return super().All(version=version, **params)

    @classmethod
    def Update(self, custom_uid: str, version: int = 1, **params):
        return super().Update(id=custom_uid, version=version, **params)

    @classmethod
    def CreateCheckoutSession(self, custom_uid: str, product_id: str, version: int = 1):
        path = f"/api/v{version}/{self.OBJECT_NAME}/{custom_uid}/checkout-session/{product_id}"
        api_requestor = APIRequestor()
        checkout_session = api_requestor.create_request(
            request_method=Method.POST,
            path=path,
            object=self.OBJECT_NAME,
            intent="Create Checkout Session",
        )
        return checkout_session

    @classmethod
    def ResetAPIKey(self, custom_uid: str, version: int = 1, **params):
        path = f"/api/v{version}/{self.OBJECT_NAME}/{custom_uid}/reset-api-key"
        
        customer_data = api_requestor.create_request(
            request_method=Method.POST,
            path=path,
            object=self.OBJECT_NAME,
            intent="Reset API Key",
        )
        return customer_data

    @classmethod
    def CreateSandboxSubscription(
        self, custom_uid: str, product_id: str, version: int = 1, **params
    ):
        path = (
            f"/api/v{version}/{self.OBJECT_NAME}/{custom_uid}/create-promo/{product_id}"
        )
        api_requestor = APIRequestor()
        sandbox_subscription = api_requestor.create_request(
            request_method=Method.POST,
            path=path,
            object=self.OBJECT_NAME,
            data=params,
            intent="Create Sandbox Subscription",
        )
        return sandbox_subscription

    @classmethod
    def CancelSubscription(self, custom_uid: str, version: int = 1):
        path = f"/api/v{version}/{self.OBJECT_NAME}/{custom_uid}/cancel-subscription"
        api_requestor = APIRequestor()
        customer_data = api_requestor.create_request(
            request_method=Method.POST,
            path=path,
            object=self.OBJECT_NAME,
            intent="Cancel Subscription",
        )
        return customer_data

    @classmethod
    def CreatePaymentLink(
        self, custom_uid: str, product_id: str, version: int = 1, **params
    ):
        path = (
            f"/api/v{version}/{self.OBJECT_NAME}/{custom_uid}/payment-link/{product_id}"
        )
        api_requestor = APIRequestor()
        payment_link_data = api_requestor.create_request(
            request_method=Method.POST,
            path=path,
            object=self.OBJECT_NAME,
            data=params,
            intent="Create Payment Link",
        )
        return payment_link_data

    @classmethod
    def Usage():
        pass

    @classmethod
    def Invoices():
        pass
