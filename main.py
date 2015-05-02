import os
import webapp2
from showrequest import ShowRequest
from handler import Handler
from password import Password
from birthday import Birthday
from birthday import Thanks
from sandbox import Sandbox
from rot13 import Rot13

class MainPage(Handler):
	def get(self):
#		self.render("forms.html")
#		self.render("birthday.html")		
		self.render("menubar.html")
		self.render("home.html")
		
app = webapp2.WSGIApplication([
		('/', MainPage),
		('/showrequest', ShowRequest),
		('/password', Password),
		('/birthday', Birthday),
		('/sandbox', Sandbox),
		('/thanks', Thanks),
		('/rot13', Rot13)
], debug=True)
