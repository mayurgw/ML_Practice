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
        curr_pacman=MyStack[len(MyStack)-1]
        nonVisitedNearBy=0
        steps=steps+1
        # if len(MyStack)>50:
        #     break
        curr_pacman_r=curr_pacman[0]
        curr_pacman_c=curr_pacman[1]
        visited.append(curr_pacman)
        # print(str(curr_pacman_r)+" "+str(curr_pacman_c)+"\n")
        buff=buff+str(curr_pacman_r)+" "+str(curr_pacman_c)+"\n"
        if grid[curr_pacman_r][curr_pacman_c]==".":
            break;
        if (curr_pacman_r+1)<r and grid[curr_pacman_r+1][curr_pacman_c]!="%" and [curr_pacman_r+1,curr_pacman_c] not in visited:
            # if [curr_pacman_r+1,curr_pacman_c] not in visited:
            nonVisitedNearBy=1
            MyStack.append([curr_pacman_r+1,curr_pacman_c])
        elif (curr_pacman_c+1)<c and grid[curr_pacman_r][curr_pacman_c+1]!="%" and [curr_pacman_r,curr_pacman_c+1] not in visited:
            print("RIGHT")
            # if [curr_pacman_r,curr_pacman_c+1] not in visited:
            nonVisitedNearBy=1
            MyStack.append([curr_pacman_r,curr_pacman_c+1])
        elif (curr_pacman_c-1)>0 and grid[curr_pacman_r][curr_pacman_c-1]!="%" and [curr_pacman_r,curr_pacman_c-1] not in visited:
            print("LEFT")
            # if [curr_pacman_r,curr_pacman_c-1] not in visited:
            nonVisitedNearBy=1
            MyStack.append([curr_pacman_r,curr_pacman_c-1])
        elif (curr_pacman_r-1)>0 and grid[curr_pacman_r-1][curr_pacman_c]!="%" and [curr_pacman_r-1,curr_pacman_c] not in visited :
            print("UP")
            # if [curr_pacman_r-1,curr_pacman_c] not in visited:
            nonVisitedNearBy=1
            MyStack.append([curr_pacman_r-1,curr_pacman_c])
        else:
            MyStack.pop()
        #if nonVisitedNearBy==0:
        if len(MyStack)>50:
            MyStack.pop()
           
    buff=str(steps)+"\n"+buff+str(steps-1)+"\n"+buff
    #print(buff)
    print(len(MyStack))
    for coord in MyStack:
        print(str(coord[0])+" "+ str(coord[1]))
    return
pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)