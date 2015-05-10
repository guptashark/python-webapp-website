from handler import Handler

class Playground(Handler):
	def get(self):
		self.render("playground.html")
