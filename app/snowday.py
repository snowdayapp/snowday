#Main application file.
import zipcodecheck
import dictionaries
def main():
	print "Welcome to SnowDay, please type in your zipcode."
	zipcode = int(raw_input('> '))
	url, city = zipcodecheck.zipcodecheck(zipcode)
	

main()
