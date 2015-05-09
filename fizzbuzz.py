from handler import Handler

class FizzBuzz(Handler):
	def get(self):
		n = self.request.get('n', 0)
		n = n and int(n)
		self.render("fizzbuzz.html", n = n)
