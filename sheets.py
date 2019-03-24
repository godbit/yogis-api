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
		series = self.sheet.get(spreadsheetId=self.sheetID,
								range=yogi.gradeCol + SERIES_DATA_START + ":" + yogi.scoreCol + SERIES_ROW_LIMIT).execute()
		activities = self.getActivities()
		
		return self._mapSeries(activities["values"], series["values"])
	
	# Fetches column description for yogi details
	def _getDetialsDesc(self):
		result = self.sheet.get(spreadsheetId=self.sheetID,
								range=DETAILS_DESC_COLUMN + DETAILS_DATA_START + ":" + DETAILS_DESC_COLUMN + DETAILS_DATA_END).execute()
		return result

	# Fetches details data for a single yogi
	def getYogiDetails(self, key):
		yogi = YOGIS[key]
		yogiDetailValues = self.sheet.get(spreadsheetId=self.sheetID,
								range=yogi.detailsCol + DETAILS_DATA_START + ":" + yogi.detailsCol + DETAILS_DATA_END).execute()
		detailsKeys = self._getDetialsDesc()

		return self._mapSingleKeyAndValue(detailsKeys["values"], yogiDetailValues["values"])

	# Maps the activity series with a persons grade/score series. The date of the activity is the key.
	def _mapSeries(self, activites, series):
		yogiSeries = []
		for i in range(len(activites)):
			innerMap = {}
			innerMap["date"] = activites[i][0]
			innerMap["description"] = activites[i][1]
			innerMap["grade"] = series[i][0]
			innerMap["delta"] = series[i][1]
			innerMap["score"] = series[i][2]
			yogiSeries.append(innerMap)
		return yogiSeries

	# Maps two lists of lists (with one element) to a dictionary
	def _mapSingleKeyAndValue(self, keys, values):
		map = {}
		for i in range(len(keys)):
			map[keys[i][0]] = values[i][0]
		return map
