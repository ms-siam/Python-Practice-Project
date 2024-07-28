#Conway's game of life
import random, time, copy
Width = 6
Height = 2

#create a lift of lists for the cells
nextCells = []
for x in range(Width):
    column = [] #create a new column
    for y in range(Height):
        if random.randint(0, 1) == 0:
            column.append('#') #Add living cell
        else:
            column.append(' ') #Add dead cell
    nextCells.append(column) #nextCells is list of column lists

while True: #Main program loop
    print('\n\n\n\n\n') #seperate each step with new lines
    currentCells = copy.deepcopy(nextCells)

    #Print currentCells on the screen
    for y in range(Height):
        for x in range(Width):
            print(currentCells[x][y], end = '') #print the # or space
        print() #print a newline at the end of the row
    
    #Calculate the next step's cells:
    for x in range(Width):
        for y in range(Height):
            #get neighboring coordinates:
            # `%WIDTH` ensures leftCoord id always between 0 and WIDTH -1
            leftCoord = (x - 1) % Width
            rightCoord = (x + 1) % Width
            aboveCoord = (y - 1) % Width
            belowCoord = (y + 1) % Width

            #Count Number of living neighbors:

        numNeighbors = 0
        if currentCells[leftCoord][aboveCoord] == '#':
            numNeighbors += 1 #Top left neighbor is alive 
        if currentCells[x][aboveCoord] == '#':
            numNeighbors += 1 #Top neighbor is alive 
        if currentCells[rightCoord][aboveCoord] == '#':
            numNeighbors += 1 #Top right neighbor is alive 
        if currentCells[leftCoord][y] == '#':
            numNeighbors += 1 #Left neighbor is alive 
        if currentCells[rightCoord][y] == '#':
            numNeighbors += 1 #Right neighbor is alive 
        if currentCells[leftCoord][belowCoord] == '#':
            numNeighbors += 1 #Bottom-left neighbor is alive 
        if currentCells[x][belowCoord] == '#':
            numNeighbors += 1 #Bottom neighbor is alive 
        if currentCells[rightCoord][belowCoord] == '#':
            numNeighbors += 1 #Bottom-right neighbor is alive 
        
        #Set cell based on conway's game of life rules:
        if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
            #Living cells with 2 or 3 neighbors stay alive:
            nextCells[x][y] = '#'
        elif currentCells[x][y] == ' ' and numNeighbors == 3:
            #Dead cells with 3 neighbors become alive:
            nextCells[x][y] = '#'
        else:
            #Everything else dies or stays dead:
            nextCells[x][y] = ' '
    time.sleep(1) #Add a 1-sec pause to reduce flickering