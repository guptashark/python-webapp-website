import webapp2

userform = """
<h1>User Signup</h1>
<form method="post">
	<label>	
		Name
		<input name="name">
	</label>
	<br>
	<label>
		Password
		<input type="password" name="password">
	</label>
	<br>
	<label>
		Verify Password
		<input type="password" name="verify">
	</label>
	<br>
	<label>
		Email (optional)
		<input name="email">
	</label>
	<br>
	<input type="submit">
</form>
"""

def matchPasswords(string1, string2):
	if(string1 == string2):
		return True
	else:
		return False

def validName(myUser):
	if (myUser):
		if(' ' in myUser):
			return False
		else:
			return True

class SignUp(webapp2.RequestHandler):
	def write_form(self):
		self.response.write(userform)

	def get(self):
		self.write_form()

	def post(self):
		userName = validName(self.request.get("name"))
		password = self.request.get("password")
		verify   = self.request.get("verify")
		email    = self.request.get("email")
		if(matchPasswords(password, verify) and userName):
			self.redirect("/thanks")
		else:
			self.write_form()
			self.response.write("Error! Bad input.")
