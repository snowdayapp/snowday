#Main application file.
from zipcodecheck import zipcodecheck
import dictionaries
def main():
	print "Welcome to SnowDay, please type in your zipcode."
	zipcode = int(raw_input('> '))
	zipcodecheck(zipcode)

main()