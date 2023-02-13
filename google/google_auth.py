Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
"""Universal file for getting google client authorizatoin"""
from __future__ import print_function # weird google stuff

import io

import google.auth
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials
import os
# 

from google.oauth2 import service_account


import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow


def google_auth():

    # for this script you will need the generic google client credentials file 1token.json and a client_credentials file (can be blank).

    SCOPES =  []  # list app scopes
    credentials = None
    CLIENT_FILE = 'client_credentials.json'  # can update this to a path if needed

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())
    

if __name__ == '__main__':
    
    auth()


