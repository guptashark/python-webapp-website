import webapp2

class ShowRequest(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-type'] = 'text/plain'
		self.response.write(self.request)

	def post(self):
		self.response.headers['Content-type'] = 'text/plain'
		self.response.write(self.request)
