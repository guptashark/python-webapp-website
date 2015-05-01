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

class Birthday(Handler):
	def get(self):
		self.render("birthday.html")

#	def valid_month(month):
#		if (month):
#			myMonth = month.capitalize()
#			for i in months:
#				if (myMonth == i):
#					return myMonth
#		return None
#
#	def valid_day(day):
#		if (day and day.isdigit()):
#			myDay = int(day)
#			if(myDay >= 1 and myDay <= 31):
#				return myDay
#		return None
	
#	def valid_year(year):
#		if (year and year.isdigit()):
#			mYear = int(year)
#			if(mYear >= 1900 and mYear <= 2020):
#				return mYear
#		return None

	def post(self):
		month = self.request.get("month")
		day = self.request.get("day")
		year = self.request.get("year")
#		if(valid_month(month) and valid_day(day) and valid_year(year)):
		self.write("ALL FINE, SRSLY, pls believe")
#		else:
#			self.render("birthday.html")
