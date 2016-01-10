import datetime
import math
import time

def is_leap_year(year):
	if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
		return True
	else:
		return False

def perpetual_calendar(year, month, day):
	monthsInYear = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
	monthsInLeapYear = [6, 2, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
	tableForC = [6, 4, 2, 0]
	
	g = day % 7
	
	if is_leap_year(year) is True:
		m = monthsInLeapYear[month - 1]
	else:
		m = monthsInYear[month - 1]
	
	a2 = int(math.floor(((((year % 100) % 28) - 1) / 4)))
	a2 = a2 + 1 if a2 < 0 else a2
	a = ((year % 100)% 28) + a2
	
	c = tableForC[int(math.floor(year / 100) % 4)]
	
	return (g + m + a + c) % 7

def main():
	initial_date = datetime.date(1901, 1, 1)
	currentDay = perpetual_calendar(1901, 1, 1)
	final_date = datetime.date(2000, 12, 31)
	total = 0

	while initial_date != final_date:
		if initial_date.day == 6 and currentDay == 0:
			total += 1

		initial_date += datetime.timedelta(days=1)
		currentDay = (currentDay + 1) % 7

	print("The result is %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))