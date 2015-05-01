from handler import Handler

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


class Birthday(Handler):
#	def write_form(error=""):
#	self.render("birthday.html", 

	def get(self):
		self.render("birthday.html")

	def post(self):
		month = valid_month(self.request.get("month"))
		day = valid_day(self.request.get("day"))
		year = valid_year(self.request.get("year"))
		if(month and day and year):
			self.write("ALL FINE")
		else:
			self.render("birthday.html")
			self.write(bad_date)  # Hacky solution to get error message. 
