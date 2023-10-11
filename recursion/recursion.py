#################### get subsequence
def getSubsequence(str):
    #base case
    if len(str)==0:
        return [""]

    ch=str[0]
    ros=str[1:]
    #faith
    sans=getSubsequence(ros)
    bigAns=[]
        #ourwork
    for sstr in sans:
        bigAns.append(sstr)

    for ichr in sans:
        bigAns.append(ch+ichr)
    return bigAns
############################### print subsequence
def printSubsequence(str,asf,currIdx):
   if(len(str)==currIdx):
       print(asf)
       return

   printSubsequence(str,asf+str[currIdx],currIdx+1)
   printSubsequence(str,asf,currIdx+1)

##############################print stair paths

def printStairPaths(asf,n):
    #base
    if(n==0):
        print(asf)
        return
    if(n<0):
       return
    #faith
    printStairPaths(asf+str(1),n-1)
    printStairPaths(asf+str(2),n-2)
    printStairPaths(asf+str(3),n-3)

#==========================get maze paths
def getMazePaths(cr,cc,dr,dc):
    #baseCase
    if(cr==dr and cc==dc):
        return [""]

    bigAns=[]
    #faith
    if(cc+1<=dc):
        horPath=getMazePaths(cr,cc+1,dr,dc)
        for sans in horPath:
            bigAns.append("h"+sans)
    if(cr+1<=dr):
        verPath=getMazePaths(cr+1,cc,dr,dc)
        for sans in verPath:
            bigAns.append("v"+sans)

    #ourWork


    return bigAns

#=================================tower of hanoi
def toh(n,a,b,c):
    if(n==0):
        return

    #faith1
    toh(n-1,a,c,b)
    print("move disc "+str(n)+" from "+a+b)
    #faith2
    toh(n-1,c,b,a)

#=================================print all Permutation

def printPermutation(str,asf):
    #base case
    if(len(str)==0):
        print(asf)
        return

    #faith
    for i in range(len(str)):
        ch=str[i]
        left_part=str[:i]
        right_part = str[i+1:]
        newProb=left_part+right_part
        printPermutation(newProb,asf+ch)

#=================================print maze paths with jumps

def printMazePathsWithJumps(cr,cc,dr,dc,asf):
    #base case
    if(cr==dr and cc==dc):
        print(asf)
        return
    if(cr>dr or cc>dc):
        return


    for i in range(1,4):
        #horizontally
        printMazePathsWithJumps(cr,cc+i ,dr,dc,asf+"h"+str(i))
        #vertically
        printMazePathsWithJumps(cr+i,cc,dr,dc,asf+"v"+str(i))
        #diagonally
        printMazePathsWithJumps(cr+i,cc+i,dr,dc,asf+"d"+str(i))

#=================================print encoding
def printEncoding(str,asf):
    #base Case
    if(len(str)==0):
        print(asf)
        return

    ch1=str[0]
    #check for 0
    if(ch1!=0):
        c1= chr(ord('a')+int(ch1) -1)
        roq=str[1:]
        #faith1
        printEncoding(roq,asf+c1)

    if(len(str)>=2):
        roq=str[2:]
        ch2=str[0:2]
        if(int(ch2)<=26):
            c2= chr(ord('a')+int(ch2)-1)
            #faith2
            printEncoding(roq,asf+c2)

#==================================Print all maze paths with 4 moves tdlr and blockers
def printAllPathsBacktrack(maze,cr,cc,dr,dc,asf,visited):
    #base case
    if(cr==dr and cc==dc):
        print(asf)
        return

    #edgecases
    if(cr<0 or cc<0 or cr>dr or cc>dc or maze[cr][cc]==1 or visited[cr][cc]):
        return

    visited[cr][cc]=True

    #faith 1 t
    printAllPathsBacktrack(maze,cr-1,cc,dr,dc,asf+"t",visited)
    #faith 2 d
    printAllPathsBacktrack(maze,cr+1,cc,dr,dc,asf+"d",visited)
    #faith 3 l
    printAllPathsBacktrack(maze,cr,cc-1,dr,dc,asf+"l",visited)
    #faith 4 r
    printAllPathsBacktrack(maze,cr,cc+1,dr,dc,asf+"r",visited)

    visited[cr][cc]=False

def targetSumSubset(arr,currIdx,ssf,ss,target):
    if(currIdx==len(arr)):
        if(ssf==target):
            print(ss)
        return

    #faith
    targetSumSubset(arr,currIdx+1,ssf+arr[currIdx],ss+str(arr[currIdx])+"-",target)

    #faith2
    targetSumSubset(arr,currIdx+1,ssf,ss,target)

#=====================NQueens

def isQueenSafe(chess,row,col):
    #check diagonally left upside
     i=row-1
     j=col-1
     while(i>=0 and j>=0):
        if(chess[i][j]==1):
            return False
        i-=1
        j-=1
     #upward direction
     i = row-1
     j = col
     while(i>=0):
        if(chess[i][j]==1):
            return False
        i-=1
                 #diagonal right upward
     i=row-1
     j=col+1
     while(i>=0 and j<len(chess)):
         if(chess[i][j]==1):
             return False
         i-=1
         j+=1
     return True
def placeNQueens(chess,asf,row):

    #base case
    if(row==len(chess)):
        print(asf)
        return

    for col in range(len(chess)):

        if(isQueenSafe(chess,row,col)):
            chess[row][col]=1
            #faith
            placeNQueens(chess,asf+str(row)+"-"+str(col)+",",row+1)
            chess[row][col]=0

#==========================================knights tour
def displayBoard(chess):
    for row in chess:
        for col in row:
            print(col,end=' ')
        print()
    print()

def knightsTour(chess,row,col,step):
    if(row<0 or col<0 or row>=len(chess)or col>=len(chess) or chess[row][col]!=0):
        return

    #base
    if(step==len(chess)*len(chess)):
        chess[row][col]=step
        #print chess
        displayBoard(chess)
        chess[row][col]=0
        return

    chess[row][col]=step
    knightsTour(chess,row-2,col+1,step+1)
    knightsTour(chess,row-1,col+2,step+1)
    knightsTour(chess,row+1,col+2,step+1)
    knightsTour(chess,row+2,col+1,step+1)
    knightsTour(chess,row+2,col-1,step+1)
    knightsTour(chess,row+1,col-2,step+1)
    knightsTour(chess,row-1,col-2,step+1)
    knightsTour(chess,row-2,col-1,step+1)
    chess[row][col]=0


# chess=[
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0]
# ]
# knightsTour(chess,0,0,1)
# placeNQueens(chess,"",0)

# arr=[10,20,30,40,50]
# targetSumSubset(arr,0,0,"",50)
#maze=[
    #[0,1,0,0],
   # [0,0,0,0],
  #  [0,1,0,0],
 #   [1,0,0,0]
#]
#visited=[
#    [False,False,False,False],
#    [False,False,False,False],
#    [False,False,False,False],
#   [False,False,False,False]
#]
#printAllPathsBacktrack(maze,0,0,3,3,"",visited)

#n=int(input())
#print(getSubsequence(str))
#print(printSubsequence(str,"",0))
#printStairPaths("",n)
#print(getMazePaths(0,0,n-1,n-1))
#toh(3,'A','B','C')
#printPermutation("abc","")
#printMazePathsWithJumps(0,0,2,2,"")
#printEncoding("1234","")