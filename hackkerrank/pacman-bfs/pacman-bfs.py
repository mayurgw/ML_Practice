#!/usr/bin/python

from collections import deque
def nextMove( r, c, pacman_r, pacman_c, food_r, food_c, grid):
    depthCnt=0
    steps=0
    queue=deque([[pacman_r,pacman_c]])
    queue.append([-1,-1])
    buff=""
    visited=[]
    cameFrom={}
    cameFrom[str(pacman_r)+" "+str(pacman_c)]=""
    while len(queue)>0:
        #print(queue)
        curr_pacman_r,curr_pacman_c=queue.popleft()
        # curr_pacman_r=int(curr_pacman_r)
        # curr_pacman_c=int(curr_pacman_c)
        
        if curr_pacman_r==-1:
            queue.append([-1,-1])
            depthCnt+=1
            continue
        if [curr_pacman_r,curr_pacman_c] not in visited:
            visited.append([curr_pacman_r,curr_pacman_c])

            buff=buff+str(curr_pacman_r)+" "+str(curr_pacman_c)+"\n"
            steps+=1
        
        
        #print(str(curr_pacman_r)+" "+str(curr_pacman_c))
       
        if grid[curr_pacman_r][curr_pacman_c]==".":
            buff_2=getCorrectPath(cameFrom,str(curr_pacman_r)+" "+str(curr_pacman_c))
            buff=buff+str(depthCnt)+buff_2
            break
        if (curr_pacman_r-1)>0 and grid[curr_pacman_r-1][curr_pacman_c]!="%":
            if [curr_pacman_r-1,curr_pacman_c] not in visited:
                queue.append([curr_pacman_r-1,curr_pacman_c])
                cameFrom[str(curr_pacman_r-1)+" "+str(curr_pacman_c)]=str(curr_pacman_r)+" "+str(curr_pacman_c)
        if (curr_pacman_c-1)>0 and grid[curr_pacman_r][curr_pacman_c-1]!="%":
            if [curr_pacman_r,curr_pacman_c-1] not in visited:
                queue.append([curr_pacman_r,curr_pacman_c-1])
                cameFrom[str(curr_pacman_r)+" "+str(curr_pacman_c-1)]=str(curr_pacman_r)+" "+str(curr_pacman_c)
        if (curr_pacman_c+1)<c and grid[curr_pacman_r][curr_pacman_c+1]!="%":
            if [curr_pacman_r,curr_pacman_c+1] not in visited:
                queue.append([curr_pacman_r,curr_pacman_c+1])
                cameFrom[str(curr_pacman_r)+" "+str(curr_pacman_c+1)]=str(curr_pacman_r)+" "+str(curr_pacman_c)
        if (curr_pacman_r+1)<r and grid[curr_pacman_r+1][curr_pacman_c]!="%":
            if [curr_pacman_r+1,curr_pacman_c] not in visited:
                queue.append([curr_pacman_r+1,curr_pacman_c])
                cameFrom[str(curr_pacman_r+1)+" "+str(curr_pacman_c)]=str(curr_pacman_r)+" "+str(curr_pacman_c)
    print(str(steps)+"\n"+buff)    
    return

def getCorrectPath(cameFrom,corr_coord):
    pathList=[]
    pathList.append(corr_coord)
    temp=corr_coord
    while (temp!=""):
        pathList.append(cameFrom[temp])
        # print(temp)
        temp=cameFrom[temp]
    pathList.reverse()
    buff=""
    for path in pathList:
        # print(path)
        buff=buff+path+"\n"
    return buff

pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]
  
grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid)