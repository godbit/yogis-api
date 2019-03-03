import httplib2
import os
import json

from apiclient import discovery
from google.oauth2 import service_account

# Constants
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CLIENT_SECRET_PATH = 'credentials/client_secret.json'
SPREADSHEET_ID_PATH = 'credentials/sheet_id'

class SheetsApi(object):
	def __init__(self):
		self.credentials = self.getCredentials()
		self.service = discovery.build('sheets', 'v4', credentials=self.credentials)
		self.sheet = self.service.spreadsheets()

	def getSpreadSheetID(self):
		with open(SPREADSHEET_ID_PATH, 'r') as file:
			id = file.readline()
		return id

	def getCredentials(self):
		credentials_path = os.path.join(os.getcwd(), CLIENT_SECRET_PATH)
		return service_account.Credentials.from_service_account_file(
			credentials_path, scopes=SCOPES)

	def getAllData(self):
		result = self.sheet.values().get(spreadsheetId=self.getSpreadSheetID(), range='A1:Q100').execute()
		print(json.dumps(result, indent=4, sort_keys=True))
		return result
	
	def getColumn(self, column):
		result = self.sheet.values().get(spreadsheetId=self.getSpreadSheetID(), range=(column + ":" + column)).execute()
		print(json.dumps(result, indent=4, sort_keys=True))
		return result
