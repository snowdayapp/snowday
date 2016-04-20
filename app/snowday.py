#Main application file.
import zipcodecheck
import dictionaries
def main():
	print "Welcome to SnowDay, please type in your zipcode."
	inputzipcode = int(raw_input('> '))
	url, city = zipcodecheck.checkzip(inputzipcode)
	

main()
