#!/usr/bin/env python
import os
import sys

for dirName,subdirList,fileList in os.walk("."):
    if dirName.count("Submission") > 0:
        os.chdir(dirName)
        fid=open('..\Feedback Attachment(s)\Feedback.txt', 'w') 
        sys.stdout = fid 
        print dirName
        print "Attempting H1P1.py"
        print ""
        try:
            execfile("H1P1.py")
        except IOError:
            print "Unable to open file H1P1.py"
        print "Attempting H1P2.py"
        print ""
        try:
            execfile("H1P2.py")
        except IOError:
            print "Unable to open file H1P2.py"

        print "\nH1P3.py was run manually with the test string 'The Ritz in the Pip'"
        print "Instructor Comments"
            
        fid.close()
        os.chdir("..\..")
