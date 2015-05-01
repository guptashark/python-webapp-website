import os
import webapp2
from showrequest import ShowRequest
from handler import Handler
from password import Password
from birthday import Birthday

class MainPage(Handler):
	def get(self):
		self.render("forms.html")
		self.render("birthday.html")		

app = webapp2.WSGIApplication([
		('/', MainPage),
		('/showrequest', ShowRequest),
		('/password', Password),
		('/birthday', Birthday)
], debug=True)
