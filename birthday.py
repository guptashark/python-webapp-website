import webapp2

form = """
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
	<div style="color: red">%(error)s</div>
	<br>
	<input type="submit">
</form>
"""

months = [	
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December']

# The bad_date thing is a hacky error message solution. 
bad_date = """
<div style="color: red">That is not a valid date.</div>
"""

def valid_month(month):
	if (month):
		myMonth = month.capitalize()
		for i in months:
			if (myMonth == i):
				return myMonth
	return None

def valid_day(day):
	if (day and day.isdigit()):
		myDay = int(day)
		if(myDay >= 1 and myDay <= 31):
			return myDay
	return None

def valid_year(year):
	if (year and year.isdigit()):
		mYear = int(year)
		if(mYear >= 1900 and mYear <= 2020):
			return mYear
	return None


class Birthday(webapp2.RequestHandler):
	def write_form(self, error=""):
		self.response.write(form % {"error": error})

	def get(self):
		self.write_form()

	def post(self):
		month = valid_month(self.request.get("month"))
		day = valid_day(self.request.get("day"))
		year = valid_year(self.request.get("year"))
		if(month and day and year):
			self.response.write("ALL FINE")
		else:
			self.write_form("That is not a valid date.") 
