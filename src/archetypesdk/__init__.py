from __future__ import absolute_import, division, print_function

import os

# Archetype Python
# API docs at http://docs.archetype.dev
# Authors:
# Behailu Tekletsadik : behailu@archetype.dev

# Configuration variables

secret_key = os.environ.get("ARCHETYPE_SECRET_KEY")
app_id = os.environ.get("ARCHETYPE_APP_ID")
prod_api_base = os.environ.get("ARCHETYPE_API_PROD_URL", "https://api.archetype.dev")
upload_api_base = "https://files.archetype.dev"
auth_version = 4
record_auth_requests = True
api_version = None
verify_ssl_certs = True
proxy = None
default_http_client = None
app_info = None
enable_telemetry = True
max_network_retries = 0

# Set to either 'debug' or 'info', controls console logging
log = None

from archetypesdk.api_resources import *


def set_app_info(name, partner_id=None, url=None, version=None):
    global app_info
    app_info = {
        "name": name,
        "partner_id": partner_id,
        "url": url,
        "version": version,
    }
