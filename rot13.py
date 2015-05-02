import webapp2
import string

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rot13_form = """
<form method="post">
	<h1>Enter some text to ROT13:</h1>
	<textarea name="text" cols="50" rows="10">
	</textarea>
	<br>
	<input type="submit">
</form>
"""

def encode(plainText):
	rot13 = string.maketrans(
			"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
			"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	return string.translate(plainText, rot13)


class Rot13(webapp2.RequestHandler):
	def get(self):
		self.response.write(rot13_form)
	
	def post(self):
		plainText = self.request.get("text")
		cipherText = encode(plainText)
		self.response.write(ciperText)
