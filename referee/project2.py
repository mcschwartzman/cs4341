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
for i in range (0, 16):                               
    new = []                 
    for j in range (0, 16):          
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
	
		#f = open("move_file","r")


		recordFile = open('./history.txt', 'a')


		if os.path.isfile('./firstturn.txt') == True:
			isMyTurn()
		else:
			

			f = open("move_file","w")

			f.write("groupX" +" "+ "F" + " " + "9")
			f.flush()
			print("'F' , 9")
			GameBoard[5][7] = GamePiece(0,5,9,"Y",None)
	
			opponentMoves.append(GameBoard[5][7])

			recordFile = open('./history.txt', 'a')

			
			recordFile.write("5" + " " + "9" + " " + "Y" + "\n")
			a=open('./firstturn.txt', 'w+')
			
			time.sleep(0.2)
	
global bestList

def isMyTurn():
	global opponentMoves
	global bestList
	global GameBoard
	global matrix
	bestList = []
	
	move_fid = open("move_file", "r")
	lines = [s.strip() for s in move_fid.readlines()]
	move_fid.close()
		
	for line in lines:
		name, row, col = tuple(line.split())
		row_num = ord(row.lower()) - ord('a') + 1
		col_num = int(col, 10)
		GameBoard[row_num][col_num] = GamePiece(0,row_num,col_num,"O",None)
		opponentMoves.append(GameBoard[row_num][col_num])
	
	record_fid = open("history.txt", 'r')
	lines = [s.strip() for s in record_fid.readlines()]
	record_fid.close()
	
	for line in lines:
		row, col, y_field = tuple(line.split())
		row_num = int(row, 10)
		col_num = int(col, 10)
		GameBoard[row_num][col_num] = GamePiece(0,row_num,col_num,"O",None)
		opponentMoves.append(GameBoard[row_num][col_num])
	
	
	

	#i=f.read(1)
	
	#while i != " ":
		#i=f.read(1)
		
	#row = f.read(1)
	#if row == "A" or row == "a":
		#row = 1
	#if row == "B" or row == "b":
		#row = 2
	#if row == "C" or row == "c":
		#row = 3
	#if row == "D" or row == "d":
		#row = 4
	#if row == "E" or row == "e":
		#row = 5	
	#if row == "F" or row == "f":
		#row = 6
	#if row == "G" or row == "g":
		#row = 7	
	#if row == "H" or row == "h":
		#row = 8
	#if row == "I" or row == "i":
		#row = 9
	#if row == "J" or row == "j":
		#row = 10
	#if row == "K" or row == "k":
		#row = 11
	#if row == "L" or row == "l":
		#row = 12
	#if row == "M" or row == "m":
		#row = 13
	#if row == "N" or row == "n":
		#row = 14
	#if row == "O" or row == "o":
		#row = 15
	
	#f.read(1)
	#column = f.read(2)
	#if column < 10:
		#column.strip()

	#f.readline(1)
	#f.readline(1)
	#GameBoard[int(row)][int(column)] = GamePiece(0,row,column,"O",None)
	
	#opponentMoves.append(GameBoard[int(row)][int(column)])


	#stop = 0
	#while stop == 0:
		

		#r = recordFile.read(1)
		#if r == "":
			#stop = 2
			#break
		#recordFile.read(1)
		#r.upper()
		#print(r),
		#c = recordFile.read(2)
		#if c < 10:
			#c.strip()
		#recordFile.read(1)

		#print(c),
		#t = recordFile.read(1)
		#print(t)
		#recordFile.readline(1)

		#GameBoard[int(r)][int(c)] = GamePiece(0,int(r),int(c),str(t),None)
		#opponentMoves.append(GameBoard[int(r)][int(c)])
	
	#f.close()
	#recordFile.close()

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
	


#def getMoves((x,y)):
	#moves = []
	#for delx in range(-1,2):
		#for dely in range(-1,2):
			#if (int(x) + int(delx)) >= 0 and (int(x)+int(delx)) < 15 and (int(y) + int(dely)) >= 0 and (int(y)+int(dely)) < 15:
				 #moves.append((int(x)+int(delx),int(y)+int(dely)))

	#return moves
#def empty_moves(hMoves):	
	#all_moves = []

	#for move in hMoves:
		#print(move)
		#all_moves += (getMoves(move))
	#empty_move = []
	#for move in all_moves:
		#if move not in hMoves:
			#empty_move.append(move)
			
	#return empty_move
	
