import webapp2

form = """
<form>
	<p>Just an input box.</p>
	<input>
	<p>An input box with a "name" paramater of "q". You should see it in the browser when you hit enter.</p>
	<input name="q">
	<p>A submit button. Either press enter or click the submit button, same action happens.</p>
	<input type="submit">
</form>

<p>A form whose action is to submit the query into google search.</p>

<form action="http://www.google.com/search">
	<input name="q">
	<input type=submit>
</form>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write(form)

app = webapp2.WSGIApplication([
		('/', MainPage),
	], debug=True)
