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
class path:
	def __init__(self, goalNode):
		self.goalNode = goalNode
		self.pathQ = []
		
		self.totalPath = 0
		
	def add_node(self, nodes):
		self.pathQ.append(nodes)
	def setTotal(self, totalPath):
		self.totalPath = totalPath
	def add_node2(self, nodes):
		self.pathQ.insert(0,nodes)

		
#game board 15x15 array#



GameBoard = np.zeros([15,15], dtype = object)

opponentMoves = []

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
	
	newPiece(row,column,"O")
	
	
	f.readline(1)
	f.readline(1)
	opponentMoves.append(GameBoard[int(row)][int(column)])
	#print("EMPTY")
	#for i in GameBoard[int(row)][int(column)].empty:
		#print(i)
			
	#print("FULL")
	#for i in GameBoard[int(row)][int(column)].full:
		#print(i)

def newPiece(row,column,types):
	#row
	GameBoard[int(row)][int(column)] = GamePiece(0,row,column,types)
	
	if GameBoard[int(row)+1][int(column)] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)+1][int(column)])
		
	if GameBoard[int(row)+1][int(column)] == 0:
		GameBoard[int(row)+1][int(column)] = GamePiece(0,row+1,column,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)+1][int(column)])


		
	if GameBoard[int(row)-1][int(column)] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)-1][int(column)])
		
	if GameBoard[int(row)-1][int(column)] == 0:
		GameBoard[int(row)-1][int(column)] = GamePiece(0,row-1,column,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)-1][int(column)])

	#column	
	if GameBoard[int(row)][int(column)+1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)][int(column)+1])
					
	if GameBoard[int(row)][int(column)+1] == 0:
		GameBoard[int(row)][int(column)+1] = GamePiece(0,row,int(column)+1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)][int(column)+1])


	if GameBoard[int(row)][int(column)-1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)][int(column)-1])
		
	if GameBoard[int(row)][int(column)-1] == 0:
		GameBoard[int(row)][int(column)-1] = GamePiece(0,row,int(column)-1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)][int(column)-1])


	#diagonal	
	if GameBoard[int(row)+1][int(column)+1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)+1][int(column)+1])
		
	if GameBoard[int(row)+1][int(column)+1] == 0:
		GameBoard[int(row)+1][int(column)+1] = GamePiece(0,row+1,int(column)+1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)+1][int(column)+1])


		
	if GameBoard[int(row)+1][int(column)-1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)+1][int(column)-1])
		
	if GameBoard[int(row)+1][int(column)-1] == 0:
		GameBoard[int(row)+1][int(column)-1] = GamePiece(0,row+1,int(column)-1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)+1][int(column)-1])


		
	if GameBoard[int(row)-1][int(column)+1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)-1][int(column)+1])
		
	if GameBoard[int(row)-1][int(column)+1] == 0:
		GameBoard[int(row)-1][int(column)+1] = GamePiece(0,row-1,int(column)+1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)-1][int(column)+1])

		
	if GameBoard[int(row)-1][int(column)-1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)-1][int(column)-1])
		
	if GameBoard[int(row)-1][int(column)-1] == 0:
		GameBoard[int(row)-1][int(column)-1] = GamePiece(0,row-1,int(column)-1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)-1][int(column)-1])			

global deepness
deepness = 0
global emptyNodes
global placeHolder
def IDS():
	global deepness
	global emptyNodes
	global placeHolder
	if deepness == 0:
		newPath = path("G")
		newPath.add_node(opponentMoves[0])
		emptyNodes = []
		emptyNodes.append(newPath)
		placeHolder = []
	for i in emptyNodes:
		
		for j in i.pathQ[0].empty:
			newPath = path("G")
			for u in i.pathQ:
				newPath.add_node(u)
			newPath.add_node2(j)
			newPiece(j.row,j.column,"F")
			placeHolder.append(newPath)
	deepness = deepness +1	
	if deepness < 6:
		IDS()
	else:
		print("END")
		

					
#need to do iterative deepening search for each of the empty nodes
#iterate like 6 times
#then assign heuristic to botton postion
#then minimax back up to find next move
#then print out that move and start again
def main():
	isMyTurn()
	IDS()
	

if __name__ == "__main__":
	main()		

