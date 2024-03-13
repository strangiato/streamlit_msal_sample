import os

import streamlit as st

from msal_streamlit_authentication import msal_authentication

clientID = os.environ["CLIENTID"]
tenantID = os.environ["TENANTID"]


value = msal_authentication(
    auth={
        "clientId": clientID,
        "authority": f"https://login.microsoftonline.com/{tenantID}",
        "redirectUri": "/",
        "postLogoutRedirectUri": "/"
    },
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    },
    # login_request={
    #     "scopes": ["aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee/.default"]
    # },
    key=1)
st.write("Received", value)
