#!/usr/bin/env python
import os
import sys
original=sys.stdout
for dirName,subdirList,fileList in os.walk("."):
    if dirName.count("Submission") > 0:
        os.chdir(dirName)
        fid=open('..\Feedback Attachment(s)\Feedback.txt', 'w')
        
        sys.stdout = fid 
        print dirName
        print "Attempting H2P1.py"
        print ""
        try:
            execfile("H2P1.py")
        except IOError:
            print "Unable to open file H2P1.py"
        except AttributeError:
            print "Unable to open image file"            
        print "Instructor Comments:\n\n\n\n"
        print "Attempting H2P2.py"
        print ""
        try:
            execfile("H2P2.py")
        except IOError:
            print "Unable to open file H2P2.py"
        except AttributeError:
            print "Unable to open image file"            
        print "Instructor Comments:\n\n\n\n"
        print "Attempting H2P3.py"
        print ""
        try:
            execfile("H2P3.py")
        except IOError:
            print "Unable to open file H2P3.py"
        except AttributeError:
            print "Unable to open image file"                        
        print "Instructor Comments:\n\n\n\n"
        print "Attempting H2P4.py"
        print ""
        try:
            execfile("H2P4.py")
        except IOError:
            print "Unable to open file H2P4.py"
        except ImportError:
            print "H2P4.py imports a library that is not found"
        except AttributeError:
            print "Unable to open image file"                        
           
        print "Instructor Comments:\n\n\n\n"
        print "Score(Max 25)"


            
        fid.close()
        os.chdir("..\..")
    
sys.stdout=original
