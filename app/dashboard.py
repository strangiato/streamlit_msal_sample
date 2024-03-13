import streamlit as st

from msal_streamlit_authentication import msal_authentication


value = msal_authentication(
    auth={
        "clientId": "95d75130-08e9-4d56-935f-1cc063a81177",
        "authority": "https://login.microsoftonline.com/8a9d6f8c-3d41-469e-ab2f-16738a0bb216",
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
