import calculations as cal

#Program Start
def main():

	print("Welcome to the Job Salary Calculator")

	while True:
		try:
			haveJob = input("Do you have a job already? (Yes or No) > ")
			break
		except:
			print("Please enter Yes or No.")
			continue

	if(haveJob == "Yes"):

		while True:
			try:
				job = input("What is your job? (Normal or YouTuber) > ")
				break
			except:
				print("Please enter a valid job (Normal or YouTuber).")
				continue

		if(job == "Normal"):

			while True:
				try:
					salary = float(input("How much do you make per hour? > £"))
					break
				except:
					print("Please enter a valid number.")
					continue

			while True:

				try:
					hours = float(input("How many hours do you work per week? > "))
					break
				except:
					print("Please enter a valid number.")
					continue

			print("You will make £", cal.moneyWeek(salary, hours), " per week,")
			print("You will make £", cal.moneyMonth(salary, hours), " per month")
			print("You will make £", cal.moneyYear(salary, hours), " per year")

			print("Thank you for using the Job Calculator\n\n")
			main()					

		elif(job == "YouTuber"):

			while True:
				try:
					videos = int(input("How many videos do you make per week? > "))
					break
				except:
					print("Please enter a valid number.")
					continue

			while True:
				try:
					query = str(input("Do you know how much you make per video? (Yes or No) > "))
					break
				except:
					print("Please enter Yes or No.")
					continue

			if(query == "Yes"):

				while True:
					try:
						moneyVid = float(input("How much do you make per video? > £"))
						break
					except:
						print("Please enter a valid number.")
						continue

				print("You will make £", moneyVidWeekYT(videos, moneyVid), " per week,")
				print("You will make £", moneyVidMonthYT(videos, moneyVid), " per month")
				print("You will make £", moneyVidYearYT(videos, moneyVid), " per year")

			elif(query == "No"):

				while True:
					try:
						viewVid = float(input("How many views do you get per video? > "))
						break
					except:
						print("Please enter a valid number.")
						continue

				print("You will make around £", moneyViewVideoYT(videos, viewVid), " per video,")
				print("You will make around £", moneyViewWeekYT(videos, viewVid), " per week,")
				print("You will make around £", moneyViewMonthYT(videos, viewVid), " per month")
				print("You will make around £", moneyViewYearYT(videos, viewVid), " per year")

			print("Thank you for using the Job Calculator\n\n")
			main()

		else:
			print("That job is not recognised!")

		print("Thank you for using the Job Calculator\n\n")
		main()

	elif(haveJob == "No"):
		
		while True:
			try:
				haveJobAspiration = int(input("How much would you like to make per year? > £"))
				break
			except:
				print("Please enter a valid number.")
				continue

		while True:
			try:
				haveJobHours = int(input("How many hours would you like to work per week? > "))
				break
			except:
				print("Please enter a valid number.")
				continue

		haveJobMonth = haveJobAspiration / 12
		haveJobWeek = haveJobMonth / 4

		haveJobTotal = haveJobWeek / haveJobHours

		haveJobFinal = round(haveJobTotal, 1)

		print("You will need to earn ", haveJobFinal, "per hour to earn £", haveJobAspiration," per year")

		print("Thank you for using the Job Calculator\n\n")

		main()

if __name__ == '__main__':
	main()