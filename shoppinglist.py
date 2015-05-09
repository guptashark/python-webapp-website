import webapp2

class ShoppingList(webapp2.RequestHandler):
	def get(self):
		self.response.write("This is a shopping List.")
