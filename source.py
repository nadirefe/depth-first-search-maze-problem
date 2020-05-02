#!/usr/bin/env python
# coding: utf-8

# # Programming homework for searching algorithms
# 
# The problem is to provide a solution path to the maze with Depth First Search algorithm.
# 
# 
# 
# The problem specifications:
# 
# *   Initial position for all the multiple mazes that read is the point **"(0,0)"**
# *   Goal is to reach the max point **"(N-1, M-1)"**, where N and M corresponds to the height and width of the maze.
# *   The multiple mazes will be read from the file that is provided in the drive file shared with you
# *   The maze consists of **0**s and **1**s which **0s indicate a clear path** and **1s indicate a wall** that can not be moved
# *   To reach to the goal, you are required to provide a path consist of clear roads(0s)
# *   The reading and converting the path to the desired outputs have already been implemented which you **CANNOT** change in order to get full credits
# *   The exact outputs that your function expected to provide are printed it in the last code block given the expected output file.
# *   You need the provide the required function(s) that finds the path from initial position to the goal position using **Depth First Search**, which you may implement it with stack or recursively as you wish.
# 
# 
# For example, the solve_dfs function will take maze parameter as:
# 
# 
# ```
# maze = [[0,0,0,0,0,0],
#         [0,1,0,0,0,0],
#         [0,0,1,1,1,0],
#         [0,0,0,0,0,0],
#         [1,0,0,0,1,0]]   
# ```
# 
# The returned path should be:
# 
# 
# 
# ```
# path => [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)]
# ```
# 
# where (x, y) is tuples.
# 
# 
# The directions extracted from this path is:
# 
# 
# 
# ```
# direction => R R R R R D D D D
# ```
# 

# ### Modules that needed (You won't need any other module to implement the search algorithm)

# In[1]:


import collections
import numpy as np


# ### Functions that already implemented

# In[2]:


def read_mazes(input_file):
    mazes = []

    with open(input_file, 'r') as maze_file:
        maze = []
        
        for line in maze_file:
            if line != '\n':
                maze.append(line.replace('\n','').split(','))
            else:
                mazes.append(np.array(maze, dtype=int))
                maze = []

        if len(maze) > 0:
            mazes.append(np.array(maze, dtype=int))
    
    return mazes


# In[3]:


def get_directions(path):
    directions = ""

    current_cell = path[0]

    for cell in path[1:]:
        if current_cell[0] == cell[0]:
            if cell[1] - current_cell[1] > 0:
                directions += "R "
            else:
                directions += "L "
        else:
            if cell[0] - current_cell[0] > 0:
                directions += "D "
            else:
                directions += "U "
        current_cell = cell

    return directions.strip()


# ### Depth First Search algorithm which you will implement 
# 
# 
# 
# *   **The function takes 2d numpy array maze as a single parameter**
# *   **Returns a list of points that starts from (0,0) an ends with (N-1,M-1)**
# *   **The direction priorities are as follows Right-Down-Left-Up**
# *   **Returns None if goal can not be reached from the initial position**
# *   Read the initial instructions if not clear
# 
# Also, you can implement multiple functions as you like or just use this function.
# 
# **HOWEVER**, the **solve_dfs** function name **MUST** remain same and **MUST** take a **single parameter maze**
# 
# So, any other functions that you would fine it useful should be called from inside the solve_dfs function

# In[4]:


#FUNCTIONS

def goRight(loc):
    loc = list(loc)
    loc[1] = loc[1] + 1
    loc = tuple(loc)
    return loc

def goDown(loc):
    loc = list(loc)
    loc[0] = loc[0] + 1
    loc = tuple(loc)
    return loc

def goLeft(loc):
    loc = list(loc)
    loc[1] = loc[1] - 1
    loc = tuple(loc)
    return loc

def goUp(loc):
    loc = list(loc)
    loc[0] = loc[0] - 1
    loc = tuple(loc)
    return loc

#Cell class      
class Cell:
    def __init__(self,currentLoc):
        self.location = currentLoc
        self.visited = False
        self.value = None
        self.cameFrom = None

