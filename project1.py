#Nicolette Vere
#Mathew Schwartzman
#Jonathan Berry
#!/usr/bin/python
class node:
    def __init__(self, name, heuristic,alphabetValue):
        self.name = name
        self.heuristic = heuristic
        self.children = []
        self.alphabetValue = alphabetValue
        
			
	        

    def add_child(self,childNode,distance):
        self.children.append(childNode)
        self.distance = distance
        childNode.children.append(self)
        childNode.distance = distance
class connection:
	def __init__(self, node1, node2,value):
		self.value = value
		self.node1 = node1
		self.node2 = node2
		
		


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

	
	
f = open("graph.txt")
files = f.read(1)
num = 0			
nodeList = []			
conn1=[]	
number = 0
while files != '#':
	files=f.read(1)
f.readline()
while num < 10:
	files = f.read(1)
	nodeName = files
	files = f.read(1)
	files=f.readline()
	nodeH = files
	newNode = node(nodeName,nodeH , 0)
	nodeList.append(newNode)
	num = num+1
f.close()
newList = []
y = open("graph.txt")

while number < 20:

	realNode = y.read(1)
	
	if realNode == '#':
		number = 21
		break
	y.read(1)
	friend = y.read(1)

	y.read(1)
	
	dist = y.read(4)
	
	newList.append(realNode)
	newList.append(friend)
	
	number = number+1
		    
for k in nodeList:
	for h in newList:
		if k.name == h:
			newList.remove(h)
			
for k in nodeList:
	for h in newList:
		if k.name == h:
			newList.remove(h)

for j in newList:
	newNode = node(j,0,0)
	nodeList.append(newNode)
y.close()
g= open("graph.txt")
number = 0
x=0
while number < 20:

	realNode = g.read(1)
	
	
	if realNode == '#':
		number = 21
		break
	g.read(1)
	friend = g.read(1)
	
	for i in nodeList:
		if friend == i.name:
			nodeFriend = i

	g.read(1)		
	dist = g.readline()
	while x < 5:	
		for h in nodeList:
			if h.name == '':
				nodeList.remove(h)
			if h.name == '\n':
				nodeList.remove(h)
			if h.name == '#':
				nodeList.remove(h)
		x = x+1
	for i in nodeList:
		if i.name == realNode:
			i.add_child(nodeFriend,dist)
			newConnection = connection(i,nodeFriend,dist)
			conn1.append(newConnection)


			


	
	number = number+1



for i in nodeList:
	i.distance = float(i.distance)
	global deepness
	deepness = 3
	
for i in nodeList:
	if i.name == 'A':
		i.alphabetValue = 1	
	elif i.name == 'C':
		i.alphabetValue = 3			
	elif i.name == 'D':
		i.alphabetValue = 4	
	elif i.name == 'E':
		i.alphabetValue = 5	
	elif i.name == 'F':
		i.alphabetValue = 6	
	elif i.name == 'G':
		i.alphabetValue = 7
	elif i.name == 'H':
		i.alphabetValue = 8	
	elif i.name == 'I':
		i.alphabetValue = 9	
	elif i.name == 'J':
		i.alphabetValue = 10
	elif i.name == 'S':
		i.alphabetValue = 11		
########	Nicolette does 2,5,8
#General Search
queue = []
openNodes = []
stopper = 1
expanding = []

def IDS():
	global deepness
	expanding = sorted(expanding, key = lambda x: x.alphabetValue, reverse=True)
	for g in expanding:
		newPath = path('G')
		for r in openNodes[0].pathQ:
			
			newPath.add_node(r)
		for i in newPath.pathQ:
			if g not in newPath.pathQ:	
				newPath.add_node2(g)
				if len(newPath.pathQ) < deepness:
					queue.insert(0,newPath)
					deepness = deepness + 1


