import httplib2
import os
import json

from apiclient import discovery
from google.oauth2 import service_account

from constants import *

class SheetsApi(object):
	def __init__(self):
		self.credentials = self._getCredentials()
		self.service = discovery.build('sheets', 'v4', credentials=self.credentials)
		self.sheet = self.service.spreadsheets().values()
		self.sheetID = self._getSpreadSheetID()

	def _getSpreadSheetID(self):
		with open(SPREADSHEET_ID_PATH, 'r') as file:
			id = file.readline()
		return id

	def _getCredentials(self):
		credentials_path = os.path.join(os.getcwd(), CLIENT_SECRET_PATH)
		return service_account.Credentials.from_service_account_file(
			credentials_path, scopes=SCOPES)

	# Fetches all dates and descriptions
	def getActivities(self):
		result = self.sheet.get(spreadsheetId=self.sheetID,
								range=DATE_COLUMN + SERIES_DATA_START + ":" + ACTIVITY_DESC_COLUMN + SERIES_ROW_LIMIT).execute()
		return result
	
	# Fetches times series data for a single yogi
	def getYogiSeries(self, key):
		yogi = YOGIS[key]
		# The delta colum is inbetween gradeCol and scoreCol => included automatically
		result = self.sheet.get(spreadsheetId=self.sheetID,
								range=yogi.gradeCol + SERIES_DATA_START + ":" + yogi.scoreCol + SERIES_ROW_LIMIT).execute()
		return result
	
	# Fetches column description for yogi details
	def getDetialsDesc(self):
		result = self.sheet.get(spreadsheetId=self.sheetID,
								range=DETAILS_DESC_COLUMN + DETAILS_DATA_START + ":" + DETAILS_DESC_COLUMN + DETAILS_DATA_END).execute()
		return result

	# Fetches details data for a single yogi
	def getYogiDetails(self, key):
		yogi = YOGIS[key]
		result = self.sheet.get(spreadsheetId=self.sheetID,
								range=yogi.detailsCol + DETAILS_DATA_START + ":" + yogi.detailsCol + DETAILS_DATA_END).execute()
		return result
