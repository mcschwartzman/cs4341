# Project 1 Assignment for Intro to WPI
# Jon Berry
# Mathew Schwartzman
# Nicolette Vere

#!/usr/bin/python
#!/usr/bin/python
class node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.children = []

    def add_child(self,childNode,distance):
        self.children.append(childNode)
        self.distance = distance
        childNode.children.append(self)
        childNode.distance = distance

f = open("graph.txt")
files = f.read(1)
num = 0			
nodeList = []			
	
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
	newNode = node(nodeName,nodeH)
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
	newNode = node(j,0)
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


	
	number = number+1




	
#########	Nicolette does 2,5,8
#Breath First Seach
#start at S
queue=[]
unsortedQ=[]
queue.append(nodeList[0])
print("Breath First Search")
print(queue[0].name)
while queue[0].name != 'G':
#look at first node in q's kiddos
	for i in queue[0].children:
		unsortedQ.append(i.distance)
	
#sort them by distance
	unsortedQ.sort()
	queueSorted = []
	for i in unsortedQ:
		for j in queue[0].children:
			if i == j.distance:
				if j not in queueSorted:
					queueSorted.append(j)
#add them to queue
	for i in queueSorted:
		queue.append(i)
	for i in queue:
		print(i.name),
#remove the first already check one from queue
	del queue[0]
	print("")
