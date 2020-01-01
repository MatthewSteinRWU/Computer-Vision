#!/usr/bin/env python
# User interaction demo
# Get a string from the user and raise it up UPPERCASE

usrString = ""
while len(usrString)< 10:
    print "Please enter a string between 10 and 30 characters"
    usrString = raw_input("-->")
    if len(usrString) < 10:
        print "Sorry, that is less than 10 characters"

print usrString.upper()
