#Created 14 September 2017

import os

import time		

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

		
global fakeList
fakeList = []
global GameBoard
GameBoard = []                                                        
for i in range (0, 15):                               
    new = []                 
    for j in range (0, 15):          
        new.append(GamePiece(0,i,j,"E",None))             
    GameBoard.append(new)
global turn
turn = 1



    
global opponentMoves
opponentMoves = []

def playGame():
	global GameBoard
	global opponentMoves
	
	global turn
	fileExistsBool = os.path.isfile('./groupX.go')
	if os.path.isfile('./history.txt') == False:

		recordFile = open('./history.txt', 'w+')


	if (fileExistsBool):
	
		f = open("move_file","r")


		recordFile = open('./history.txt', 'a')


		if os.path.isfile('./firstturn.txt') == True:
			isMyTurn()
		else:

			f = open("move_file","w")

			f.write("GroupX" +" "+ "F" + " " + "7")
			print("'F' , 7")
			GameBoard[5][7] = GamePiece(0,5,7,"Y",None)
	
			opponentMoves.append(GameBoard[5][7])

			recordFile = open('./history.txt', 'a')

			
			recordFile.write("5" + " " + "7" + " " + "Y" + "\n")
			a=open('./firstturn.txt', 'w+')
			a.close()
			time.sleep(0.2)
	

def isMyTurn():
	global opponentMoves
	
	global GameBoard
	global matrix
	f = open("move_file", "r")
	recordFile = open("history.txt", "r")

	i=f.read(1)
	
	while i != " ":
		i=f.read(1)
		
	row = f.read(1)
	if row == "A" or row == "a":
		row = 0
	if row == "B" or row == "b":
		row = 1
	if row == "C" or row == "c":
		row = 2
	if row == "D" or row == "d":
		row = 3
	if row == "E" or row == "e":
		row = 4	
	if row == "F" or row == "f":
		row = 5
	if row == "G" or row == "g":
		row = 6	
	if row == "H" or row == "h":
		row = 7
	if row == "I" or row == "i":
		row = 8
	if row == "J" or row == "j":
		row = 9
	if row == "K" or row == "k":
		row = 10
	if row == "L" or row == "l":
		row = 11
	if row == "M" or row == "m":
		row = 12
	if row == "N" or row == "n":
		row = 13
	if row == "O" or row == "o":
		row = 14
	
	f.read(1)
	column = f.read(2)
	

	f.readline(1)
	f.readline(1)
	GameBoard[int(row)][int(column)] = GamePiece(0,row,column,"O",None)
	
	opponentMoves.append(GameBoard[int(row)][int(column)])


	stop = 0
	while stop == 0:

		r = recordFile.read(1)
		if r == "":
			stop = 2
			break
		recordFile.read(1)
		r.upper()
		print(r),
		c = recordFile.read(2)
		if int(c) >= 10:
			recordFile.read(1)

		print(c),
		t = recordFile.read(1)
		print(t)
		recordFile.readline(1)

		GameBoard[int(r)][int(c)] = GamePiece(0,int(r),int(c),str(t),None)
		opponentMoves.append(GameBoard[int(row)][int(column)])


	f.close()
	recordFile.close()
	makeTree()
