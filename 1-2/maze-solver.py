import numpy
import sys

#initialize data structures
try:
    #the maze which was made using maze-maker.py
    maze = numpy.load("maze.npy")
    
    #stores the DFS path in form of (next cell,current cell) entries
    path = []       
    
    #stores potential node that can be visited next in format same as of path list
    next_node = []  
    
    #stores the final path as traversed by DFS from starting cell to the end cell
    finalpath=[]
    
    #stores the cell that have been visited with value >1 to avoid repetition while performing DFS
    visited = numpy.zeros([maze.shape[0],maze.shape[1]],dtype=int)
except:
    print("loading error")
    sys.exit()



#getting the final path from the path list 
#the format for the path node needs to be (child node , parent node)
#linear function that gets the path by finding the current's node parent node repeatedly till the end of the list
def get_path():
    current = path.pop()
    finalpath.append(current[:2])
    #print("adding {} to the final path ".format(current[:2]))

    next=[]
    while(len(path)>0):
        next = path.pop()
        # print("checking {} and {} ".format(next[:2],current[2:]))
        if next[:2] == current[2:]:
            # print("found equal")
            finalpath.append(next[:2])
            # print("adding {} to the final path ".format(next[:2]))
            current = next            
    finalpath.append(next[2:])
    finalpath.reverse()



#function for depth first search            
def dfs(currentx,currenty,endx,endy):

    #the end condition for stopping the recursion and exiting the programme
    if currentx == endx and currenty == endy:
        #debug statements commented out
        # print(path)
        # print(visited)
        get_path()
        print("The maze is : \n {}".format(maze))
        print("the DFS path is {}".format(finalpath))
        sys.exit()

    #dfs works on first in first out principle 
    #adding entries for potential next node in the next_node list
    if currentx>0 and maze[currenty , currentx-1] == 1 and visited[currenty , currentx-1]==0:
        next_node.append([currentx-1,currenty,currentx,currenty])
    if currenty>0 and maze[currenty-1 , currentx] == 1 and visited[currenty-1 , currentx]==0:
        next_node.append([currentx,currenty-1,currentx,currenty])
    if currentx<maze.shape[1]-1 and maze[currenty , currentx+1] == 1 and visited[currenty , currentx+1]==0:
        next_node.append([currentx+1,currenty,currentx,currenty])
    if currenty<maze.shape[0]-1 and maze[currenty+1 , currentx] == 1 and visited[currenty+1 , currentx]==0:
        next_node.append([currentx,currenty+1,currentx,currenty])
    
    #poping the last entry from next_node list and calling DFS on the node 
    while(1):
        next = next_node.pop()
        if visited[next[1],next[0]] == 0 : 
            #adding the node to path list so that the final path can be calculated
            path.append(next)
            #marking the node as visited to avoid repetition of nodes
            visited[currenty,currentx]=len(path)
            dfs(next[0],next[1],endx,endy)
    


def solve():
    #taking user input for starting coordinates
    startx = int(input("enter staring x coordinates :"))
    starty = int(input("enter starting y coordinates :"))

    #taking user input for ending coordinates
    endx = int(input("enter ending x coordinates :"))
    endy = int(input("enter ending y coordinates :"))

    #applying depth first search to get a path from the initial point to the final point
    dfs(startx,starty,endx,endy)

    
if __name__ == "__main__":
    solve()
    
