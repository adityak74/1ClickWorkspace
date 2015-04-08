import os
import pickle

def saveWorkspaceList(workspaceList):
	workspaceListLen =  len(workspaceList)
	try:
		if workspaceListLen is 0:
			print "No list items"
			return -1
		else:
			pickle.dump( workspaceList , open( 'WorkingListSaveFile.p' , "wb" ) )
	except Exception, e:
		raise e
	

def loadWorkingList():
	try:
		workspaceList = pickle.load( open( "WorkingListSaveFile.p" , "rb" ) )
		return workspaceList
	except Exception, e:
		return -1
	
	

