print "Welcome to SnowDay, please type in your zipcode."
zipcode = int(raw_input('> '))
if zipcode in range(1000, 2792):
	location = "ma"
elif zipcode in range(2801, 2941):
	location = "ri"
elif zipcode in range(3031, 3898):
	location = "nh"
