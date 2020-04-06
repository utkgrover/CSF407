#   code generates the maze to perform dfs on
#   maze is a numpy array , with 0 for blockage and i for path 
#   

import numpy 


def makeMaze():
    # print("The coordinate system is defined such that leftmost point on topmost row is (0,0)")
    # print("x coordinate as we move to the right, y increases as we move downwards ")
    
    height = int(input("enter the height of the maze :"))
    width  = int (input("enter the width of the maze :"))
    #print(" {} is the height , {} is the width ".format(height,width))
    
    maze = numpy.ones([height,width],dtype=int)
    #maze = numpy.full((height,width),1)
    #print(maze)

    while(True):
        x = int(input("enter x coordinate of the block , enter -1 to stop:\n"))
        if(x==-1):
            break
        y = int(input("enter y coordinate of the block :\n"))
        
        if(x>-1 and x<width and y>-1 and y<height):
            maze[y,x]=0

    print(maze)
    numpy.save("maze",maze)

if __name__ == "__main__":
    makeMaze()
