# Sheets contstants
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CLIENT_SECRET_PATH = 'credentials/client_secret.json'
SPREADSHEET_ID_PATH = 'credentials/sheet_id'

# ========= Time series constants ========= 

# Key rows
SERIES_DATA_START = str(3)
SERIES_ROW_LIMIT = str(100) # Limits how many rows the api will search if all data is requested

# Key columns
DATE_COLUMN = "A"
ACTIVITY_DESC_COLUMN = "B"

# ========= Details constants ========= 

# Key rows
DETAILS_DATA_START = str(3)
DETAILS_DATA_END = str(13) # Limits how many rows the api will search if all data is requested

# Key columns
DETAILS_DESC_COLUMN = "W"

# ========= Mapping people to colums ========= 

# Helper class for storing ppl
class YogiMapping():
	def __init__(self, gradeCol, deltaCol, scoreCol, detailsCol):
		# Time series
		self.gradeCol=gradeCol
		self.deltaCol=deltaCol
		self.scoreCol=scoreCol
		# Details
		self.detailsCol=detailsCol

# Contants related to a person
_CISSI = YogiMapping("D","E","F","X")
_EMIL = YogiMapping("G","H","I","Y")
_FANNY = YogiMapping("J","K","L","Z")
_HENRY = YogiMapping("M","N","O","AA")
_LANNY = YogiMapping("P","Q","R","AB")
_EMELIA = YogiMapping("S","T","U","AC")

# Dictinary used to find column mapping given id/key
YOGIS = {
	"cissi" : _CISSI,
	"emil" : _EMIL,
	"fanny" : _FANNY,
	"henry" : _HENRY,
	"lanny" : _LANNY,
	"emelia" : _EMELIA
}

