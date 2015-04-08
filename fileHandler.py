from Tkinter import *
import os,sys

def getDirectoryList(value=None):
    if value is None:
    	value = os.getcwd()
    	path = value
    	#print path
    else:
    	path = os.path.abspath(value)
    	#print path
    dirs = os.listdir(path)
    #print dirs
    #dirs = sorted(dirs)
    #print dirs
    for file in dirs:
    	if(os.path.isdir(path + "/" + file)):
    		print file
    	

#Testing the function by passing params
#getDirectoryList("/opt/lampp/htdocs/")
