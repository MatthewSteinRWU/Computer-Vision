#!/usr/bin/env python
import os
import sys
import time
original=sys.stdout
for dirName,subdirList,fileList in os.walk("."):
    if dirName.count("Submission") > 0:
        os.chdir(dirName)
        fid=open('..\Feedback Attachment(s)\Feedback.txt', 'w')
        
        sys.stdout = fid 
        print dirName
        print "Attempting H3P1.py"
        print "Renamed files Hall01 02 03 -> 02 03 01"        
        print ""
        #try:

        os.rename('Hall01.jpg','temp.jpg')
        os.rename('Hall03.jpg','Hall01.jpg')
        os.rename('Hall02.jpg','Hall03.jpg')
        os.rename('temp.jpg','Hall02.jpg')
        sys.argv=['H3P1.py','Hall01.jpg']
        execfile("H3P1.py")
##        os.remove('..\Feedback Attachment(s)\H3P1Result01.jpg')
##        os.remove('..\Feedback Attachment(s)\H3P1Result02.jpg')
##        os.remove('..\Feedback Attachment(s)\H3P1Result03.jpg')
        os.rename('H3P1.jpg','..\Feedback Attachment(s)\H3P1Result01.jpg')
        sys.argv=['H3P1.py','Hall02.jpg']
        execfile("H3P1.py")
        os.rename('H3P1.jpg','..\Feedback Attachment(s)\H3P1Result02.jpg')
        sys.argv=['H3P1.py','Hall03.jpg']
        execfile("H3P1.py")
        os.rename('H3P1.jpg','..\Feedback Attachment(s)\H3P1Result03.jpg')            
        #except IOError:
        print "Unable to open file H3P1.py"
        #except AttributeError:
        print "Unable to open image file"            
        print "Instructor Comments:\n\n\n\n"
        print "Attempting H3P2.py"
        print ""
        try:
            sys.argv=['H3P2.py','Building01.jpg']
            execfile("H3P2.py")
        except IOError:
            print "Unable to open file H3P2.py"
        except AttributeError:
            print "Unable to open image file"            
        print "Instructor Comments:\n\n\n\n"
        print "Attempting H3P3.py"
        print ""
        try:
            execfile("H3P3.py")
        except IOError:
            print "Unable to open file H3P3.py"
        except AttributeError:
            print "Unable to open image file"                        
        print "Instructor Comments:\n\n\n\n"
        print "Score(Max 25)"


            
        fid.close()
        os.chdir("..\..")
    
sys.stdout=original