#Check the neighbour cells if they are visited nodes or nodes with value 1.  
def checkNeighbours(currentNode,nodeDict):
    if((nodeDict[goRight(currentNode)].visited ==True or nodeDict[goRight(currentNode)].value==1)
        and (nodeDict[goDown(currentNode)].visited ==True or nodeDict[goDown(currentNode)].value==1)
        and (nodeDict[goLeft(currentNode)].visited ==True or nodeDict[goLeft(currentNode)].value==1)
        and (nodeDict[goUp(currentNode)].visited ==True or nodeDict[goUp(currentNode)].value==1)):
        return True
"""
This start function covers the maze with 1's. For example, this maze:
maze = [[0,0,0,0,0,0],
        [0,1,0,0,0,0],
        [0,0,1,1,1,0],
        [0,0,0,0,0,0],
        [1,0,0,0,1,0]] 

would be this: 
maze = [[1,1,1,1,1,1,1,1]
        [1,0,0,0,0,0,0,1],
        [1,0,1,0,0,0,0,1],
        [1,0,0,1,1,1,0,1],
        [1,0,0,0,0,0,0,1],
        [1,1,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,1]]
"""

def start(maze,height,width,nodeDict): 
  for i in range(1,height+1):
      for k in range(1, width+1):
          cell = Cell((i,k))
          nodeDict[(i,k)] = cell
          cell.value = maze[(i-1,k-1)]     
#top line
  for i in range(0,width+2):
      cell = Cell((0,i))
      nodeDict[(0,i)] = cell
      cell.value = 1
#bottom line
  for i in range(0,width+2):
      cell = Cell((height+1+1,i))
      nodeDict[(height+1,i)] = cell
      cell.value = 1
#left line
  for i in range(1,height+1):
      cell = Cell((i,0))
      nodeDict[(i,0)] = cell
      cell.value = 1
#right line
  for i in range(1,height+1):
      cell = Cell((i,width+1))
      nodeDict[(i,width+1)] = cell
      cell.value = 1
  return nodeDict


# In[5]:


#Solve the maze with Depth First Search approach.
def solve_dfs(maze):
    width= maze.shape[1]
    height = maze.shape[0]
    goal = (maze.shape[0], maze.shape[1])
    nodeDict = {}
    path =[(1,1)]
    nodeDict= start(maze,height,width,nodeDict)
    currentNode = (1,1)    
    while(currentNode !=goal and path != None):
        if (nodeDict[goRight(currentNode)].value== 0 and nodeDict[goRight(currentNode)].visited ==False):
            nodeDict[goRight(currentNode)].visited = True
            nodeDict[goRight(currentNode)].cameFrom = currentNode
            currentNode = goRight(currentNode)
            path.append(currentNode)        
        elif(nodeDict[goDown(currentNode)].value== 0 and nodeDict[goDown(currentNode)].visited == False):
            nodeDict[goDown(currentNode)].visited = True
            nodeDict[goDown(currentNode)].cameFrom = currentNode
            currentNode = goDown(currentNode)
            path.append(currentNode)
        elif(nodeDict[goLeft(currentNode)].value == 0 and nodeDict[goLeft(currentNode)].visited == False):
            nodeDict[goLeft(currentNode)].visited = True
            nodeDict[goLeft(currentNode)].cameFrom = currentNode
            currentNode = goLeft(currentNode)
            path.append(currentNode)
        elif(nodeDict[goUp(currentNode)].value == 0 and nodeDict[goUp(currentNode)].visited == False):
            nodeDict[goUp(currentNode)].visited = True
            nodeDict[goUp(currentNode)].cameFrom = currentNode
            currentNode = goUp(currentNode)
            path.append(currentNode)
        elif (checkNeighbours(currentNode,nodeDict) ==True):
            if(currentNode == (1,1)):
                path =None
          
            else:
                currentNode = nodeDict[currentNode].cameFrom
                path.pop()
        else:
            path = None
    return path


# ### Main code block that reads the mazes, run the search algorithm and returns the path and prints the directions that reach to the goal

# In[7]:


#Read the maze from input.txt
mazes=read_mazes("input.txt")

for maze, ind in zip(mazes, range(1, len(mazes)+1)):
    path = solve_dfs(maze)

    if path != None:
        directions = get_directions(path)
        print(str(ind) + ") " + directions + '\n')
    else:
        print(str(ind) + ') Could not find a path...\n')

