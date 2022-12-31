# Archetype Python Library

The Archetype Python library provides convenient access to the Archetype API from applications written in Python. It includes a pre-defined set of classes for API resources that initialize themselves dynamically from API responses which makes it compatible with a wide range of versions of the Archetype API.

The SDK has everything you need to build and manage API subscriptions, usage-based billing, tracking metered usage, issue volume based discounts, graduated pricing models and more.

# About Archetype
[Archetype](https://archetype.dev) is the revenue infrastruce that make API monetization quick and painless. It works by integrating powerful, reliable purchase server with cross-platform support. Our open-source framework provides a backend and a wrapper around payment processors like Stripe to save engineers months from having to build custom billing infrastructure for their APIs.

Whether you are building a new API or already have millions of customers, you can use Archetype to:

-   Fetch products, make purchases, and check subscription status with our  [native SDKs](https://docs.archetype.dev/docs/installation).
-   Host add [configure products](https://docs.archetype.dev/docs/products) remotely from our dashboard.
-   Analyze the most important metrics for your app business  [in one place](https://docs.archetype.dev/docs/analytics).
-   See customer transaction histories, chart lifetime value, and  [grant promotional subscriptions](https://docs.archetype.dev/docs/users).

Sign up to [get started](https://app.archetype.dev/signup).

# Documentation



If looking to use our APIs directly, the [API reference](https://docs.archetype.dev/reference/basic) is here.

With Archetype, you can keep track of all your app transactions in one place — whether your customers are charged through iOS, Android, or the web. As the single source of truth for your API business, we make sure your customers' subscription status is always up to date.


# Installation

**[Explore the docs and view the quickstart guide](https://docs.archetype.dev/docs/quickstart-guide)**

You don't need this source code unless you want to modify the package. If you just want to use the package, just run:

```sh
pip install -upgrade archetypesdk
```


## Requirements

Python 3.6+ (PyPy supported)

# Usage


The library needs to be configured with your account's **app_id** and **secret key** which is available in your **[Archetype Dashboard](app.archetype.dev/settings)**. Set `archetype.app_id` and `archetype.secret_key` to their values:

```python
import archetypesdk as archetype

archetype.app_id = "ARCHETYPE_APP_ID"
archetype.secret_key = "ARCHETYPE_SECRET_KEY"

# create customer

customer = archetype.Customer.Create(custom_uid="CUSTOM_UID")

# list customers
customers = archetype.Customer.All()

# print the first customer's email
print(customers[0]["email"])

# retrieve specific Customer
customer = archetype.Customer.Retrieve("CUSTOM_UID")

# print that customer's email
print(customer["email"])

## Track a Metered Usage

archetype.BillableMetric.LogUsage(
    custom_ud="YOUR_CUSTOMER_ID", 
    billable_metric_id="BILLABLE_METRIC_ID", 
    amount=#Float
)


# Authorize a Flask Request with Archetype Middelware

@app.route("/a", methods=["GET", "POST"])
@archetype.Auth
def auth_test_url():
    return jsonify({"response": "success!"}), 200

# Authorize a Django Request with Archetype Middelware

@archetype.Auth
def sensitive_fbv(request, *args, **kwargs):
    return HttpResponse()

# Authorize a FastAPI Request with Archetype Middelware
from archetypesdk.fastapi import authorized

@app.get("/authorize")
async def hello_world(is_authorized = Depends(authorized)):
    return {"response": "Success"}


```

You can leverage the SDK to create and configure billable metrics, products, token management, authorization and more. Check out [the docs](https://docs.archetype.dev/docs/welcome) for more examples and use cases.