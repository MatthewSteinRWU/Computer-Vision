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
        print ""
        sys.path.append(".")
        try:
            print "Attempting H4P1.py Map01.jpg Map02.jpg"        
            sys.argv=['H4P1.py','Map01.jpg','Map02.jpg']
            execfile("H4P1.py")
            print "Attempting H4P1.py Map02.py Map01.jpg"        
            sys.argv=['H4P1.py','Map02.jpg','Map01.jpg']
            execfile("H4P1.py")

         
        except IOError:
            print "Unable to open file H4P1.py"
        except AttributeError:
            print "Unable to open image file"            
        print "Instructor Comments:\n\n\n\n"
        print ""
        print "Attempting H4P2.py Campus01.py Campus02.jpg"
        try:
            sys.argv=['H4P2.py','Campus01.jpg','Campus02.jpg']
            execfile("H4P2.py")
            print "Attempting H4P2.py Campus02.jpg Campus01.jpg"        
            sys.argv=['H4P2.py','Campus02.jpg','Campus01.jpg']
            execfile("H4P2.py")
        except IOError:
            print "Unable to open file H4P1.py"
        except AttributeError:
            print "Unable to open image file"  

        print "Instructor Comments:\n\n\n\n"
        print ""
        try:
            sys.argv=['H4P3.py','Campus03.jpg','Campus04.jpg']
            execfile("H4P3.py")
            print "Attempting H4P3.py Campus04.jpg Campus03.jpg"        
            sys.argv=['H4P2.py','Campus04.jpg','Campus03.jpg']
            execfile("H4P2.py")
        except IOError:
            print "Unable to open file H4P3.py"
        except AttributeError:
            print "Unable to open image file"  

            
        fid.close()
        os.chdir("..\..")
    
sys.stdout=original