def General_Search(problem, search):
	queue = []
	openNodes = []
	stopper = 1
	
	expanding = []
	newPath = path('G')
	newPath.add_node(problem[0])
	queue.append(newPath)
	print(search)
	while stopper == 1:
		if len(queue) == 0:
			return "FAILURE"
		
		openNodes.insert(0,queue[0])
	

		
		for i in queue:
			for j in i.pathQ:
				
				print(j.name),
			
			print(","),
			
		print("")
		
		
		del queue[0]
		if openNodes[0].pathQ[0].name == 'G':
			stopper = 2
			print("GOAL")
		expanding = []
		for i in openNodes[0].pathQ[0].children:
		#add to queue depending on search method
			expanding.insert(0,i)
			
		
		if search == "breath-first":
				
			#first = openNodes[0].pathQ[0].name
			#for x in expanding:
				#second = x.name
				#for a in conn1:
					#if a.node1.name ==first and a.node2.name == second:
						#x.distance = a.value
						#print(first,second, x.distance)
					#elif a.node1.name==second and a.node2.name==first:
						#x.distance = a.value
						#print(first,second, x.distance)
			
						
			expanding = sorted(expanding, key = lambda x: x.alphabetValue, reverse=False)
			for g in expanding:
				newPath = path('G')
				for r in openNodes[0].pathQ:
					
					newPath.add_node(r)
				for i in newPath.pathQ:
					if g not in newPath.pathQ:	
						newPath.add_node2(g)
						queue.append(newPath)
		if search == "depth-first":
		
				
			#first = openNodes[0].pathQ[0].name
			#for x in expanding:
				#second = x.name
				#for a in conn1:
					#if a.node1.name ==first and a.node2.name == second:
						#x.distance = a.value
						#print(first,second, x.distance)
					#elif a.node1.name==second and a.node2.name==first:
						#x.distance = a.value
						#print(first,second, x.distance)
			
						
			expanding = sorted(expanding, key = lambda x: x.alphabetValue, reverse=True)
			for g in expanding:
				newPath = path('G')
				for r in openNodes[0].pathQ:	# for first seen in open nodes
					
					newPath.add_node(r)	# add path to visited nodes
				for i in newPath.pathQ:	#
					if g not in newPath.pathQ:	
						newPath.add_node2(g)
						queue.insert(0,newPath)
											
		if search == "uniform-cost":
		
				
			first = openNodes[0].pathQ[0].name
			for x in expanding:
				second = x.name
				for a in conn1:
					if a.node1.name ==first and a.node2.name == second:
						x.distance = a.value
						
					elif a.node1.name==second and a.node2.name==first:
						x.distance = a.value
						
			
			
				newPath = path('G')
				
				for r in openNodes[0].pathQ:
					
					newPath.add_node(r)
					newPath.totalPath = newPath.totalPath + float(r.distance)
					

				if r.name != x.name:	
					newPath.add_node2(x)
					queue.append(newPath)
				newPath.totalPath = newPath.totalPath + float(x.distance)
				
					
			queue = sorted(queue, key = lambda x: float(x.totalPath), reverse=False)
			
			
		if search == "beam":
			placeHolder = []
			expanding = sorted(expanding, key = lambda x: x.heuristic, reverse=False)
			
			
			if len(expanding)-1 > 1:
				
				placeHolder.append(expanding[0])
				placeHolder.append(expanding[1])
				placeHolder.append(expanding[2])
				placeHolder = sorted(placeHolder, key = lambda x: x.heuristic, reverse=False)

				if placeHolder[0].alphabetValue>placeHolder[1].alphabetValue:
					#print(placeHolder[0].name,placeHolder[1].name,placeHolder[2].name)
					del placeHolder[1]
					
					
					
					
				else:
					placeHolder = sorted(placeHolder, key = lambda x: x.heuristic, reverse=False)
					
					placeHolder2 =[]
					placeHolder2.append(placeHolder[2])
					placeHolder = placeHolder2
					
					
					
					#print(placeHolder[1].name)
			else:
				
				placeHolder = expanding
				#print(placeHolder[0].name)
				

			for g in placeHolder:
		
				
				newPath = path('G')
				for r in openNodes[0].pathQ:
					
					newPath.add_node(r)
				for i in newPath.pathQ:
					if g not in newPath.pathQ:	
						newPath.add_node2(g)
						queue.append(newPath)
			if len(queue) >2:
				if len(queue[0].pathQ)>2:
					if float(queue[2].pathQ[0].heuristic)>=float(queue[1].pathQ[0].heuristic):
						del queue[2]
			
		if search == "depth-limited":
		
				
			#first = openNodes[0].pathQ[0].name
			#for x in expanding:
				#second = x.name
				#for a in conn1:
					#if a.node1.name ==first and a.node2.name == second:
						#x.distance = a.value
						#print(first,second, x.distance)
					#elif a.node1.name==second and a.node2.name==first:
						#x.distance = a.value
						#print(first,second, x.distance)
			
						
			expanding = sorted(expanding, key = lambda x: x.alphabetValue, reverse=True)
			for g in expanding:
				newPath = path('G')
				for r in openNodes[0].pathQ:
					
					newPath.add_node(r)
				for i in newPath.pathQ:
					if g not in newPath.pathQ:	
						newPath.add_node2(g)
						if len(newPath.pathQ) < 4:
							queue.insert(0,newPath)
						
		if search == "iterative-deepening":
			global deepness
			expanding = sorted(expanding, key = lambda x: x.alphabetValue, reverse=True)
			for g in expanding:
				newPath = path('G')
				for r in openNodes[0].pathQ:
					
					newPath.add_node(r)
				for i in newPath.pathQ:
					if g not in newPath.pathQ:	
						newPath.add_node2(g)
						if len(newPath.pathQ) < deepness:
							queue.insert(0,newPath)
							deepness = deepness + 1
			
															
General_Search(nodeList, "breath-first")			
General_Search(nodeList, "uniform-cost")
General_Search(nodeList, "beam")
General_Search(nodeList, "depth-first")
General_Search(nodeList, "depth-limited")
General_Search(nodeList, "iterative-deepening")