def checkEmpty(l,l2):
	global fakeList
	global e

	global opponentMoves
	
	for i in l:

			
		if GameBoard[int(i.row)][int(i.column)].row != 15 :
			if GameBoard[int(i.row)+1][int(i.column)].types == "E":
				GameBoard[int(i.row)+1][int(i.column)].parent = GameBoard[int(i.row)][int(i.column)]
				l2.append(GameBoard[int(i.row)+1][int(i.column)])
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)+1][int(i.column)])		

		if GameBoard[int(i.row)][int(i.column)].column != 15:					
			if GameBoard[int(i.row)][int(i.column)+1].types == "E":
				GameBoard[int(i.row)][int(i.column)+1].parent = GameBoard[int(i.row)][int(i.column)]
				l2.append(GameBoard[int(i.row)][int(i.column)+1])
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)][int(i.column)+1])		
	
				
		if GameBoard[int(i.row)][int(i.column)].row != 1 :	
			if GameBoard[int(i.row)-1][int(i.column)].types == "E":
				GameBoard[int(i.row)-1][int(i.column)].parent = GameBoard[int(i.row)][int(i.column)]
				l2.append(GameBoard[int(i.row)-1][int(i.column)])
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)-1][int(i.column)])		
						
		if GameBoard[int(i.row)][int(i.column)].row != 1 :								
			if GameBoard[int(i.row)][int(i.column)-1].types == "E":
				l2.append(GameBoard[int(i.row)][int(i.column)-1])
				GameBoard[int(i.row)][int(i.column)-1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)][int(i.column)-1])		
				
				
				
		if GameBoard[int(i.row)][int(i.column)].row != 1 and GameBoard[int(i.row)][int(i.column)].column != 15 and GameBoard[int(i.row)][int(i.column)].column != 1 and GameBoard[int(i.row)][int(i.column)].row != 15:							
			if GameBoard[int(i.row)-1][int(i.column)-1].types == "E":
				l2.append(GameBoard[int(i.row)-1][int(i.column)-1])
				GameBoard[int(i.row)-1][int(i.column)-1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)-1][int(i.column)-1])		

		if GameBoard[int(i.row)][int(i.column)].row != 1 and GameBoard[int(i.row)][int(i.column)].column != 15 and GameBoard[int(i.row)][int(i.column)].column != 1 and GameBoard[int(i.row)][int(i.column)].row != 15:							
			if GameBoard[int(i.row)+1][int(i.column)-1].types == "E":
				l2.append(GameBoard[int(i.row)+1][int(i.column)-1])
				GameBoard[int(i.row)+1][int(i.column)-1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)+1][int(i.column)-1])	
					
		if GameBoard[int(i.row)][int(i.column)].row != 1 and GameBoard[int(i.row)][int(i.column)].column != 15 and GameBoard[int(i.row)][int(i.column)].column != 1 and GameBoard[int(i.row)][int(i.column)].row != 15:							
			if GameBoard[int(i.row)+1][int(i.column)+1].types == "E":
				l2.append(GameBoard[int(i.row)+1][int(i.column)+1])
				GameBoard[int(i.row)+1][int(i.column)+1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)+1][int(i.column)+1])	
				
		if GameBoard[int(i.row)][int(i.column)].row != 1 and GameBoard[int(i.row)][int(i.column)].column != 15 and GameBoard[int(i.row)][int(i.column)].column != 1 and GameBoard[int(i.row)][int(i.column)].row != 15:							
			if GameBoard[int(i.row)-1][int(i.column)+1].types == "E":
				l2.append(GameBoard[int(i.row)-1][int(i.column)+1])
				GameBoard[int(i.row)-1][int(i.column)+1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)-1][int(i.column)+1])	

global newList
newList = []	
global otherList
otherList = []	

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
	global recursionFix
	global types

	global f
	final = []
	setHeuristic(bestList)

		
	for i in bestList:
		i.value = i.value +abs(int(i.row) - int(opponentMoves[0].row))  + abs(int(i.column) - int(opponentMoves[0].column)) 
	
	bestList = sorted(bestList, key = lambda x: x.parent.row, reverse=False	)
	bestList = sorted(bestList, key = lambda x: x.parent.column, reverse=False	)
	recursionFix = 0
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

	if row == 1:
		row = "A"
	if row == 2:
		row = "B"
	if row == 3:
		row = "C"
	if row == 4:
		row = "D"
	if row == 5:
		row = "E"
	if row == 6:
		row = "F"
	if row == 7:
		row = "G"
	if row == 8:
		row = "H"
	if row == 9:
		row = "I"
	if row == 10:
		row = "J"
	if row == 11:
		row = "K"
	if row == 12:
		row = "L"
	if row == 13:
		row = "M"
	if row == 14:
		row = "N"
	if row == 15:
		row = "O"
	row.upper()
	print(row,column)

	
	recordFile.close()
	f.truncate()
	f.write("groupX" +" "+ str(row) + " " + str(column))		

def findMinimax(recursionFix=10):
	global bestList
	global opponentMoves
	global stopper
	global types
	
	global final
	global end
	maxList = []
	final = []
	someList = []
		
	if recursionFix == 0:
		f = open("move_file", "w")
		print("hit recusion base")

		f.write("groupX" +" "+ int(list(bestList)[0].row) + " " + int(list(bestList)[0].column))
		f.flush()
		return 
		
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
				if i.row == y.row and i.column == y.column and i.column != 0 and i.row != 0 and i.column != 16 and i.row != 16:
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
	#look how recursive it is
	
	if stopper != 0:
		return findMinimax((recursionFix-1))

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
