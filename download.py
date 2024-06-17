# download_from_drive.py
import argparse
import os
import io
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

TOKEN_FILE = './creds/token.json'
CREDENTIALS_FILE = './creds/credentials.json'

def authenticate():
    """Shows basic usage of the Drive v3 API.
    Lists the user's Google Drive files.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return creds

def download_file_from_drive(drive_service, file_id, output_path):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(output_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")
    fh.close()

def main():
    parser = argparse.ArgumentParser(description="Download a file from Google Drive")
    parser.add_argument("file_id", type=str, help="Google Drive file ID for the file to be downloaded")
    parser.add_argument("output_file", type=str, help="Path to save the downloaded file")

    args = parser.parse_args()

    creds = authenticate()
    drive_service = build('drive', 'v3', credentials=creds)
    download_file_from_drive(drive_service, args.file_id, args.output_file)

if __name__ == "__main__":
    main()