def setHeuristic(l):
	global newList
	global otherList

	for i in l:

		if i.row == i.parent.row:
			#print("TWO")
			i.value = i.value + 2
			if i.parent.row == i.parent.parent.row:
				#print("THREE")
				i.value = i.value + 3
				if i.parent.parent.row == i.parent.parent.parent.row:
					#print("FOUR")
					i.value = i.value + 4
					if i.parent.parent.parent.row == i.parent.parent.parent.parent.row:
						#print("FIVE")
						i.value = i.value+100

	
	for i in l:
		if i.column == i.parent.column:
			#print("TWO")
			i.value = i.value + 2
			if i.parent.column == i.parent.parent.column:
				#print("THREE")
				i.value = i.value + 3
				if i.parent.parent.column == i.parent.parent.parent.column:
					#print("FOUR")
					i.value = i.value + 4
					if i.parent.parent.parent.column == i.parent.parent.parent.parent.column:
						#print("FIVE")
						i.value =i.value + 100
						
	for i in l:
		if i.column+1 == i.parent.column and i.row+1 == i.parent.row:
			#print("TWO")
			i.value = i.value + 2
			if i.parent.column+1 == i.parent.parent.column and i.parent.row+1 == i.parent.parent.row:
				#print("THREE")
				i.value = i.value + 3
				if i.parent.parent.column+1 == i.parent.parent.parent.column and i.parent.parent.row+1 == i.parent.parent.parent.row:
					#print("FOUR")
					i.value = i.value + 4
					if i.parent.parent.parent.column+1 == i.parent.parent.parent.parent.column and i.parent.parent.parent.row+1 == i.parent.parent.parent.parent.row:
						#print("FIVE")
						i.value =i.value + 100
		
	for i in l:
		if i.column-1 == i.parent.column and i.row+1 == i.parent.row:
			#print("TWO")
			i.value = i.value + 2
			if i.parent.column-1 == i.parent.parent.column and i.parent.row+1 == i.parent.parent.row:
				#print("THREE")
				i.value = i.value + 3
				if i.parent.parent.column-1 == i.parent.parent.parent.column and i.parent.parent.row+1 == i.parent.parent.parent.row:
					#print("FOUR")
					i.value = i.value + 4
					if i.parent.parent.parent.column-1 == i.parent.parent.parent.parent.column and i.parent.parent.parent.row+1 == i.parent.parent.parent.parent.row:
						#print("FIVE")
						i.value =i.value + 100	


	for i in l:
		if i.column+1 == i.parent.column and i.row-1 == i.parent.row:
			#print("TWO")
			i.value = i.value + 2
			if i.parent.column+1 == i.parent.parent.column and i.parent.row-1 == i.parent.parent.row:
				#print("THREE")
				i.value = i.value + 3
				if i.parent.parent.column+1 == i.parent.parent.parent.column and i.parent.parent.row-1 == i.parent.parent.parent.row:
					#print("FOUR")
					i.value = i.value + 4
					if i.parent.parent.parent.column+1 == i.parent.parent.parent.parent.column and i.parent.parent.parent.row-1 == i.parent.parent.parent.parent.row:
						#print("FIVE")
						i.value =i.value + 100	
						
						

	for i in l:
		if i.column-1 == i.parent.column and i.row-1 == i.parent.row:
			#print("TWO")
			i.value = i.value + 2
			if i.parent.column-1 == i.parent.parent.column and i.parent.row-1 == i.parent.parent.row:
				#print("THREE")
				i.value = i.value + 3
				if i.parent.parent.column-1 == i.parent.parent.parent.column and i.parent.parent.row-1 == i.parent.parent.parent.row:
					#print("FOUR")
					i.value = i.value + 4
					if i.parent.parent.parent.column-1 == i.parent.parent.parent.parent.column and i.parent.parent.parent.row-1 == i.parent.parent.parent.parent.row:
						#print("FIVE")
						i.value =i.value + 100	
global swithedList
switchedList = []	
def checkEmpty(l,l2):
	global fakeList
	global e

	global opponentMoves
	
	for i in l:

			
		if GameBoard[int(i.row)][int(i.column)].row != 14 :
			if GameBoard[int(i.row)+1][int(i.column)].types == "E":
				GameBoard[int(i.row)+1][int(i.column)].parent = GameBoard[int(i.row)][int(i.column)]
				l2.append(GameBoard[int(i.row)+1][int(i.column)])
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)+1][int(i.column)])		

		if GameBoard[int(i.row)][int(i.column)].column != 14:					
			if GameBoard[int(i.row)][int(i.column)+1].types == "E":
				GameBoard[int(i.row)][int(i.column)+1].parent = GameBoard[int(i.row)][int(i.column)]
				l2.append(GameBoard[int(i.row)][int(i.column)+1])
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)][int(i.column)+1])		
	
				
		if GameBoard[int(i.row)][int(i.column)].row != 0 :	
			if GameBoard[int(i.row)-1][int(i.column)].types == "E":
				GameBoard[int(i.row)-1][int(i.column)].parent = GameBoard[int(i.row)][int(i.column)]
				l2.append(GameBoard[int(i.row)-1][int(i.column)])
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)-1][int(i.column)])		
						
		if GameBoard[int(i.row)][int(i.column)].row != 0 :								
			if GameBoard[int(i.row)][int(i.column)-1].types == "E":
				l2.append(GameBoard[int(i.row)][int(i.column)-1])
				GameBoard[int(i.row)][int(i.column)-1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)][int(i.column)-1])		
				
				
				
		if GameBoard[int(i.row)][int(i.column)].row != 0 and GameBoard[int(i.row)][int(i.column)].column != 14 and GameBoard[int(i.row)][int(i.column)].column != 0 and GameBoard[int(i.row)][int(i.column)].row != 14:							
			if GameBoard[int(i.row)-1][int(i.column)-1].types == "E":
				l2.append(GameBoard[int(i.row)-1][int(i.column)-1])
				GameBoard[int(i.row)-1][int(i.column)-1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)-1][int(i.column)-1])		

		if GameBoard[int(i.row)][int(i.column)].row != 0 and GameBoard[int(i.row)][int(i.column)].column != 14 and GameBoard[int(i.row)][int(i.column)].column != 0 and GameBoard[int(i.row)][int(i.column)].row != 14:							
			if GameBoard[int(i.row)+1][int(i.column)-1].types == "E":
				l2.append(GameBoard[int(i.row)+1][int(i.column)-1])
				GameBoard[int(i.row)+1][int(i.column)-1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)+1][int(i.column)-1])		
		if GameBoard[int(i.row)][int(i.column)].row != 0 and GameBoard[int(i.row)][int(i.column)].column != 14 and GameBoard[int(i.row)][int(i.column)].column != 0 and GameBoard[int(i.row)][int(i.column)].row != 14:							
			if GameBoard[int(i.row)+1][int(i.column)+1].types == "E":
				l2.append(GameBoard[int(i.row)+1][int(i.column)+1])
				GameBoard[int(i.row)+1][int(i.column)+1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)+1][int(i.column)+1])	
		if GameBoard[int(i.row)][int(i.column)].row != 0 and GameBoard[int(i.row)][int(i.column)].column != 14 and GameBoard[int(i.row)][int(i.column)].column != 0 and GameBoard[int(i.row)][int(i.column)].row != 14:							
			if GameBoard[int(i.row)-1][int(i.column)+1].types == "E":
				l2.append(GameBoard[int(i.row)-1][int(i.column)+1])
				GameBoard[int(i.row)-1][int(i.column)+1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)-1][int(i.column)+1])	

