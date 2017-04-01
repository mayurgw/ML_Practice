#!/usr/bin/python
def dfs( r, c, pacman_r, pacman_c, food_r, food_c, grid):
    # print("hello")
    curr_pacman_r=pacman_r
    curr_pacman_c=pacman_c
    MyStack=[]
    MyStack.append([curr_pacman_r,curr_pacman_c])
    steps=0
    buff=""
    visited=[]
    while (len(MyStack)>0):
        curr_pacman=MyStack.pop()
        steps=steps+1
        curr_pacman_r=curr_pacman[0]
        curr_pacman_c=curr_pacman[1]
        visited.append(curr_pacman)
        # print(str(curr_pacman_r)+" "+str(curr_pacman_c)+"\n")
        buff=buff+str(curr_pacman_r)+" "+str(curr_pacman_c)+"\n"
        if grid[curr_pacman_r][curr_pacman_c]==".":
            break;
        if (curr_pacman_r-1)>0 and grid[curr_pacman_r-1][curr_pacman_c]!="%":
            if [curr_pacman_r-1,curr_pacman_c] not in visited:
                MyStack.append([curr_pacman_r-1,curr_pacman_c])
        if (curr_pacman_c-1)>0 and grid[curr_pacman_r][curr_pacman_c-1]!="%":
            if [curr_pacman_r,curr_pacman_c-1] not in visited:
                MyStack.append([curr_pacman_r,curr_pacman_c-1])
        if (curr_pacman_c-1)<c and grid[curr_pacman_r][curr_pacman_c+1]!="%":
            if [curr_pacman_r,curr_pacman_c+1] not in visited:
                MyStack.append([curr_pacman_r,curr_pacman_c+1])
        if (curr_pacman_r+1)<r and grid[curr_pacman_r+1][curr_pacman_c]!="%":
            if [curr_pacman_r+1,curr_pacman_c] not in visited:
                MyStack.append([curr_pacman_r+1,curr_pacman_c])
    buff=str(steps)+"\n"+buff
    print(buff)
    
    return
pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)