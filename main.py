import os
import webapp2
from handler import Handler
from birthday import Birthday

class MainPage(Handler):
	def get(self):
#		self.render("forms.html")
		self.render("birthday.html")		

class TestHandler(webapp2.RequestHandler):
	def get(self):
		#q = self.request.get("q")
		self.response.headers['Content-type'] = 'text/plain'
		self.response.write(q)

	def post(self):
		self.response.headers['Content-type'] = 'text/plain'
		self.response.write(self.request)

class PassWord(webapp2.RequestHandler):
	def get(self):
		q = self.request.get("q")
		self.response.write("You can clearly see your password in the url.<br>")
		self.response.write("The password is: ")
		self.response.write(q)

app = webapp2.WSGIApplication([
		('/', MainPage),
		('/testhandler', TestHandler),
		('/password', PassWord),
		('/birthday', Birthday)
], debug=True)
