#Created 14 September 2017

import os
import numpy as np
import collections


class FakePiece:
    def __init__(self,value,row, column, types,parent):
        self.value = value
        self.types= types    # an int
        self.full = []
        self.empty = []
        self.parent =parent    # a list of nodes
        self.row = row
        self.column  = column

    def addFull(self, childNode):
		self.full.append(childNode)	

    def addEmpty(self, childNode):
		self.empty.append(childNode)		

class GamePiece:
    def __init__(self,value,row, column, types,parent):
        self.value = value
        self.parent = parent
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
global fakeList
fakeList = []
global GameBoard
#GameBoard = np.zeros([15,15], dtype = object)
GameBoard = []                                                        
for i in range (0, 16):                               
    new = []                 
    for j in range (0, 16):          
        new.append(GamePiece(0,i,j,"E",None))             
    GameBoard.append(new)
#print(GameBoard)
#for i in GameBoard:
	#if i.all() == 0:
		#i = GamePiece(0,i.rows,i.column,"E",None)
#rows = 15
#columns = 15


#while length < 15:
	#gameColumn.append(GamePiece(0,length,0,"E",None))
	#length = length +1
#GameBoard = []
#length = 0
#while length < 15:
	#for i in gameColumn:
		#i.column = length
	#GameBoard.append(gameColumn)
	#length = length +1
#print(matrix)

    #print(end="\n")
    
global opponentMoves
opponentMoves = []
#global myMoves
#myMoves = []
###Boolean Function to check if My Turn###
f = open("move_file.txt")
def isMyTurn():
  global GameBoard
  global matrix
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
	if row == "E":
		row = 5		
	f.read(1)
	column = f.read(1)
	
	
	#GameBoard[row][column] = GamePiece(0,row,column,"O")
	#print(GameBoard)
	#print(row,column)
	f.readline(1)
	f.readline(1)
	GameBoard[int(row)][int(column)] = GamePiece(0,row,column,"O",None)
	##adds new piece to gameboard####
	
	#newPiece(row,column,"O")
	opponentMoves.append(GameBoard[int(row)][int(column)])
def setHeuristic(l):
	for i in l:
		if i.row == i.parent.row:
			#print("TWO")
			#i.value = i.value + 2
			if i.parent.row == i.parent.parent.row:
				#print("THREE")
				#i.value = i.value + 3
				if i.parent.parent.row == i.parent.parent.parent.row:
					#print("FOUR")
					#i.value = i.value + 4
					if i.parent.parent.parent.row == i.parent.parent.parent.parent.row:
						#print("FIVE")
						i.value = i.value + 5
		#print(i.row,i.column,i.parent)
	
	for i in l:
		if i.column == i.parent.column:
			#print("TWO")
			if i.parent.column == i.parent.parent.column:
				#print("THREE")
				if i.parent.parent.column == i.parent.parent.parent.column:
					#print("FOUR")
					if i.parent.parent.parent.column == i.parent.parent.parent.parent.column:
						#print("FIVE")
						i.value = 5
		#print(i.row,i.column,i.parent)	
