#Created 14 September 2017

import os


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
for i in range (0, 15):                               
    new = []                 
    for j in range (0, 15):          
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
def playGame():
	global GameBoard
	global opponentMoves
	fileExistsBool = os.path.isfile('./file.txt')
	f = open("move_file.txt")
	if (fileExistsBool):	
		if f.read(1) == "":
			f.close()
			f = open("move_file.txt","w")

			f.write("GroupX" +" "+ "F" + " " + "7")
			print("'F' , 7")
			GameBoard[5][7] = GamePiece(0,5,7,"O",None)
	
			opponentMoves.append(GameBoard[5][7])

		
		else:
			isMyTurn()
		
def isMyTurn():
	global opponentMoves
	
	global GameBoard
	global matrix
	f = open("move_file.txt")

	i=f.read(1)
	
	while i != " ":
		i=f.read(1)
		
	row = f.read(1)
	if row == "A":
		row = 0
	if row == "B":
		row = 1
	if row == "C":
		row = 2
	if row == "D":
		row = 3
	if row == "E":
		row = 4	
	if row == "F":
		row = 5
	if row == "G":
		row = 6	
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

	f.close()
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
						#l.remove(i)
						#print(i.row,i.column,i.value)
						#otherList.append(i)
		#print(i.row,i.column,i.parent)
	
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
		#print(i.row,i.column,i.parent)
global swithedList
switchedList = []	
def checkEmpty(l,l2):
	global fakeList
	global e

	global opponentMoves
	
	for i in l:
		#print("___")
		#print(GameBoard[int(i.row)][int(i.column)].row ,GameBoard[int(i.row)][int(i.column)].column,GameBoard[int(i.row)][int(i.column)].value)

			
		if GameBoard[int(i.row)][int(i.column)].row != 14 :
			if GameBoard[int(i.row)+1][int(i.column)].types == "E":
				#print("Right")
				#print(GameBoard[int(i.row)+1][int(i.column)].row,GameBoard[int(i.row)+1][int(i.column)].column)
				GameBoard[int(i.row)+1][int(i.column)].parent = GameBoard[int(i.row)][int(i.column)]
				#GameBoard[int(i.row)+1][int(i.column)].types = "F"
				l2.append(GameBoard[int(i.row)+1][int(i.column)])
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)+1][int(i.column)])		

		if GameBoard[int(i.row)][int(i.column)].column != 14:					
			if GameBoard[int(i.row)][int(i.column)+1].types == "E":
				#print("UP")
				#print(GameBoard[int(i.row)][int(i.column)+1].row,GameBoard[int(i.row)][int(i.column)+1].column)
				GameBoard[int(i.row)][int(i.column)+1].parent = GameBoard[int(i.row)][int(i.column)]
				#GameBoard[int(i.row)][int(i.column)+1].types = "F"
				l2.append(GameBoard[int(i.row)][int(i.column)+1])
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)][int(i.column)+1])		
	
				
		if GameBoard[int(i.row)][int(i.column)].row != 0 :	
			if GameBoard[int(i.row)-1][int(i.column)].types == "E":
				#print("LEFT")
				#print(GameBoard[int(i.row)-1][int(i.column)].row,GameBoard[int(i.row)-1][int(i.column)].column)
				GameBoard[int(i.row)-1][int(i.column)].parent = GameBoard[int(i.row)][int(i.column)]
				#GameBoard[int(i.row)-1][int(i.column)].types = "F"
				l2.append(GameBoard[int(i.row)-1][int(i.column)])
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)-1][int(i.column)])		
						
		if GameBoard[int(i.row)][int(i.column)].row != 0 :								
			if GameBoard[int(i.row)][int(i.column)-1].types == "E":
				l2.append(GameBoard[int(i.row)][int(i.column)-1])
				#GameBoard[int(i.row)][int(i.column)-1].types = "F"	
				GameBoard[int(i.row)][int(i.column)-1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)][int(i.column)-1])		
				#print("DOWN")
				#print(GameBoard[int(i.row)][int(i.column)-1].row,GameBoard[int(i.row)][int(i.column)-1].column)
				
				
				
		if GameBoard[int(i.row)][int(i.column)].row != 0 and GameBoard[int(i.row)][int(i.column)].column != 14:								
			if GameBoard[int(i.row)-1][int(i.column)-1].types == "E":
				l2.append(GameBoard[int(i.row)-1][int(i.column)-1])
				#GameBoard[int(i.row)][int(i.column)-1].types = "F"	
				GameBoard[int(i.row)-1][int(i.column)-1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)-1][int(i.column)-1])		

				#print("LEFTDOWN")
				#print(GameBoard[int(i.row)][int(i.column)-1].row,GameBoard[int(i.row)][int(i.column)-1].column)
		if GameBoard[int(i.row)][int(i.column)].row != 0 and GameBoard[int(i.row)][int(i.column)].column != 14:								
			if GameBoard[int(i.row)+1][int(i.column)-1].types == "E":
				l2.append(GameBoard[int(i.row)+1][int(i.column)-1])
				#GameBoard[int(i.row)][int(i.column)-1].types = "F"	
				GameBoard[int(i.row)+1][int(i.column)-1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)+1][int(i.column)-1])		

				#print("LEFTUP")
				#print(GameBoard[int(i.row)][int(i.column)-1].row,GameBoard[int(i.row)][int(i.column)-1].column)		
		if GameBoard[int(i.row)][int(i.column)].row != 0 and GameBoard[int(i.row)][int(i.column)].column != 14:								
			if GameBoard[int(i.row)+1][int(i.column)+1].types == "E":
				l2.append(GameBoard[int(i.row)+1][int(i.column)+1])
				#GameBoard[int(i.row)][int(i.column)-1].types = "F"	
				GameBoard[int(i.row)+1][int(i.column)+1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)+1][int(i.column)+1])	
				#print("RIGHTUP")	
		if GameBoard[int(i.row)][int(i.column)].row != 0 and GameBoard[int(i.row)][int(i.column)].column != 14:								
			if GameBoard[int(i.row)-1][int(i.column)+1].types == "E":
				l2.append(GameBoard[int(i.row)-1][int(i.column)+1])
				#GameBoard[int(i.row)][int(i.column)-1].types = "F"	
				GameBoard[int(i.row)-1][int(i.column)+1].parent = GameBoard[int(i.row)][int(i.column)]
				GameBoard[int(i.row)][int(i.column)].addEmpty(GameBoard[int(i.row)-1][int(i.column)+1])	
				#print("RIGHTDOWN")
				#print(GameBoard[int(i.row)][int(i.column)-1].row,GameBoard[int(i.row)][int(i.column)-1].column)
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
	e= 0
	while e < 1:
		#setHeuristic(newList)

		#for i in newList:
			#if i.value >= 1000000:
				#otherList.append(i)
				#newList.remove(i)
			#if not newList:
				#e = 1
		checkEmpty(newList,fakeList)
		for i in fakeList:
			i.types = "E"
		bestList = fakeList
		newList =[]
		#setHeuristic(fakeList)
		#for i in fakeList:
			#if i.value >= 1000000:
				#otherList.append(i)
				#fakeList.remove(i)
	
			#if not fakeList:
				#e=1
		checkEmpty(fakeList,newList)
		for i in newList:
			i.types = "E"
		bestList = newList
		fakeList = []
		e = e+1
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
	global f
	final = []	
	#for i in otherList:
		#bestList.append(i)
	setHeuristic(bestList)
	for i in bestList:
		i.value = i.value +abs(int(i.row) - int(opponentMoves[0].row))  + abs(int(i.column) - int(opponentMoves[0].column)) 

		#print(i.row,i.column,i.value)
	bestList = sorted(bestList, key = lambda x: x.parent.row, reverse=False	)
	bestList = sorted(bestList, key = lambda x: x.parent.column, reverse=False	)

	while stopper > 0:
		if stopper != 0:
			findMin()		
		if stopper !=0:
			findMax()
		else:
			
			print(final[0].row,final[0].column)
			printItOut()	
		stopper=stopper-1
