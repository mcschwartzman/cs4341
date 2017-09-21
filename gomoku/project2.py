#Created 14 September 2017

import os
import numpy as np
import collections


class FakePiece:
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
global fakeList
fakeList = []
global GameBoard
GameBoard = np.zeros([15,15], dtype = object)
global opponentMoves
opponentMoves = []
global myMoves
myMoves = []
###Boolean Function to check if My Turn###
f = open("move_file.txt")
def isMyTurn():
  global GameBoard
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
	newPiece(row,column,"O")
	opponentMoves.append(GameBoard[int(row)][int(column)])
	
	#print("EMPTY")
	#for i in GameBoard[int(row)][int(column)].empty:
		#print(i.row,i.column)
			
	#print("FULL")
	#for i in GameBoard[int(row)][int(column)].full:
		#print(i.row,i.column)

def newPiece(row,column,types):
	global GameBoard
	global fakeList
	#row

	GameBoard[int(row)][int(column)] = GamePiece(0,row,column,types)

	
	if GameBoard[int(row)+1][int(column)] != 0 and GameBoard[int(row)+1][int(column)].types != "F":
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)+1][int(column)])
		
		
	if GameBoard[int(row)+1][int(column)] == 0:
		GameBoard[int(row)+1][int(column)] = FakePiece(0,row+1,column,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)+1][int(column)])
	

		
	if GameBoard[int(row)-1][int(column)] != 0 and GameBoard[int(row)-1][int(column)] != "F":
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)-1][int(column)])
		
	if GameBoard[int(row)-1][int(column)] == 0:
		GameBoard[int(row)-1][int(column)] = FakePiece(0,row-1,column,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)-1][int(column)])

	#column	
	if GameBoard[int(row)][int(column)+1] != 0 and GameBoard[int(row)][int(column)+1] != "F":
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)][int(column)+1])
					
	if GameBoard[int(row)][int(column)+1] == 0:
		GameBoard[int(row)][int(column)+1] = FakePiece(0,row,int(column)+1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)][int(column)+1])


	if GameBoard[int(row)][int(column)-1] != 0 and GameBoard[int(row)][int(column)-1] != "F":
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)][int(column)-1])
		
	if GameBoard[int(row)][int(column)-1] == 0:
		GameBoard[int(row)][int(column)-1] = FakePiece(0,row,int(column)-1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)][int(column)-1])


	#diagonal	
	if GameBoard[int(row)+1][int(column)+1] != 0 and GameBoard[int(row)+1][int(column)+1] != "F":
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)+1][int(column)+1])
		
	if GameBoard[int(row)+1][int(column)+1] == 0:
		GameBoard[int(row)+1][int(column)+1] = FakePiece(0,row+1,int(column)+1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)+1][int(column)+1])


		
	if GameBoard[int(row)+1][int(column)-1] != 0 and GameBoard[int(row)+1][int(column)-1] != "F":
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)+1][int(column)-1])
		
	if GameBoard[int(row)+1][int(column)-1] == 0:
		GameBoard[int(row)+1][int(column)-1] = FakePiece(0,row+1,int(column)-1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)+1][int(column)-1])


		
	if GameBoard[int(row)-1][int(column)+1] != 0 and GameBoard[int(row)-1][int(column)+1] != "F":
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)-1][int(column)+1])
		
	if GameBoard[int(row)-1][int(column)+1] == 0:
		GameBoard[int(row)-1][int(column)+1] = FakePiece(0,row-1,int(column)+1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)-1][int(column)+1])

		
	if GameBoard[int(row)-1][int(column)-1] != 0 and GameBoard[int(row)-1][int(column)-1] != "F":
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)-1][int(column)-1])
		
	if GameBoard[int(row)-1][int(column)-1] == 0:
		GameBoard[int(row)-1][int(column)-1] = FakePiece(0,row-1,int(column)-1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)-1][int(column)-1])
				
