import webapp2
import cgi

form = """
<p> When is your birthday?</p>
<form method="post" action="/birthday">
	<label>
		Month
		<input type="text" name="month" value=%(month)s>
	</label>
	<label>
		Day
		<input type="text" name="day" value=%(day)s>
	</label>
	<label>
		Year
		<input type="text" name="year" value=%(year)s>
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

def escape_html(s):
	return cgi.escape(s, quote = True)

class Birthday(webapp2.RequestHandler):
	def write_form(self, error="", month="", day="", year=""):
		self.response.write(form % {"error": error, 
									"month": month, 
									"day": day, 
									"year": year})

	def get(self):
		self.write_form()

	def post(self):
		month = escape_html(self.request.get("month"))
		day = escape_html(self.request.get("day"))
		year = escape_html(self.request.get("year"))
		if(valid_month(month) and valid_day(day) and valid_year(year)):
			self.response.write("ALL FINE")
		else:
			self.write_form("That is not a valid date.", month, day, year) 
