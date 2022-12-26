def add_time(start_time, duration_time):
	#start_time -> ["12:20 AM"]
	#duration_time -> ["4:40"]

	temp1, time_symbol = start_time.split()
	dur1, dur2 = duration_time.split(':')
	sta1, sta2 = temp1.split(':')

	dur1, dur2 = int(dur1), int(dur2)
	sta1, sta2 = int(sta1), int(sta2)

	if sta1 > 12 or sta1 < 1: #valid times
		print('Error')
	elif sta2 >= 60 or sta2 < 0: #valid times
		print('Error')
	elif dur2 >= 60 or dur2 < 0: #valid times
		print('Error')
	else: #if everything went okay
		new1 = sta1 + dur1 #adding hours
		new2 = sta2 + dur2 #adding minutes

		#I determine whether it should be AM or PM
		if time_symbol == 'AM': #this is good
			symbols = ['AM', 'PM'] #this is good
		elif time_symbol == 'PM': #this is good
			symbols = ['PM', 'AM'] #this is good
		how_many_days = int(new1 / 12) #this is good
		how_many_min = int(new2 / 60) #this is good
		days_count = -1 #to count the days
		for i in range(how_many_days + 1): #this is good
			days_count = days_count + 1
			if i % 2 == 0:
				x = 0
			else:
				x = 1

		#PAY CLOSE ATTENTION TO THE SPACING AND PUNCTUATION OF THE RESULTS
		#The magic part
		something = ['', '(next day)']
		for i in range(2, how_many_days + 1):
			something.append('(' + str(i) + ' days later)')
		if new1 > 12:
			if new2 >= 60:
				return str(new1 - 12 * how_many_days) + ':' + str(new2 - 60 * how_many_min) + symbols[x] + ' ' + something[days_count]
			else: #if new minutes < 60
				return str(new1 - 12 * how_many_days) + ':' + str(new2) + symbols[x] + ' ' + something[days_count]
		else: #if new hours < 12
			if new2 >= 60:
				return str(new1) + ':' + str(new2 - 60 * how_many_min) + symbols[x] + ' ' + something[days_count]
			else: #if new minutes < 60
				return str(new1) + ':' + str(new2) + symbols[x] + ' ' + something[days_count]

	#return new_time