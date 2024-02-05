from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd

SERVICE_ACCOUNT_FILE = 'individual-413420-696c57a6de69.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1SahPL83sheaoakVfzJ91I1p3oAVIfScIBOUrF_1QitQ'
SHEET_NAME = 'Лист1'
NEW_SHEET_NAME = 'Отсортированный Лист'

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SHEET_NAME).execute()
values = result.get('values', [])

if not values:
    print('No data found.')
else:
    df = pd.DataFrame(values)

    df_sorted = df.sort_values(by=2)

    request_body = {
        'requests': [{
            'addSheet': {
                'properties': {
                    'title': NEW_SHEET_NAME
                }
            }
        }]
    }
    service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=request_body).execute()

    values_for_update = df_sorted.values.tolist()

    update_range = f"{NEW_SHEET_NAME}!A1"

    update_body = {
        'values': values_for_update
    }
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=update_range,
        valueInputOption='RAW', body=update_body).execute()
