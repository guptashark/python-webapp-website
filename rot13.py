import webapp2
import string

rot13_form = """
<form method="post">
	<h1>Enter some text to ROT13:</h1>
	<textarea name="text" cols="50" rows="10">%(plain)s</textarea>
	<br>
	<input type="submit">
</form>
"""

class Rot13(webapp2.RequestHandler):
	def write_form(self, plain=""):
		self.response.write(rot13_form % {"plain" : plain})

	def get(self):
		self.write_form();
	
	def post(self):
		plainText = self.request.get("text")
		plain = plainText.encode('rot13')
		self.write_form(plain)
