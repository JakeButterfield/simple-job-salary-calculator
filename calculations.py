#Functions for the program
def moneyWeek(salary, hours):
	total = salary * hours
	return int(total)

def moneyMonth(salary, hours):
	week = salary * hours
	total = week * 4
	return int(total)

def moneyYear(salary, hours):
	week = salary * hours
	month = week * 4
	total = month * 12
	return int(total)

def moneyVidWeekYT(videos, moneyVid):
	total = videos * moneyVid
	return int(total)

def moneyVidMonthYT(videos, moneyVid):
	week = videos * moneyVid
	total = week * 4
	return int(total)

def moneyVidYearYT(videos, moneyVid):
	week = videos * moneyVid
	month = week * 4
	total = month * 12
	return int(total)

def moneyViewVideoYT(videos, viewVid):
	total = viewVid / 500
	return int(total)

def moneyViewWeekYT(videos, viewVid):
	moneyVidView = viewVid / 500
	total = moneyVidView * videos
	return int(total)

def moneyViewMonthYT(videos, viewVid):
	moneyVidView = viewVid / 500
	week = moneyVidView * videos
	total = week * 4
	return int(total)

def moneyViewYearYT(videos, viewVid):
	moneyVidView = viewVid / 500
	week = moneyVidView * videos
	month = week * 4
	total = month * 12
	return int(total)
