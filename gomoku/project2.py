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



#class for pieces#



class GamePiece:
    def __init__(self,value,row, column):
        self.value = value    # an int
        self.children = []    # a list of nodes
        self.row = row
        self.column  = column

    def addChild(self, childNode):
		self.children.append(childNode)	
		
#class for pieces in a row/column/diagonal#
class ConnectedPieces:
    def __init__(self, starterNode):
        self.starterNode = starterNode    
        self.connected= []
        self.connected.append(starterNode)
 

    def addNewNode(self, node):
		self.connected.append(node)
		
#list of oppenents rows		
class ORow:
    def __init__(self, connected):
        self.connected = connected   
        self.ORow = []
    

    def addORow(self, connected):
		self.ORow.append(connected)
		
#list of your rows		
class YRow:
    def __init__(self, connected):
        self.connected = connected    
        self.YRow = []
   
    def addYRow(self, connected):
		self.YRow.append(connected)
		
class OColumn:
    def __init__(self, connected):
        self.connected = connected    
        self.OColumn = []
    

    def addOColumn(self, connected):
		self.OColumn.append(connected)
		
class YColumn:
    def __init__(self, connected):
        self.connected = connected   
        self.YColumn = []
    

    def addORow(self, connected):
		self.YColumn.append(connected)
		
class ODiagonal:
    def __init__(self, connected):
        self.connected = connected   
        self.ODiagonal = []
   

    def addODiagonal(self, connected):
		self.ODiagonal.append(connected)
		
class YDiagonal:
    def __init__(self, connected):
        self.connected = connected 
        self.YDiagonal = []


    def addYDiagona(self, connected):
		self.YDiagonal.append(connected)
		
#game board 15x15 array#
def makeGame():
	w,h = 15,15
	GameBoard = [[0 for x in range(w)] for y in range(h)]	
					
#function that assigns a heuristic value to pieces#

def assignHeuristic(strategy, gamepiece):
	
	if strategy == "offense":
		for i in YRow:
			if i[0].column - 1 == gamepiece.column:
				if i[0].row == gamepiece.row:
					if GameBoard[gamepiece.row][gamepiece.column] == 0:
						gamepiece.value = gamepiece.value + len(i)
			elif i[len(i)].column == gamepiece.column:
				if i[0].row == gamepiece.row:
					if GameBoard[gamepiece.row][gamepiece.column] == 0:
						gamepiece.value = gamepiece.value + len(i)					
			
		
		for i in YColumn:
			if i[0].row - 1 == gamepiece.row:
				if i[0].column == gamepiece.column:
					if GameBoard[gamepiece.row][gamepiece.column] == 0:
						gamepiece.value = gamepiece.value + len(i)
			elif i[len(i)].row == gamepiece.row:
				if i[0].column == gamepiece.column:
					if GameBoard[gamepiece.row][gamepiece.column] == 0:
						gamepiece.value = gamepiece.value + len(i)				
			
		for i in YDiagonal:
			if i[0].row - 1 == gamepiece.row:
				if i[0].column-1 == gamepiece.column:
					if GameBoard[gamepiece.row][gamepiece.column] == 0:
						gamepiece.value = gamepiece.value + len(i)
			elif i[len(i)].row == gamepiece.row:
				if i[len(i)].column == gamepiece.column:
					if GameBoard[gamepiece.row][gamepiece.column] == 0:
						gamepiece.value = gamepiece.value + len(i)	
										
	elif strategy == "defense":
		for i in ORow:
			if i[0].column - 1 == gamepiece.column:
				if i[0].row == gamepiece.row:
					if GameBoard[gamepiece.row][gamepiece.column] == 0:
						gamepiece.value = gamepiece.value + len(i)
			elif i[len(i)].column == gamepiece.column:
				if i[0].row == gamepiece.row:
					if GameBoard[gamepiece.row][gamepiece.column] == 0:
						gamepiece.value = gamepiece.value + len(i)	
								
		for i in OColumn:
			if i[0].row - 1 == gamepiece.row:
				if i[0].column == gamepiece.column:
					if GameBoard[gamepiece.row][gamepiece.column] == 0:
						gamepiece.value = gamepiece.value + len(i)
			elif i[len(i)].row == gamepiece.row:
				if i[0].column == gamepiece.column:
					if GameBoard[gamepiece.row][gamepiece.column] == 0:
						gamepiece.value = gamepiece.value + len(i)					
		for i in ODiagonal:		
			if i[0].row - 1 == gamepiece.row:
				if i[0].column-1 == gamepiece.column:
					if GameBoard[gamepiece.row][gamepiece.column] == 0:
						gamepiece.value = gamepiece.value + len(i)
			elif i[len(i)].row == gamepiece.row:
				if i[len(i)].column == gamepiece.column:
					if GameBoard[gamepiece.row][gamepiece.column] == 0:
						gamepiece.value = gamepiece.value + len(i)	
#minimax

#alpha beta pruning
