from handler import Handler

class Password(Handler):
	def get(self):
		q = self.request.get("q")
		self.write("You can clearly see your password in the url.<br>")
		self.write("The password is: ")
		self.write(q)