def fakePiece(row,column,types):
	global GameBoard
	global fakeList
	#row
	GameBoard[int(row)][int(column)] = FakePiece(0,row,column,types)


	
	if GameBoard[int(row)+1][int(column)] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)+1][int(column)])
		
	if GameBoard[int(row)+1][int(column)] == 0:
		GameBoard[int(row)+1][int(column)] = FakePiece(0,row+1,column,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)+1][int(column)])
	

		
	if GameBoard[int(row)-1][int(column)] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)-1][int(column)])
		
	if GameBoard[int(row)-1][int(column)] == 0:
		GameBoard[int(row)-1][int(column)] = FakePiece(0,row-1,column,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)-1][int(column)])

	#column	
	if GameBoard[int(row)][int(column)+1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)][int(column)+1])
					
	if GameBoard[int(row)][int(column)+1] == 0:
		GameBoard[int(row)][int(column)+1] = FakePiece(0,row,int(column)+1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)][int(column)+1])


	if GameBoard[int(row)][int(column)-1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)][int(column)-1])
		
	if GameBoard[int(row)][int(column)-1] == 0:
		GameBoard[int(row)][int(column)-1] = FakePiece(0,row,int(column)-1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)][int(column)-1])


	#diagonal	
	if GameBoard[int(row)+1][int(column)+1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)+1][int(column)+1])
		
	if GameBoard[int(row)+1][int(column)+1] == 0:
		GameBoard[int(row)+1][int(column)+1] = FakePiece(0,row+1,int(column)+1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)+1][int(column)+1])


		
	if GameBoard[int(row)+1][int(column)-1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)+1][int(column)-1])
		
	if GameBoard[int(row)+1][int(column)-1] == 0:
		GameBoard[int(row)+1][int(column)-1] = FakePiece(0,row+1,int(column)-1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)+1][int(column)-1])


		
	if GameBoard[int(row)-1][int(column)+1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)-1][int(column)+1])
		
	if GameBoard[int(row)-1][int(column)+1] == 0:
		GameBoard[int(row)-1][int(column)+1] = FakePiece(0,row-1,int(column)+1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)-1][int(column)+1])

		
	if GameBoard[int(row)-1][int(column)-1] != 0:
		GameBoard[int(row)][int(column)].addFull(GameBoard[int(row)-1][int(column)-1])
		
	if GameBoard[int(row)-1][int(column)-1] == 0:
		GameBoard[int(row)-1][int(column)-1] = FakePiece(0,row-1,int(column)-1,types)
		GameBoard[int(row)][int(column)].addEmpty(GameBoard[int(row)-1][int(column)-1])
#need to do iterative deepening search for each of the empty nodes
#iterate like 6 times
global deepness
global emptyNodes
global placeHolder
placeHolder = []
emptyNodes = []
deepness = 0
def IDS():
	global emptyNodes
	global deepness
	global myMoves

	global placeHolder
	global GameBoard
	#print("IDS")
	if deepness == 0:
		newPath = path("G")
		for i in opponentMoves:
			newPath.add_node(i)
			emptyNodes.append(newPath)
		
		newPath = path("G")
		for i in myMoves:
			#print(i.row,i.column)
			newPath.add_node(i)		
		#print(opponentMoves[0].row,opponentMoves[0].column)
			emptyNodes.append(newPath)
	else:
		for i in emptyNodes:
			#print(i)
			for k in i.pathQ[0].empty:
				#print(k.row, k.column,k.types)
			
				
				newPath = path("G")
			
				for l in i.pathQ:
					#print(l.row,l.column),
					newPath.add_node(l)

				#print("\n")

				fakePiece(k.row,k.column,"F")
				

				if k.row >= 0 and k.column>=0:
					newPath.add_node2(GameBoard[int(k.row)][int(k.column)])
					placeHolder.append(newPath)
			#for y in placeHolder[0]:
				#for t in i.pathQ[0].full:
					#if t.row == y.row and t.column == y.column:
					#placeHolder.remove(y)
		emptyNodes = placeHolder	
		#for i in emptyNodes:
			##print(i)
		
			#for y in i.pathQ:
				##print(deepness)
				#print(y.row,y.column),
			#print("\n")
			#print(deepness)
	deepness = deepness +1	
	if deepness < 20:
		IDS()
	else:
		#print("END")
		addHeuristics()


