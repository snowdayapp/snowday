#Seperates the location of zipcodes from main file.
from time import sleep
import zipcodes
import dictionaries

def checkzip(zipcode):
	if zipcode in range(1000, 2792):
		url = "http://www.wcvb.com/weather/closings"
	elif zipcode in range(2801, 2941):
		url = "http://www.ribroadcasters.com/News_and_Events/Closings_Delays/"
	elif zipcode in range(3031, 3898):
		url = "http://www.wmur.com/weather/closings"
	elif zipcode in range(3901, 4883):
		url = 'http://www.wcsh6.com/closings'
	elif zipcode in range(5001, 5908):
		url = 'http://www.vpr.net/apps/school-closings/'
	elif zipcode in range(6001, 6929):
		url = 'http://www.nbcconnecticut.com/weather/school-closings/'
	elif zipcode in range(7001, 8990):
		url = 'http://nj1015.com/closings/'
	elif zipcode in range(10000, 14976):
		url = 'http://www.nbcnewyork.com/weather/school-closings/'
	elif zipcode in range(15000, 19641):
		url = 'http://www.nbcphiladelphia.com/weather/school-closings/'
	elif zipcode in range(19701, 19980):
		url = 'http://schoolclosings.delaware.gov/'
	elif zipcode in range(20001, 20100) or zipcode in range(20201, 20600) or zipcode in range(56901, 56973):
		url = 'http://www.nbcwashington.com/weather/school-closings/' #DC!
	elif zipcode in range(20101, 20200) or zipcode in range(22001, 24659):
		url = 'http://www.nbcwashington.com/weather/school-closings/'
	elif zipcode in range(20601, 21931):
		url = 'http://www.nbcwashington.com/weather/school-closings/'
	elif zipcode in range(24701, 26887):
		url = 'http://wvde.state.wv.us/closings/'
	elif zipcode in range(27006, 28910):
		url = 'http://www.wral.com/weather/closings/'
	elif zipcode in range(29001, 29946):
		url = 'http://www.wyff4.com/weather/closings'
	elif zipcode in range(30001, 32000) or zipcode in range(39813, 39902):
		url = 'http://www.wsbtv.com/weather/school-closings'
	elif zipcode in range(32003, 34998):
		url = 'fhttp://www.nbcmiami.com/weather/school-closings/'
	elif zipcode in range(35004, 36926):
		url = 'http://www.wbrc.com/category/224912/delays-and-closings'
	elif zipcode in range(37010, 38590):
		url = 'http://www.wsmv.com/category/211161/nashville-school-closings-snowbird-closings'
	elif zipcode in range(38601, 39777):
		url = 'http://www.wapt.com/weather/closings'
	elif zipcode in range(40003, 42789):
		url = 'http://www.wkyt.com/weather/closings'
	elif zipcode in range(43001, 45600):
		url = 'http://fox8.com/closings/'
	elif zipcode in range(46001, 47998):
		url = 'http://www.wthr.com/category/285877/indiana-weather-school-closings'
	elif zipcode in range(48001, 49972):
		url = 'mi'
	elif zipcode in range(50001, 52810):
		url = 'ia'
	elif zipcode in range(53001, 54991):
		url = 'wi'
	elif zipcode in range(55001, 56764):
		url = 'mn'
	elif zipcode in range(57001, 57800):
		url = 'sd'
	elif zipcode in range(58001, 58857):
		url = 'nd'
	elif zipcode in range(59001, 59938):
		url = 'mt'
	elif zipcode in range(60001, 63000):
		url = 'il'
	elif zipcode in range(63001, 65900):
		url = 'mo'
	elif zipcode in range(66002, 67955):
		url = 'ks'
	elif zipcode in range(68001, 69368):
		url = 'ne'
	elif zipcode in range(70001, 71498):
		url = 'la'
	elif zipcode in range(71601, 72960):
		url = 'ar'
	elif zipcode in range(73001, 74967):
		url = 'ok'
	elif zipcode in range(75001, 80000) or zipcode in range(88510, 88596):
		url = 'tx'
	elif zipcode in range(80001, 81659):
		url = 'co'
	elif zipcode in range(82001, 83129):
		url = 'wy'
	elif zipcode in range(83201, 83889):
		url = 'id'
	elif zipcode in range(84001, 84792):
		url = 'ut'
	elif zipcode in range(85001, 86557):
		url = 'az'
	elif zipcode in range(87001, 88442):
		url = 'nm'
	elif zipcode in range(88901, 89884):
		url = 'nv'
	elif zipcode in range(90001, 96163):
		url = 'ca'
	elif zipcode in range(96701, 96899):
		url = 'hi'
	elif zipcode in range(97001, 97921):
		url = 'or'
	elif zipcode in range(98001, 99403):
		url = 'wa'
	elif zipcode in range(99501, 99951):
		url = 'ak'
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