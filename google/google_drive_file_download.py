import io
import json

import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
import requests

def download_file(file_id, client_token=None) -> None:
    """Downloads a file
    Args:
        file_id: ID of the file to download
        file_name: name of file to download
        client_token: client access token

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    
    if not client_token:
        SCOPES = ['https://www.googleapis.com/auth/drive']  # only first item is necessary for basic downloads
        credentials = None
        CLIENT_FILE = 'client_credentials.json'

        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_FILE, SCOPES)
        flow.redirect_uri = "https://developers.google.com/oauthplayground"
        credentials = flow.run_local_server(port=0)
        client_token = json.loads(credentials.to_json())['token']
        
        
    url = "https://www.googleapis.com/drive/v2/files/{}?alt=media".format(file_id)
    header = {"Authorization": "Bearer " + client_token}
    resp = requests.get(url, headers=header)
    return resp.content