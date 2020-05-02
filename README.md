# depth-first-search-maze-problem
Solving a Maze problem with Depth First Search method

- Initial position for all the multiple mazes that read is the point "(0,0)"
- Goal is to reach the max point "(N-1, M-1)", where N and M corresponds to the height and width of the maze.
- The multiple mazes will be read from the file that is provided in the drive file shared with you
- The maze consists of 0s and 1s which 0s indicate a clear path and 1s indicate a wall that can not be moved
- To reach to the goal, you are required to provide a path consist of clear roads(0s)


```
- maze =[[0,0,0,0,0,0]
        [0,1,0,0,0,0],
        [0,0,1,1,1,0],
        [0,0,0,0,0,0],
        [1,0,0,0,1,0]] 
```
        
- The returned path should be:
```
path => [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)]
```

- The directions extracted from this path is:
```
direction => R R R R R D D D D
```
