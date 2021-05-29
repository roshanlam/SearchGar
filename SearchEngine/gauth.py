from glib import Create_Service
import os
CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

files = os.listdir("../Data/")

info = [i for i in files]

for i in info:
    file_meta = {
        'name': i,
        'mineType': 'application/vnd.google-apps.folder'
    }

    service.files().create(body=file_meta).execute()
