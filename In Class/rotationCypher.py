#!/usr/bin/env python
# Perform a rotation cypher on a string

usrString = "The Ritz in the Pip"
outString = ""


for i in range(len(usrString)):
    outString+=(chr(ord(usrString[i])+1))

    

print outString
    
