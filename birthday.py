import webapp2

class Birthday(webapp2.RequestHandler):
	def post(self):
		month = self.request.get("month")
		day = self.request.get("day")
		year = self.request.get("year")
		self.response.write("ALL FINE, SRSLY, pls believe")

