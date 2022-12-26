def add_time(start_time, duration_time):
	#start_time -> ["12:20 AM"]
	#duration_time -> ["4:40"]

	temp1, time_symbol = start_time.split()
	dur1, dur2 = duration_time.split(':')
	sta1, sta2 = temp1.split(':')

	dur1, dur2 = int(dur1), int(dur2)
	sta1, sta2 = int(sta1), int(sta2)

	#PAY CLOSE ATTENTION TO THE SPACING AND PUNCTUATION OF THE RESULTS
	if sta1 > 12 or sta1 < 1: #valid times
		print("Error")
	elif sta2 >= 60 or sta2 < 0: #valid times
		print("Error")
	elif dur2 >= 60 or dur2 < 0: #valid times
		print("Error")
	else: #if everything went okay
		new1 = sta1 + dur1 #adding hours
		new2 = sta2 + dur2 #adding minutes

		symbols = ["AM", "PM"]
		how_many_days = 0

		if new1 > 12:


	return 1#new_time