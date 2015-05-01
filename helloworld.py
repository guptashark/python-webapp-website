import webapp2
from birthday import Birthday
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

<p>A form whose action is to submit the text to TestHandler instead of google search.</p>
<form action="/testhandler">
	<input name="q">
	<input type="submit">
</form>

<p>A form that does the same action as above, but uses a post method instead of get.</p>
<form method="post" action="/testhandler">
	<input name="q">
	<input type="submit">
</form>

<p>A form that has a type different from text - it has a type of password.</p>
<form action="/password">
	<input type="password" name="q">
	<input type="submit">
</form>

<p>A form where we can experiment with the different kinds of inputs.</p>
<form>
	<input type="checkbox" name="q">
	<input type="checkbox" name="r">
	<input type="checkbox" name="s">
	<input type="submit">
	<br>
	<label>
		One
		<input type="radio" name="t" value="one">
	</label>
	<br>
	<label>
		Two
		<input type="radio" name="t" value="two">
	</label>
	<br>
	<label>
		Three
		<input type="radio" name="t" value="three">
	</label>
	<br>
	<input type="submit">
	<br>
	<select name="q">
		<option value="1">Red</option>
		<option value="2">Blue</option>
		<option value="3">Yellow</option>
	</select>
	<input type="submit">
</form>
"""

birthday = """
<p> When is your birthday?</p>
<form method="post" action="/birthday">
	<label>
		Month
		<input type="text" name="month">
	</label>
	<label>
		Day
		<input type="text" name="day">
	</label>
	<label>
		Year
		<input type="text" name="year">
	</label>
	<br>
	<br>
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
#		self.response.write(form)
		self.response.write(birthday)		

class TestHandler(webapp2.RequestHandler):
	def get(self):
		#q = self.request.get("q")
		self.response.headers['Content-type'] = 'text/plain'
		self.response.write(q)

	def post(self):
		self.response.headers['Content-type'] = 'text/plain'
		self.response.write(self.request)

class PassWord(webapp2.RequestHandler):
	def get(self):
		q = self.request.get("q")
		self.response.write("You can clearly see your password in the url.<br>")
		self.response.write("The password is: ")
		self.response.write(q)

app = webapp2.WSGIApplication([
		('/', MainPage),
		('/testhandler', TestHandler),
		('/password', PassWord),
		('/birthday', Birthday)
], debug=True)
