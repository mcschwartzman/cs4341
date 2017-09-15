#Created 14 September 2017

import os


###Boolean Function to check if My Turn###
def isMyTurn():

  fileExistsBool = os.path.isfile('./file.txt')

  if (fileExistsBool):  # if groupname.txt exists
    print "my turn" # it is my turn
  else:
    print "not my turn" # it is not my turn

  print fileExistsBool
  return fileExistsBool


isMyTurn()