from time import sleep

def zipcodecheck(zipcode) :
	if zipcode in range(1000, 2792):
		url = "ma"
	elif zipcode in range(2801, 2941):
		url = "ri"
	elif zipcode in range(3031, 3898):
		url = "nh"
	elif zipcode in range(3901, 4883):
		url = 'me'
	elif zipcode in range(5001, 5908):
		url = 'vt'
	elif zipcode in range(6001, 6929):
		url = 'ct'
	elif zipcode in range(7001, 8990):
		url = 'nj'
	elif zipcode in range(10000, 14976):
		url = 'ny'
	elif zipcode in range(15000, 19641):
		url = 'pa'
	elif zipcode in range(19701, 19980):
		url = 'de'
	else:
		print "Invalid Zipcode, exiting in\n"
		countdown = 3
		for number1 in range(0, 4):
			sleep(1)
			print countdown
			countdown -= 1
		exit()
	return url