def printItOut():

	f = open("move_file.txt", "w+")

	row = final[0].row
	column = final[0].column
	
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
	
	print(row,column)

	f.truncate()
	f.write("GroupX" +" "+ str(row) + " " + str(column))

def findMin():
	#print("min")
	global bestList
	global opponentMoves
	global stopper
	global final
	global end
	maxList = []
	final = []
	someList = []
	#for i in opponentMoves[0].empty:
		
		#i.value = 0	
	for i in bestList:
		#print(i.parent.row,i.parent.column, i.row,i.column,i.value)
		for y in i.parent.empty:
			maxList.append(y.value)
		i.parent.value = min(maxList)
		maxList = []
	for i in bestList:
		someList.append(i.parent)
	bestList = set(someList)	
	for i in someList:
		#print(i.row,i.column,i.value)
		#for j in i.empty:
			#print(j.row,j.column,j.value),
		#print("MOO")
		for k in opponentMoves:
			for y in k.empty:
				if i.row == y.row and i.column == y.column:
					#print(i.row,i.column,y.row,y.column,i.value)

				#print("YOU WINNNN")
					final.append(i)
					stopper = 0
				#break


def findMax():
	#print("max")
	global stopper
	global bestList
	global opponentMoves
	global final
	global end
	#for i in opponentMoves[0].empty:
		
		#i.value = 100000	
	maxList = []
	someList = []
	for i in bestList:
		#print(i.parent.row,i.parent.column, i.row,i.column,i.value)
		for y in i.parent.empty:
			maxList.append(y.value)
		i.parent.value = max(maxList)
		maxList = []
	for i in bestList:
		someList.append(i.parent)
	bestList = set(someList)	
	for i in someList:
		#print(i.row,i.column,i.value)
		#for j in i.empty:
			#print(j.row,j.column,j.value),
		#print("MOO")
		for k in opponentMoves:
			for y in k.empty:
				if i.row == y.row and i.column == y.column:
					#print(i.row,i.column,y.row,y.column,i.value)
					final.append(i)
					stopper = 0

	
	
	
def main():
	global myMoves
	
	global GameBoard
	global last
	global opponentMoves
	playGame()


if __name__ == "__main__":
	main() 


def pruner():

	alpha
	beta
