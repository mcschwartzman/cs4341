#Created 14 September 2017

import os
import numpy as np





class GamePiece:
    def __init__(self,value,row, column, types):
        self.value = value
        self.types= types    # an int
        self.full = []
        self.empty = []     # a list of nodes
        self.row = row
        self.column  = column

    def addFull(self, childNode):
		self.full.append(childNode)	

    def addEmpty(self, childNode):
		self.empty.append(childNode)	
				
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



GameBoard = np.zeros([15,15], dtype = object)


###Boolean Function to check if My Turn###
f = open("move_file.txt")
def isMyTurn():

  fileExistsBool = os.path.isfile('./file.txt')

  if (fileExistsBool):


	
	i=f.read(1)
	
	while i != " ":
	
		i=f.read(1)
	row = f.read(1)
	if row == "A":
		row = 1
	if row == "B":
		row = 2
	if row == "C":
		row = 3
	if row == "D":
		row = 4
		
	f.read(1)
	column = f.read(1)
	
	GameBoard[int(row)][int(column)] = GamePiece(0,row,column,"O")
	#row
	if GameBoard[int(row)+1][int(column)] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)+1][int(column)])
		
	if GameBoard[int(row)+1][int(column)] == 0:
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)+1][int(column)])
		
	if GameBoard[int(row)-1][int(column)] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)-1][int(column)])
		
	if GameBoard[int(row)-1][int(column)] == 0:
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)-1][int(column)])
	#column	
	if GameBoard[int(row)][int(column)+1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)][int(column)+1])
			
		
	if GameBoard[int(row)][int(column)+1] == 0:
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)][int(column)+1])
		
	if GameBoard[int(row)][int(column)-1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)][int(column)-1])
		
	if GameBoard[int(row)][int(column)-1] == 0:
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)][int(column)-1])
	#diagonal	
	if GameBoard[int(row)+1][int(column)+1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)+1][int(column)+1])
		
	if GameBoard[int(row)+1][int(column)+1] == 0:
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)+1][int(column)+1])
		
	if GameBoard[int(row)+1][int(column)-1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)+1][int(column)-1])
		
	if GameBoard[int(row)+1][int(column)-1] == 0:
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)+1][int(column)-1])
		
	if GameBoard[int(row)-1][int(column)+1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)-1][int(column)+1])
		
	if GameBoard[int(row)-1][int(column)+1] == 0:
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)-1][int(column)+1])
		
	if GameBoard[int(row)-1][int(column)-1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)-1][int(column)-1])
		
	if GameBoard[int(row)-1][int(column)-1] == 0:
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)-1][int(column)-1])
	f.readline(1)
	f.readline(1)
	#print("EMPTY")
	#for i in GameBoard[int(row)][int(column)].empty:
		#print(i)
			
	#print("FULL")
	#for i in GameBoard[int(row)][int(column)].full:
		#print(i)
			

				
isMyTurn()
		

#class for pieces#					
#function that assigns a heuristic value to pieces#

	#use iterative deepening search to do give each one a heuristic
	#use assignHeuristic
	#do mini max using those heuristics
	#prune out the bad ones with alpha beta

#once you have the move youre doing figure out again 
#which rows/columns/diagonals it goes in and add it to that

# print out answer
