from flask import Flask
from flask_restful import Resource, Api

from sheets import SheetsApi

app = Flask(__name__)
api = Api(app)

class Activities(Resource):
	def get(self):
		return SheetsApi().getActivities()

class YogiSeries(Resource):
	def get(self, key):
		return SheetsApi().getYogiSeries(key)

class YogiDetails(Resource):
	def get(self, key):
		return SheetsApi().getYogiDetails(key)


api.add_resource(Activities, '/activities/')
api.add_resource(YogiSeries, '/yogiSeries/<string:key>')
api.add_resource(YogiDetails, '/yogiDetails/<string:key>')


if __name__ == '__main__':
	app.run(debug=True)