from handler import Handler
import webapp2

class Birthday(Handler):
	def post(self):
		month = self.request.get("month")
		day = self.request.get("day")
		year = self.request.get("year")
		self.write("ALL FINE, SRSLY, pls believe")