def addHeuristics():
	global GameBoard
	theList = []
	rowList = []
	for i in emptyNodes:
		#print(deepness)
		if deepness == 20:
			theList.append(i)						
	for r in theList:
		newList = []
		for g in r.pathQ:
			
			newList.append(g.row)
			#print(g.row),
			#print(g.column)
		if (len(set(newList)) < len(newList)):
			#print("TRUE")
			for i in r.pathQ:
				i.value = i.value + len(newList)-len(set(newList))
				#print(i.row,i.column,i.value)

		#print("\n")
		if allSame(newList) ==True and len(newList) == 5:
			
			#print(r.pathQ[0].row,r.pathQ[0].column)
			r.pathQ[0].value = 10000
			
		else:
			for i in r.pathQ:
				i.value = i.value + 0			
			#break
		
		
	for r in theList:
		newList = []
		for g in r.pathQ:
			
			newList.append(g.column)
			#print(g.row),
			#print(g.column)
		if (len(set(newList)) < len(newList)):
			#print("TRUE")
			for i in r.pathQ:
				i.value = i.value + len(newList)-len(set(newList))
				#print(i.row,i.column,i.value)

		#print("\n")
		if allSame(newList) ==True and len(newList) == 5:
			#print(r.pathQ[0].row,r.pathQ[0].column)
			r.pathQ[0].value = 10000
			
		else:
			for i in r.pathQ:
				i.value = i.value + 0			
			#break	
	
global newList
global nList	

def allSame(lists):
	return all(x == lists[0] for x in lists)

global currentNodes
global bigList			
global win
global smallList
win = 1
global last
last = ""
def minimax():
	global GameBoard
	global currentNodes
	global bigList
	global win
	win = 1
	global last
	
	global smallList

	global last
	currentNodes = []
	for i in emptyNodes:
		#print(i.pathQ[0].row, i.pathQ[0].column, i.pathQ[0].value)
		currentNodes.append(i.pathQ[0])
	end = 1
	while end == 1:
		if win != "ITS OVER":
			findMax()
			if win != "ITS OVER":
				findMin()
		elif win == "ITS OVER":
			#print(last.row,last.column)
			end = 2
	#print("\n")
def findMax():
	global currentNodes
	global bigList
	global win
	global smallList

	global last
	#print("MAX")
	bigList = []

	currentNodes = sorted(currentNodes, key = lambda x: x.value, reverse=True)
	
	biggest = currentNodes[0]
	#print(biggest.value)
	for i in currentNodes:
		if i.value == biggest.value:
			bigList.append(i)
			if i == opponentMoves[0]:
				win = "ITS OVER"
				last = smallList[0]
			#print(i.row,i.column,i.value)
def findMin():
	global currentNodes
	global bigList
	global win
	global smallList

	global last
	#print("MIN")
	currentNodes = []
	smallList = []
	for i in bigList:
		for o in i.full:
			currentNodes.append(o)
			#print(o.row,o.column,o.value)

	currentNodes = sorted(currentNodes, key = lambda x: x.value, reverse=False)
	smallest = currentNodes[0]
	#print(smallest.value)
	for i in currentNodes:
		if i.value == smallest.value:
			smallList.append(i)
			if i == opponentMoves[0]:
				win = "ITS OVER"
				last = bigList[0]
			#print(i.row,i.column,i.value)		
def printOutStuff():
	global myMoves
	print("Groupx"),
	#print(""),
	print(last.row),	
	#print(""),
	column = int(last.column)
	#print(column)
	c = "A"
	if column == 1:
		c = "A"
	elif column == 2:
		c = "B"
	elif column == 3:
		c = "C"
	elif column == 4:
		c = "D"
	elif column == 5:
		c = "E"
	elif column == 6:
		c = "F"
	elif column == 7:
		c = "G"
	elif column == 8:
		c = "H"	
	elif column == 9:
		c = "I"	
	elif column == 10:
		c = "J"	
	elif column == 11:
		c = "K"	
	elif column == 12:
		c = "L"	
	elif column == 13:
		c = "M"			
	print(c)
	myMoves.append(last)
	
def restartGame():
	global myMoves
	global GameBoard
	global opponentMoves
	global win
	global last
	last = ""
	win=""
	GameBoard = np.zeros([15,15], dtype = int)
	GameBoard = np.zeros([15,15], dtype = object)
	for i in opponentMoves:
		#print(i.row,i.column)
		#for f in i.empty:
			#print(f.row,f.column),
		#print("")
		newPiece(i.row,i.column,'O')
		#for i in GameBoard[i.row][i.column].empty:
			#print(i.row,i.column)
	for i in myMoves:
		#print(i)
		newPiece(i.row,i.column,'Y')
	

	#print(GameBoard)				
#then print out that move and start again
def main():
	global myMoves
	
	global GameBoard
	global last
	global opponentMoves
	isMyTurn()
	IDS()
	minimax()
	printOutStuff()
	#restartGame()

if __name__ == "__main__":
	main()		

