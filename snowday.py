def zipcodecheck():
	if zipcode in range(1000, 2792):
		location = "ma"
	elif zipcode in range(2801, 2941):
		location = "ri"
	elif zipcode in range(3031, 3898):
		location = "nh"
	elif zipcode in range(3901, 4883):
		location = 'me'
	elif zipcode in range(5001, 5908):
		location = 'vt'
	else:
		exit()
	return location

def main():
print "Welcome to SnowDay, please type in your zipcode."
zipcode = int(raw_input('> '))
