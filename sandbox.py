from handler import Handler

class Sandbox(Handler):
	def get(self):
		self.render("sandmenu.html")
		self.render("forms.html")

