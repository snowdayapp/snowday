#Snow Day Application

## Functionalities:
* Notifiy user of delay, cancelation, etc
** Input of zipcode
** Parses html file of news station to check for cancalations every 10 minutes
** Returns "No cancelations yet every hour for 24 hours, if snow is in forecast."
** Returns cancelation type upon confirmation.
* Snow Day Calculator
** Uses zipcode
** Uses snow day history
* Store local snow day history
** Probably in an python dictionary.

## Functions:
* start() - Main screen
* about() - About screen
* zipcode() - Enter zipcode input
* calculator() - snow day calculator
* history() - Shows snow day history
* check() - updates cancellation list.

## Variables/type:
* zipcode/integer - User's ZIP
* notifications/booleen - if notifications are on or not.
* cancellations/list - List of cancellations
