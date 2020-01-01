#!/usr/bin/env python
# User interaction demo
# Get a string from the user and raise it up UPPERCASE

usrString = ""
outString = ""

while len(usrString)< 10:
    print "Please enter a string between 10 and 30 characters"
    usrString = raw_input("-->")
    if len(usrString) < 10:
        print "Sorry, that is less than 10 characters"
    if len(usrString) > 30:
        print "String too long, only using first 30 characters"

#print usrString.upper()
for i in range(len(usrString)):
    if usrString[i] >= 'a' and usrString[i] <= 'z':
        outString+=(chr(ord(usrString[i])-32))
    else:
        outString+=usrString[i]
    

print outString
    
