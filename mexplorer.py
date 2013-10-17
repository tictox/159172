import pygame
import mazeclass
import time
# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size=[1000,500]
screen=pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("Maze Project")

# Get a new maze
mazegrid =  [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
             [2,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,2],
             [2,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1,1,0,2],
             [2,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,2],
             [2,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,2],
             [2,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,2],
             [2,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,2],
             [2,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,2],
             [2,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,6],
             [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

the_maze = mazeclass.Maze(mazegrid)


##########################################################

# code to be implemented
# make a variable for the stack class
#stack = Stack()
stack = []

class Position:
    def __init__(self,i,j):
        self.icoord = i
        self.jcoord = j
        

def depthfirsttraversal(i,j):
    up = the_maze.grid[i-1][j]
    down = the_maze.grid[i+1][j]
    left = the_maze.grid[i][j-1]
    right = the_maze.grid[i][j+1]
    
# check for a leaf node
    isLeaf = False
    if up.status == 3 or up.status == 4: 
        if down.status != 0 and down.status != 3 and down.status != 4:
            if left.status != 0 and left.status != 3 and left.status != 4:
                if right.status != 0 and right.status != 3 and right.status != 4:
                    isLeaf = True
    elif down.status == 3 or down.status == 4: 
        if up.status != 0 and up.status != 3 and up.status != 4:
            if left.status != 0 and left.status != 3 and left.status != 4:
                if right.status != 0 and right.status != 3 and right.status != 4:
                    isLeaf = True
    elif left.status == 3 or left.status == 4: 
        if up.status != 0 and up.status != 3 and up.status != 4:
            if down.status != 0 and down.status != 3 and down.status != 4:
                if right.status != 0 and right.status != 3 and right.status != 4:
                    isLeaf = True
    elif right.status == 3 or right.status == 4: 
        if up.status != 0 and up.status != 3 and up.status != 4:
            if down.status != 0 and down.status != 3 and down.status != 4:
                if left.status != 0 and left.status != 3 and left.status != 4:
                    isLeaf = True
                    
    if isLeaf == True:
        the_maze.grid[i][j].status = 3
        return

# update and delay the maze
    the_maze.display_maze(screen) 
    pygame.time.delay(50) 
    pygame.display.flip()    
    # change the status of the cell to visited
 
    if the_maze.grid[i][j].status == 0:
        the_maze.grid[i][j].status = 3
    elif the_maze.grid[i][j].status == 3:
        the_maze.grid[i][j].status = 4
        
    the_maze.bot_xcoord = i
    the_maze.bot_ycoord = j
    
# check for any possible moves (up to 4 moves)
    if up.status == 0 or up.status == 3 or up.status == 6:
        depthfirsttraversal(i-1,j)
    if down.status == 0 or down.status == 3 or down.status == 6: 
        depthfirsttraversal(i+1,j)
    if left.status == 0 or left.status == 3 or left.status == 6:
        depthfirsttraversal(i,j-1)
    if right.status == 0 or right.status == 3 or right.status == 6:
        depthfirsttraversal(i,j+1)

def depthfirstsearch(i,j):
    current = the_maze.grid[i][j]
    
    while current.status != 6:
        current = the_maze.grid[i][j]
        position = Position(i,j)
        
        if current.status == 6:
            stack.append(position)
            stack.reverse()
            while len(stack) != 0:
                item = stack.pop()
                the_maze.bot_xcoord = item.icoord
                the_maze.bot_ycoord = item.jcoord
                the_maze.display_maze(screen) 
                pygame.time.delay(50) 
                pygame.display.flip()
            return
        up = the_maze.grid[i-1][j]
        down = the_maze.grid[i+1][j]
        left = the_maze.grid[i][j-1]
        right = the_maze.grid[i][j+1]
        print str(i) + " " + str(j)
        print "up " + str(up.status)
        print "down " + str(down.status)
        print "left " + str(left.status)
        print "right " + str(right.status)
        if up.status == 0 or up.status == 6:
            current.status = 5
            stack.append(position)
            print current.status
            i = i - 1
        elif down.status == 0 or down.status == 6:
            current.status = 5
            current.status = 5
            stack.append(position)
            i = i + 1
        elif right.status == 0 or right.status == 6:
            current.status = 5
            stack.append(position)
            j = j + 1
        elif left.status == 0 or left.status == 6:
            current.status = 5
            stack.append(position)
            j = j - 1
        else:
            current.status = 5
            new = stack.pop()
            i = new.icoord
            j = new.jcoord
            
def breadthfirstsearch(i,j):
    return

# Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while done==False:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN: # If user wants to perform an action
                if event.key == pygame.K_d:
                    the_maze.reset(mazegrid)
                    x = the_maze.bot_xcoord
                    y = the_maze.bot_ycoord
                    depthfirsttraversal(the_maze.bot_xcoord, the_maze.bot_ycoord)
                    the_maze.bot_xcoord = x
                    the_maze.bot_ycoord = y
                if event.key == pygame.K_s:
                    the_maze.reset(mazegrid)
                    depthfirstsearch(the_maze.bot_xcoord, the_maze.bot_ycoord)
                if event.key == pygame.K_q:
                    the_maze.reset(mazegrid)
                    breadthfirstsearch(the_maze.bot_xcoord, the_maze.bot_ycoord)
     
        the_maze.display_maze(screen)
        # Limit to 20 frames per second
        clock.tick(50)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
# If you forget this line, the program will 'hang' on exit.
pygame.quit ()