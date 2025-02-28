import os
import google.auth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError

# If modifying a sheet is required, the SCOPES variable should include:
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Set the path to your credentials file using an environment variable
CREDS_PATH = os.getenv('GOOGLE_CREDS_PATH', './config/credentials.json')  # Default if not found

def get_credentials():
    """Shows the authentication flow and gets the credentials."""
    creds = None
    # Check if token.json exists and is valid
    if os.path.exists('token.json'):
        creds, _ = google.auth.load_credentials_from_file('token.json')

    # If no valid credentials are available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # OAuth flow for getting the credentials
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)  # Removed redirect_uri here, it will be auto handled
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def create_google_sheet(spreadsheet_name):
    """Creates a new Google Sheet and returns the link."""
    try:
        creds = get_credentials()
        service = build('sheets', 'v4', credentials=creds)
        
        # Define the properties for the new Google Sheet
        spreadsheet = {
            'properties': {
                'title': spreadsheet_name
            },
            'sheets': [{
                'properties': {
                    'title': 'Sheet1'
                }
            }]
        }

        # Create the spreadsheet
        spreadsheet = service.spreadsheets().create(body=spreadsheet).execute()

        # Return the URL of the new sheet
        sheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet['spreadsheetId']}/edit"
        return sheet_url
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None  # or return some appropriate error response

def get_google_sheet_link(spreadsheet_id):
    """Returns the Google Sheet link for an existing spreadsheet ID."""
    if not spreadsheet_id:
        raise ValueError("spreadsheet_id is required to generate the link")
    
    return f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit"
