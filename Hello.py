import streamlit as st
import requests

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "your_redirect_uri"

# ORCID OAuth URLs
AUTH_URL = "https://orcid.org/oauth/authorize"
TOKEN_URL = "https://orcid.org/oauth/token"

# Streamlit app
st.title("ORCID Authentication Example")

# Authentication button
if st.button("Login with ORCID"):
    # Redirect user to ORCID for authentication
    auth_params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'scope': '/authenticate',
        'redirect_uri': REDIRECT_URI
    }
    auth_url = f"{AUTH_URL}?{'&'.join([f'{key}={val}' for key, val in auth_params.items()])}"
    st.experimental_set_query_params(code="")  # Clear previous code if any
    st.markdown(f"[Click here to authenticate]({auth_url})")

# Handle authentication callback
code = st.experimental_get_query_params().get("code", None)
if code:
    # Exchange code for access token
    token_data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    response = requests.post(TOKEN_URL, data=token_data)
    access_token = response.json().get('access_token', None)

    # Use access_token for further API requests

