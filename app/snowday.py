#Main application file.
import zipcodecheck as zipcodefile
import dictionaries
def main():
	print "Welcome to SnowDay, please type in your zipcode."
	inputzipcode = int(raw_input('> '))
	url, city = zipcodefile.checkzip(inputzipcode)
	return url, city
	

main()
