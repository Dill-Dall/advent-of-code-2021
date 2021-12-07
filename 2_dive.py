tup = [('forward',5),('down',5),('forward', 8),('up', 3),('down', 8),('forward', 2)]

myListofTuples = [()]

with open('2.txt') as inputFile:
    myListofTuples = [tuple(line.split()) for line in inputFile.readlines()]


horizontal=0
depth=0
aim=0
for command in myListofTuples:
    direction   = command[0]
    distance    = int(command[1])
    if(direction == "forward"):
        horizontal += distance
        depth += distance * aim
    if(direction == "backward"):
        horizontal += -distance
    elif(direction == "down"):
        aim   += distance
    elif(direction == "up"):
        aim   += -distance
print(f'hor: {horizontal} depth: {depth} total: {horizontal*depth}')
