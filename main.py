from flask import Flask
from flask_restful import Resource, Api

from sheets import SheetsApi

app = Flask(__name__)
api = Api(app)

class Sheets(Resource):
	def get(self):
		sheetsApi = SheetsApi()
		return sheetsApi.getAllData()

class SheetsColumn(Resource):
	def get(self, column):
		sheetsApi = SheetsApi()
		return sheetsApi.getColumn(column)

class Test(Resource):
	def get(self):
		sheetsApi = SheetsApi()
		return sheetsApi.getSpreadSheetID()

api.add_resource(Sheets, '/sheets/')
api.add_resource(SheetsColumn, '/sheets/column/<string:column>')
api.add_resource(Test, '/test/')

if __name__ == '__main__':
	app.run(debug=True)