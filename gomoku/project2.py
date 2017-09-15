import os

def isMyTurn():

	#fileExistsBool = 

	if (os.path.isfile('./file.txt')):	# if groupname.txt exists
		print "my turn"	# it is my turn
	else:
		print "not my turn"	# it is not my turn