global newList
newList = []	
global otherList
otherList = []	
global bestList
bestList = []
global e
e = 0
global types
types = "Y"
global listType
listType = ""	
def makeTree():
	global opponentMoves
	global fakeList
	global e
	global types
	global newList
	global bestList
	global otherList
	checkEmpty(opponentMoves,fakeList)
	newList = []
	otherList = []
	checkEmpty(fakeList, newList)
	fakeList = []
	for i in newList:
		i.types = "E"
	checkEmpty(newList,fakeList)
	for i in fakeList:
		i.types = "E"

	newList = []
	checkEmpty(fakeList,newList)
	for i in newList:
		i.types = "E"

	fakeList = []

	for i in newList:
		i.types = "E"



	bestList = newList
	
	minimax()
global final 
final = []
global end 
end = 0		
global stopper
stopper = 10
def minimax():
	global final
	global bestList
	global opponentMoves
	global stopper
	global otherList
	global end
	global types

	global f
	final = []
	setHeuristic(bestList)
	for i in bestList:
		i.value = i.value +abs(int(i.row) - int(opponentMoves[0].row))  + abs(int(i.column) - int(opponentMoves[0].column)) 

	bestList = sorted(bestList, key = lambda x: x.parent.row, reverse=False	)
	bestList = sorted(bestList, key = lambda x: x.parent.column, reverse=False	)

	findMinimax()		
	if stopper == 0:
		printItOut()
	
def printItOut():

	f = open("move_file", "w+")
	row = final[0].row
	column = final[0].column
	recordFile = open("history.txt", "a")

	recordFile.write(str(row) + " " + str(column) + " " + "Y")
	recordFile.write("\n")

	if row == 0:
		row = "A"
	if row == 1:
		row = "B"
	if row == 2:
		row = "C"
	if row == 3:
		row = "D"
	if row == 4:
		row = "E"
	if row == 5:
		row = "F"
	if row == 6:
		row = "G"
	if row == 7:
		row = "H"
	if row == 8:
		row = "I"
	if row == 9:
		row = "J"
	if row == 10:
		row = "K"
	if row == 11:
		row = "L"
	if row == 12:
		row = "M"
	if row == 13:
		row = "N"
	if row == 14:
		row = "O"
	row.upper()
	print(row,column)

	
	recordFile.close()
	f.truncate()
	f.write("GroupX" +" "+ str(row) + " " + str(column))		

def findMinimax():
	global bestList
	global opponentMoves
	global stopper
	global types

	global final
	global end
	maxList = []
	final = []
	someList = []
		
	for i in bestList:
		for y in i.parent.empty:
			maxList.append(y.value)
		if types == "O":
			i.parent.value = min(maxList)
			#print(types)
			types = "Y"
		else:
			i.parent.value = max(maxList)
			#print(types)
			types = "O"

		maxList = []
	for i in bestList:
		someList.append(i.parent)

	prune(someList)

	bestList = set(someList)



	for i in someList:

		for k in opponentMoves:
			for y in k.empty:
				if i.row == y.row and i.column == y.column:
					if i not in final and len(final) < 4:
						final.append(i)
						#print(i.row,i.column)
					else:
						if types == "Y":
							final = sorted(final, key = lambda x: x.value, reverse=True)

						else:
							final = sorted(final, key = lambda x: x.value, reverse=False)

						stopper = 0
						#print("STOP")


					
	#look how recursive it is
	if stopper != 0:
		findMinimax()

def prune(parentlist):
	global types

	#this is where intermediate nodes are checked
	setHeuristic(parentlist)
	if types == "Y":
		parentlist = sorted(parentlist, key = lambda x: x.value, reverse=True)
	else:
		parentlist = sorted(parentlist, key = lambda x: x.value, reverse=False)
	#this is where pruning happens
	while len(parentlist) > 4:
		del parentlist[len(parentlist)-1]

def main():
	global myMoves
	
	global GameBoard
	global last
	global opponentMoves
	playGame()



if __name__ == "__main__":
	main() 
