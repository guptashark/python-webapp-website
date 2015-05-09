import string
from handler import Handler

class Rot13(Handler):
	def write_form(self, plain=""):
		self.render("rot13-form.html", plain=plain)

	def get(self):
		self.write_form();
	
	def post(self):
		plainText = self.request.get("text")
		mYplain = plainText.encode('rot13')
		self.write_form(mYplain)
