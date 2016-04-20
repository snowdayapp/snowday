#Seperates the location of zipcodes from main file.
from time import sleep
import zipcodes

def checkzip(zipcode):
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
	elif zipcode in range(20001, 20100) or zipcode in range(20201, 20600) or zipcode in range(56901, 56973):
		url = 'dc'
	elif zipcode in range(20101, 20200) or zipcode in range(22001, 24659):
		url = 'va'
	elif zipcode in range(20601, 21931):
		url = 'md'
	elif zipcode in range(24701, 26887):
		url = 'wv'
	elif zipcode in range(27006, 28910):
		url = 'nc'
	elif zipcode in range(29001, 29946):
		url = 'sc'
	elif zipcode in range(30001, 32000):
		url = 'ga'
	elif zipcode in range(32003, 34998):
		url = 'fl'
	elif zipcode in range(35004, 36926):
		url = 'al'
	elif zipcode in range(37010, 38590):
		url = 'tn'
	elif zipcode in range(38601, 39777):
		url = 'ms'
	elif zipcode in range(39813, 39902):
		url = 'ga'
	elif zipcode in range(40003, 42789):
		url = 'ky'
	elif zipcode in range(43001, 45600):
		url = 'oh'
	elif zipcode in range(46001, 47998):
		url = 'in'
	elif zipcode in range(48001, 49972):
		url = 'mi'
	elif zipcode in range(50001, 52810):
		url = 'ia'
	elif zipcode in range(53001, 54991):
		url = 'wi'
	elif zipcode in range(55001, 56764):
		url = 'mn'
	else:
		print "Invalid Zipcode, exiting in\n"
		countdown = 3
		for number1 in range(0, 4):
			sleep(1)
			print countdown, "\n"
			countdown -= 1
		exit()
	city = zipcodes.zipcodedict[int(zipcode)]
	return url, city