def checkEmpty(l,l2):
	global fakeList
	global e
	global opponentMoves
	
	for i in l:
		#print("___")
		#print(GameBoard[int(i.row)][int(i.column)].row ,GameBoard[int(i.row)][int(i.column)].column)
		#if GameBoard[int(i.row)][int(i.column)].row == if GameBoard[int(i.row)-1][int(i.column)].row == :
			
			
			
		if GameBoard[int(i.row)][int(i.column)].row != 15:
			if GameBoard[int(i.row)+1][int(i.column)].types == "E":
				#print("Right")
				#print(GameBoard[int(i.row)+1][int(i.column)].row,GameBoard[int(i.row)+1][int(i.column)].column)
				GameBoard[int(i.row)+1][int(i.column)].parent = GameBoard[int(i.row)][int(i.column)]
				l2.append(GameBoard[int(i.row)+1][int(i.column)])		

		if GameBoard[int(i.row)][int(i.column)].column != 15:					
			if GameBoard[int(i.row)][int(i.column)+1].types == "E":
				#print("UP")
				#print(GameBoard[int(i.row)][int(i.column)+1].row,GameBoard[int(i.row)][int(i.column)+1].column)
				GameBoard[int(i.row)][int(i.column)+1].parent = GameBoard[int(i.row)][int(i.column)]
				l2.append(GameBoard[int(i.row)][int(i.column)+1])	
				
		if GameBoard[int(i.row)][int(i.column)].row != 0:	
			if GameBoard[int(i.row)-1][int(i.column)].types == "E":
				#print("LEFT")
				#print(GameBoard[int(i.row)-1][int(i.column)].row,GameBoard[int(i.row)-1][int(i.column)].column)
				GameBoard[int(i.row)-1][int(i.column)].parent = GameBoard[int(i.row)][int(i.column)]
				l2.append(GameBoard[int(i.row)-1][int(i.column)])
						
		if GameBoard[int(i.row)][int(i.column)].row != 0:								
			if GameBoard[int(i.row)][int(i.column)-1].types == "E":
				l2.append(GameBoard[int(i.row)][int(i.column)-1])	
				GameBoard[int(i.row)][int(i.column)-1].parent = GameBoard[int(i.row)][int(i.column)]
				#print("DOWN")
				#print(GameBoard[int(i.row)][int(i.column)-1].row,GameBoard[int(i.row)][int(i.column)-1].column)
		if GameBoard[int(i.row)][int(i.column)].row  == 4 and GameBoard[int(i.row)][int(i.column)].column == 15:
			e = 1

global newList
newList = []	
global otherList
otherList = []	
global bestList
bestList = []
global e
e = 0
global listType
listType = ""	
def makeTree():
	global opponentMoves
	global fakeList
	global e
	global newList
	global bestList
	global otherList
	checkEmpty(opponentMoves,fakeList)
	#print("FAKELIST")
	newList = []
	otherList = []
	checkEmpty(fakeList, newList)
	fakeList = []
	checkEmpty(newList,fakeList)
	newList = []
	checkEmpty(fakeList,newList)
	fakeList = []
	while e != 1:
		for i in newList:
			if i.value == 5:
				otherList.append(i)
				newList.remove(i)
			if not newList:
				e = 1
		checkEmpty(fakeList,newList)
		checkEmpty(newList,fakeList)
		bestList = fakeList
		newList =[]
		setHeuristic(fakeList)
		listType = "NEWLIST"
		for i in fakeList:
			if i.value == 5:
				otherList.append(i)
				fakeList.remove(i)	
			if not fakeList:
				e=1
		checkEmpty(fakeList,newList)
		bestList = newList
		fakeList = []
		listType = "FAKELIST"
global final 
final = []		
def minimax():
	global final
	global bestList
	global otherList
	final = []	
	for i in otherList:
		#print(i.value)
		bestList.append(i)
	#for i in bestList:
		#print(i.value)
	bestList = sorted(bestList, key = lambda x: x.parent.row, reverse=False	)
	bestList = sorted(bestList, key = lambda x: x.parent.column, reverse=False	)

	trashList = []
	for i in bestList:
		trashList.append(i.parent)
		
	newest = set(trashList)
	for i in bestList:
		placeHolder = []
		for k in newest:
			if i.parent.row == k.row and k.column == i.parent.column:
				placeHolder.append(i)
		final.append(placeHolder)
		placeHolder = []
	for i in final:
		i = sorted(i, key = lambda x: x.value, reverse=False)

	findMin()
global minList
minList = []
def findMin():
	minList = []
	global final
	smallest = 0
	for i in final:
		for j in i:
			if j.value == smallest:
				minList.append(j)
	for i in minList:
		i.parent.value = smallest
	bestList = minList

def findMax():
	global final
	maxList = []
	largest = 5
	for i in final:
		for j in i:
			if j.value == largest:
				maxList.append(j)
	for i in maxList:
		i.parent.value = largest	
	bestList = maxList
def main():
	global myMoves
	
	global GameBoard
	global last
	global opponentMoves
	isMyTurn()
	makeTree()
	minimax()

if __name__ == "__main__":
	main()		

