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

#need to determine if playing offense or defense
def determineStrategy():
	
	ORow = sorted(ORow, key = lambda x: len(x), reverse=True)
	YRow = sorted(YRow, key = lambda x: len(x), reverse=True)
	OColumn = sorted(OColumn, key = lambda x: len(x), reverse=True)
	YColumn = sorted(YColumn, key = lambda x: len(x), reverse=True)
	ODiagonal = sorted(ODiagonal, key = lambda x: len(x), reverse=True)
	YDiagonal = sorted(YDiagonal, key = lambda x: len(x), reverse=True)
	OScore = []
	OScore.append(ORow[0])
	OScore.append(OColumn[0])
	OScore.append(ODiagonal[0])
	OScore = sorted(OScore, key = lambda x: x, reverse=True)


	YScore = []
	YScore.append(YRow[0])
	YScore.append(YColumn[0])
	YScore.append(YDiagonal[0])
	YScore = sorted(YScore, key = lambda x: x, reverse=True)

	if OScore[0]> YScore[0]:
		return "Defense"
	elif OScore[0] < YScore[0]:
		return "Offense"
	elif OScore[0] == YScore[0]:
		return "Offense"
		
#make a list of all the empty nodes touching desired teams pieces	
def getEmptyList():
	strategy = determineStrategy()
	emptyNodes = []
	if strategy == "Offense":
		for i in ORow:
			for j in i:
				if Gameboard[i.row+1][i.column]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column])
					
				elif Gameboard[i.row-1][i.column] ==0:
					emptyNodes.append(Gameboard[i.row-1][i.column]) 
					
				elif Gameboard[i.row][i.column+1] ==0:
					emptyNodes.append(Gameboard[i.row][i.column+1])
					
				elif Gameboard[i.row][i.column-1] ==0:
					emptyNodes.append(Gameboard[i.row][i.column-1])
					
				elif Gameboard[i.row+1][i.column+1]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column+1])
					
				elif Gameboard[i.row-1][i.column-1]==0:
					emptyNodes.append(Gameboard[i.row-1][i.column-1])
					
				elif Gameboard[i.row-1][i.column+1]==0:
					emptyNodes.append(Gameboard[i.row-1][i.column+1])
					
				elif Gameboard[i.row+1][i.column-1]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column-1])

		for i in OColumn:
			for j in i:
				if Gameboard[i.row+1][i.column]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column])
					
				elif Gameboard[i.row-1][i.column] ==0:
					emptyNodes.append(Gameboard[i.row-1][i.column]) 
					
				elif Gameboard[i.row][i.column+1] ==0:
					emptyNodes.append(Gameboard[i.row][i.column+1])
					
				elif Gameboard[i.row][i.column-1] ==0:
					emptyNodes.append(Gameboard[i.row][i.column-1])
					
				elif Gameboard[i.row+1][i.column+1]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column+1])
					
				elif Gameboard[i.row-1][i.column-1]==0:
					emptyNodes.append(Gameboard[i.row-1][i.column-1])
					
				elif Gameboard[i.row-1][i.column+1]==0:
					emptyNodes.append(Gameboard[i.row-1][i.column+1])
					
				elif Gameboard[i.row+1][i.column-1]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column-1])
		for i in ODiagonal:
			for j in i:
				if Gameboard[i.row+1][i.column]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column])
					
				elif Gameboard[i.row-1][i.column] ==0:
					emptyNodes.append(Gameboard[i.row-1][i.column]) 
					
				elif Gameboard[i.row][i.column+1] ==0:
					emptyNodes.append(Gameboard[i.row][i.column+1])
					
				elif Gameboard[i.row][i.column-1] ==0:
					emptyNodes.append(Gameboard[i.row][i.column-1])
					
				elif Gameboard[i.row+1][i.column+1]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column+1])
					
				elif Gameboard[i.row-1][i.column-1]==0:
					emptyNodes.append(Gameboard[i.row-1][i.column-1])
					
				elif Gameboard[i.row-1][i.column+1]==0:
					emptyNodes.append(Gameboard[i.row-1][i.column+1])
					
				elif Gameboard[i.row+1][i.column-1]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column-1])
	if strategy == "Defense":
		for i in YRow:
			for j in i:
				if Gameboard[i.row+1][i.column]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column])
					
				elif Gameboard[i.row-1][i.column] ==0:
					emptyNodes.append(Gameboard[i.row-1][i.column]) 
					
				elif Gameboard[i.row][i.column+1] ==0:
					emptyNodes.append(Gameboard[i.row][i.column+1])
					
				elif Gameboard[i.row][i.column-1] ==0:
					emptyNodes.append(Gameboard[i.row][i.column-1])
					
				elif Gameboard[i.row+1][i.column+1]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column+1])
					
				elif Gameboard[i.row-1][i.column-1]==0:
					emptyNodes.append(Gameboard[i.row-1][i.column-1])
					
				elif Gameboard[i.row-1][i.column+1]==0:
					emptyNodes.append(Gameboard[i.row-1][i.column+1])
					
				elif Gameboard[i.row+1][i.column-1]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column-1])

		for i in YColumn:
			for j in i:
				if Gameboard[i.row+1][i.column]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column])
					
				elif Gameboard[i.row-1][i.column] ==0:
					emptyNodes.append(Gameboard[i.row-1][i.column]) 
					
				elif Gameboard[i.row][i.column+1] ==0:
					emptyNodes.append(Gameboard[i.row][i.column+1])
					
				elif Gameboard[i.row][i.column-1] ==0:
					emptyNodes.append(Gameboard[i.row][i.column-1])
					
				elif Gameboard[i.row+1][i.column+1]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column+1])
					
				elif Gameboard[i.row-1][i.column-1]==0:
					emptyNodes.append(Gameboard[i.row-1][i.column-1])
					
				elif Gameboard[i.row-1][i.column+1]==0:
					emptyNodes.append(Gameboard[i.row-1][i.column+1])
					
				elif Gameboard[i.row+1][i.column-1]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column-1])
		for i in YDiagonal:
			for j in i:
				if Gameboard[i.row+1][i.column]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column])
					
				elif Gameboard[i.row-1][i.column] ==0:
					emptyNodes.append(Gameboard[i.row-1][i.column]) 
					
				elif Gameboard[i.row][i.column+1] ==0:
					emptyNodes.append(Gameboard[i.row][i.column+1])
					
				elif Gameboard[i.row][i.column-1] ==0:
					emptyNodes.append(Gameboard[i.row][i.column-1])
					
				elif Gameboard[i.row+1][i.column+1]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column+1])
					
				elif Gameboard[i.row-1][i.column-1]==0:
					emptyNodes.append(Gameboard[i.row-1][i.column-1])
					
				elif Gameboard[i.row-1][i.column+1]==0:
					emptyNodes.append(Gameboard[i.row-1][i.column+1])
					
				elif Gameboard[i.row+1][i.column-1]==0:
					emptyNodes.append(Gameboard[i.row+1][i.column-1])	
def minimax():	
	#use iterative deepening search to do give each one a heuristic
	#use assignHeuristic
	#do mini max using those heuristics
	#prune out the bad ones with alpha beta

#once you have the move youre doing figure out again 
#which rows/columns/diagonals it goes in and add it to that

# print out answer
