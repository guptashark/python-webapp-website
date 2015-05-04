import webapp2

userform = """
<h1>User Signup</h1>
<form method="post">
	<label>	
		Name
		<input name="name" value=%(name)s>
	</label>
	<div style="color: red">%(error1)s</div>
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
	<div style="color: red">%(error2)s</div>
	<br>
	<label>
		Email (optional)
		<input name="email" value=%(email)s>
	</label>
	<br>
	<input type="submit">
</form>
"""

def matchPasswords(string1, string2):
	if string1:
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
	def write_form(self, error1="", error2="", name="", email=""):
		self.response.write(userform % {"error1" : error1,
										"error2" : error2,
										"name" : name,
										"email" : email})

	def get(self):
		self.write_form()

	def post(self):
		userName = self.request.get("name") # Weird behavior... 
# check username input like: Aishwary Gupta, why does form refill with just Aishwary?
		password = self.request.get("password")
		verify   = self.request.get("verify")
		email    = self.request.get("email")
		if(matchPasswords(password, verify) and validName(userName)):
			self.redirect("/thanks")
		elif(matchPasswords(password, verify)):
			self.write_form("Not a vaild username.", "", userName, email)
		elif(validName(userName)):
			self.write_form("", "Passwords don't match and cannot be empty.", 
					userName, email)
		else:
			self.write_form("Not a valid username.", 
							"Passwords don't match", 
							userName, 
							email)
