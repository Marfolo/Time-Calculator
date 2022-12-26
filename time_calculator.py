def add_time(start_time, duration_time):
	#start_time -> ["12:20 AM"]
	#duration_time -> ["4:40"]

	temp1, time_symbol = start_time.split()
	dur1, dur2 = duration_time.split(':')
	sta1, sta2 = temp1.split(':')

	dur1, dur2 = int(dur1), int(dur2)
	sta1, sta2 = int(sta1), int(sta2)

	#PAY CLOSE ATTENTION TO THE SPACING AND PUNCTUATION OF THE RESULTS
	if sta1 > 12 or sta1 < 1:
		print("Error")
	elif sta2 >=60 or sta2 < 0:
		print("Error")
	elif dur2 >=60 or dur2 < 0:
		print("Error")
	else:
		print("hi")


	return 1#new_time