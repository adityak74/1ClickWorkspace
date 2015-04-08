import os
import pickle

def saveWorkspaceList(workspaceList):
	pickle.dump( workspaceList , open( 'WorkingListSaveFile.p' , "wb" ) )

def loadWorkingList():
	try:
		workspaceList = pickle.load( open( "WorkingListSaveFile.p" , "rb" ) )
		return workspaceList
	except Exception, e:
		return -1
	
	

