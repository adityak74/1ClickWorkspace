#!/usr/bin/python
import os
import pickle

class Workspace:

	def __init__(self,path,metaData):
		self.path = path
		self.metaData = metaData

	def displayWorkspace(self):
		print "Path : ", self.path, ", Meta-Data : ", self.metaData


#w1 = Workspace("/opt/lampp","TestData")
#w1.displayWorkspace()

workspaceList = []

def saveWorkspaceItems(itemsList):
	no_of_items = len(itemsList)
	try:
		if no_of_items is 0:
			print "No list items"
			return -1
		else:
			pickle.dump( workspaceList , open( 'TempWorkingListSaveFile.p' , "wb" ) )
			print "Saved."
	except Exception, e:
		raise e

def retrieveWorkingItems():
	workspaceList = pickle.load( open( "TempWorkingListSaveFile.p" , "rb" ) )
	return workspaceList

#Test entries for checking the module
#workspaceList.append(Workspace("/opt/lampp","TestData1"))
#workspaceList.append(Workspace("/opt/lampp/htdocs","TestData2"))
#workspaceList.append(Workspace("/home","TestData3"))

#for item in workspaceList:
#		print "Path : %s -> Data : %s" % (item.path,item.metaData)

#retrieveWorkingItems() //For retrieving the items with the data
#saveWorkspaceItems(workspaceList) //Passing the working list for saving it with the metadata
