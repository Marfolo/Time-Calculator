def add_time(start_time, duration_time):
	#start_time -> ["12:20 AM"]
	#duration_time -> ["4:40"]

	temp1, time_symbol = start_time.split()
	dur1, dur2 = duration_time.split(':')
	sta1, sta2 = temp1.split(':')


	return new_time