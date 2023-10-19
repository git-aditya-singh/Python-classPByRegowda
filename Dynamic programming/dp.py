#memoization
def fib(n,dp):
    #base
    if(n<2):
        dp[n]=n
        return dp[n]
    if(dp[n]!=0):
        return dp[n]

    #faith
    dp[n]=fib(n-1,dp)+fib(n-2,dp)
    return dp[n]

#tabulation
def fib_tab(N,dp):
    for n in range(0,N+1):
        #base
        if(n<2):
            dp[n]= n
            continue

        #faith
        dp[n]= dp[n-1]+dp[n-2]  #fib(n-1,dp)+fib(n-2,dp)


def display(arr):
    for i in arr:
        print(i,end=" ")

def climbStairs(n,dp):
    #base
    if(n==0):
        dp[n]=1
        return dp[n]

    if(n<0):
        return 0

    if(dp[n]!=0):
        return dp[n]

    #faith
    s1=climbStairs(n-1,dp)
    s2=climbStairs(n-2,dp)
    s3=climbStairs(n-3,dp)

    dp[n]= s1+s2+s3
    return dp[n]

def climbStairs_tab(N,dp):
    for n in range(0,N+1):
        if(n==0):
            dp[n]=1
            continue

        #faith
        s1=0
        s2=0
        s3=0
        if(n-1>=0):
            s1=dp[n-1]
        if(n-2>=0):
            s2=dp[n-2]
        if(n-3>=0):
            s3=dp[n-3]

        dp[n]= s1+s2+s3
    return dp[N]

def climbStairsWithvariableJumps_memo(n,jumpsPossible,dp):
    if(n==0):
        dp[n]=1
        return dp[n]

    if(n<0):
        return 0

    if(dp[n]!=-1):
        return dp[n]

    stepsPossible=jumpsPossible[n-1]

    count=0
    for jump in range(1,stepsPossible+1):

        count+=climbStairsWithvariableJumps_memo(n-jump,jumpsPossible,dp)

    dp[n]=count
    return count

def climbStairsWithvariableJumps_tab(N,jumpsPossible,dp):
    for n in range(0,N+1):
        if(n==0):
            dp[n]=1
            continue
        stepsPossible=jumpsPossible[n-1]
        count=0
        for jump in range(1,stepsPossible+1):
            if(n-jump>=0):
                count+=dp[n-jump]
        dp[n]=count
    return dp[N]

def mazePathMinimum(cr,cc,dr,dc,maze):
    #base
    if(cr==dr and cc==dc):
        return maze[cr][cc]

    if(cr>dr or cc>dc):
        return 1000000000

    hc=mazePathMinimum(cr,cc+1,dr,dc,maze)
    dgc=mazePathMinimum(cr+1,cc+1,dr,dc,maze)
    vc=mazePathMinimum(cr+1,cc,dr,dc,maze)

    ans=min(min(hc,vc),dgc)
    return ans+maze[cr][cc]


def minMovesForStairsMemo(n,jumps,dp):
    if(n==0):
        return 0
    if(n<0):
        return float('inf')
    if(dp[n]!=-1):
        return dp[n]
    minMoves=float('inf')
    for jump in range(1,jumps[n-1]+1):
        moves=minMovesForStairsMemo(n-jump,jumps,dp)
        minMoves=min(minMoves,moves+1)

    dp[n]=minMoves
    return minMoves




def minMovesForStairsTab(N,jumps,dp):
    for n in range(N+1):
        if(n==0):
            dp[n]=0
            continue
        minMoves=float('inf')
        for jump in range(1,jumps[n-1]+1):
            if(n-jump>=0):
                moves= dp[n-jump] #minMovesForStairsMemo(n-jump,jumps,dp)
                minMoves=min(minMoves,moves+1)
        dp[n]=minMoves
    return dp[N]

def maxGoldMemo(mine,row,col,n,m,dp):
    if(col>=m):
        dp[row][col]= 0
        return dp[row][col]
    if(row<0 or row>=n):
        return 0
    if(dp[row][col]!=-1):
        return dp[row][col]
    ans1=maxGoldMemo(mine,row-1,col+1,n,m,dp)
    ans2=maxGoldMemo(mine,row,col+1,n,m,dp)
    ans3=maxGoldMemo(mine,row+1,col+1,n,m,dp)
    dp[row][col]=mine[row][col]+max(ans1,ans2,ans3)
    return dp[row][col]

def maxGoldTab(mine,row,n,m,dp):
        for col in range(m,-1,-1):
            if(col>=m):
                dp[row][col]= 0
                continue
            if(row>=n):
                dp[row][col]=0
                continue
            ans1=float('-inf')
            ans3=float('-inf')
            if(row-1>=0):
                ans1=dp[row-1][col+1]  #maxGold(mine,row-1,col+1,n,m,dp)
            ans2=dp[row][col+1]  #maxGold(mine,row,col+1,n,m,dp)
            if(row+1<n):
                ans3=dp[row+1][col+1] #(mine,row+1,col+1,n,m,dp)

            dp[row][col]=mine[row][col]+max(ans1,ans2,ans3)
        return dp[row][0]

def coinCombinationMemo(coins,n,target,dp):
    #base
    if(target==0):
        return 1
    if(n<=0):
        return 0
    if(dp[n][target]!=-1):
        return dp[n][target]
    inc=0
    #faith
    if(target-coins[n-1]>=0):
        inc=coinCombinationMemo(coins,n,target-coins[n-1],dp)
    exc=coinCombinationMemo(coins,n-1,target,dp)

    #ourwrk
    dp[n][target]=inc+exc
    return dp[n][target]

def coinCombinationTab(coins,N,Tar,dp):
    #base
    for n in range(N+1):
        for target in range (Tar+1):
            if(target==0):
                dp[n][target]= 1
                continue
            if(n==0):
                dp[n][target]=0
                continue
            inc=0
            #faith
            if(target-coins[n-1]>=0):
                 inc=dp[n][target-coins[n-1]]#coinCombinationMemo(coins,n,target-coins[n-1],dp)
            exc=dp[n-1][target]#coinCombinationMemo(coins,n-1,target,dp)
            dp[n][target]=inc+exc
    return dp[N][Tar]

def coinPermutationMemo(coins,n, tar,dp):
    if(tar==0):
        dp[n][tar]=1
        return dp[n][tar]
    if(dp[n][tar]!=-1):
        return dp[n][tar]
    perm=0
    for coin in coins:
       if(tar-coin>=0):
            perm+=coinPermutationMemo(coins,n,tar-coin,dp)
    dp[n][tar]= perm
    return dp[n][tar]

def coinPermutationTab(coins,n, Tar,dp):
    for tar in range(Tar+1):
        if(tar==0):
            dp[n][tar]=1
            continue

        perm=0
        for coin in coins:
            if(tar-coin>=0):
                perm+=dp[n][tar-coin]#coinPermutationMemo(coins,n,tar-coin,dp)
        dp[n][tar]= perm
    return dp[n][Tar]

def knapsack(n,values,weights,cap,dp):

    #base case:
    if(cap==0 or n==0):
        dp[n][cap]= 0
        return dp[n][cap]

    if(dp[n][cap]!=-1):
        return dp[n][cap]

    if(cap<weights[n-1]):
        exc=knapsack(n-1,values,weights,cap,dp)
        dp[n][cap]=exc
        return exc

    #faith
    inc=0
    if(cap-weights[n-1]>=0):
        inc=values[n-1]+knapsack(n-1,values,weights,cap-weights[n-1],dp)
    exc=knapsack(n-1,values,weights,cap,dp)

    dp[n][cap]= max(inc,exc)
    return dp[n][cap]

def knapsacktab(N,values,weights,Cap,dp):
    for n in range(N+1):
        for cap in range(Cap+1):

            if(cap==0 or n==0):
                dp[n][cap]= 0
                continue


            if(cap<weights[n-1]):
                exc=knapsack(n-1,values,weights,cap,dp)
                dp[n][cap]=exc
                continue

            inc=0
            if(cap-weights[n-1]>=0):
                inc=  values[n-1] + dp[n-1][cap-weights[n-1]]#knapsack(n-1,values,weights,cap-weights[n-1],dp)
            exc= dp[n-1][cap] #knapsack(n-1,values,weights,cap,dp)

            dp[n][cap]= max(inc,exc)

    return dp[N][Cap]

def knapsackUnbounded(n,values,weights,cap,dp):

    #base case:
    if(cap==0 or n==0):
        dp[n][cap]= 0
        return dp[n][cap]

    if(dp[n][cap]!=-1):
        return dp[n][cap]

    if(cap<weights[n-1]):
        exc=knapsackUnbounded(n-1,values,weights,cap,dp)
        dp[n][cap]=exc
        return exc


    inc=values[n-1]+knapsackUnbounded(n,values,weights,cap-weights[n-1],dp)
    exc=knapsackUnbounded(n-1,values,weights,cap,dp)

    dp[n][cap]= max(inc,exc)
    return dp[n][cap]

def countBinaryStringMemo(n,lastDigit,dp):
    if(n==1):
        dp[lastDigit][n]=1
        return dp[lastDigit][n]
    if(dp[lastDigit][n]!=-1):
        return dp[lastDigit][n]
    #faith
    count=0
    count+=countBinaryStringMemo(n-1,1,dp)
    if(lastDigit!=0):
        count+=countBinaryStringMemo(n-1,0,dp)
    dp[lastDigit][n]=count
    return dp[lastDigit][n]

def countBinaryStringTab(N,dp):
    for n in range(N+1):
        if(n==1):
            dp[0][n]=1
            dp[1][n]=1
            continue

        count=0
        dp[0][n]=dp[1][n-1]#countBinaryStringMemo(n-1,1,dp)
        count+=dp[0][n]
        dp[1][n]=dp[0][n-1]+count#countBinaryStringMemo(n-1,0,dp)

    return dp[0][N]+dp[1][N]

def countEncodings(str,n,dp):
    #base
    if(n==0 or n==1):
        return 1
    if(dp[n]!=-1):
        return dp[n]
    #faith
    if(str[n-1]>'0'):
        x=countEncodings(str,n-1,dp)
    if(str[n-2]=='1' or (str[n-2]=='2' and str[n-1]<'7')):
        y=countEncodings(str,n-2,dp)

    dp[n]=x+y
    return dp[n]

def countEncodingsTab(str,N,dp):
    for n in range(N+1):
        if(n==0 or n==1):
            dp[n]=1
            continue
        #faith
        if(str[n-1]>'0'):
            x=dp[n-1]#countEncodings(str,n-1,dp)
        if(str[n-2]=='1' or (str[n-2]=='2' and str[n-1]<'7')):
            y=dp[n-2]#countEncodings(str,n-2,dp)

        dp[n]=x+y
    return dp[N]

def paintHouse(mat,n,lastColour):
    if(n==0):
        return 0
    red=float('inf')
    green=float('inf')
    blue=float('inf')
    if(lastColour!=0):
        red=mat[n-1][0]+paintHouse(mat,n-1,0)
    if(lastColour!=1):
        green=mat[n-1][1]+paintHouse(mat,n-1,1)
    if(lastColour!=2):
        blue=mat[n-1][2]+paintHouse(mat,n-1,2)

    return min(red,green,blue)

def paintHouseMemo(mat,n,lastColour,dp):
    if(n==0):
        return 0
    if(dp[n][lastColour]!=-1):
        return dp[n][lastColour]
    red=float('inf')
    green=float('inf')
    blue=float('inf')
    if(lastColour!=0):
        red=mat[n-1][0]+paintHouseMemo(mat,n-1,0,dp)
    if(lastColour!=1):
        green=mat[n-1][1]+paintHouseMemo(mat,n-1,1,dp)
    if(lastColour!=2):
        blue=mat[n-1][2]+paintHouseMemo(mat,n-1,2,dp)

    dp[n][lastColour]=min(red,green,blue)
    return dp[n][lastColour]

def paintHouseTab(mat,N,dp):
    for n in range(N+1):
        if(n==0):
            dp[n][0]=0
            dp[n][1]=0
            dp[n][2]=0
            continue

        dp[n][0]=min(mat[n-1][0]+dp[n-1][1],mat[n-1][0]+dp[n-1][2])#paintHouseMemo(mat,n-1,0,dp)
        dp[n][1]=min(mat[n-1][1]+dp[n-1][0],mat[n-1][1]+dp[n-1][2])
        dp[n][2]=min(mat[n-1][2]+dp[n-1][0],mat[n-1][2]+dp[n-1][1])
        # green=mat[n-1][1]+paintHouseMemo(mat,n-1,1,dp)
        # blue=mat[n-1][2]+paintHouseMemo(mat,n-1,2,dp)

    return min(dp[N][0],dp[N][1],dp[N][2])

def tileFloor(n,dp):
    if(n==0 or n==1):
        dp[n]= 1
        return dp[n]
    if(dp[n]!=-1):
        return dp[n]
    #faith
    hz=tileFloor(n-2,dp)
    vr=tileFloor(n-1,dp)
    dp[n]= hz+vr
    return dp[n]

def tileFloorTab(N,dp):
    for n in range(N+1):
        if(n==0 or n==1):
            dp[n]= 1
            continue
        #faith
        hz=dp[n-2]#tileFloor(n-2,dp)
        vr=dp[n-1]#tileFloor(n-1,dp)
        dp[n]= hz+vr
    return dp[N]


def friendsPairing(n,dp):
    if(n==0 or n==1 or n==2):
        dp[n]=n
        return dp[n]
    if(dp[n]!=-1):
        return dp[n]
    #faith
    al=friendsPairing(n-1,dp)
    pair=friendsPairing(n-2,dp)
    dp[n]=al+((n-1)*pair)
    return dp[n]

def friendsPairingTab(N,dp):
    for n in range(N+1):
        if(n==0 or n==1 or n==2):
            dp[n]=n
            continue
    #faith
        al=dp[n-1]#friendsPairing(n-1,dp)
        pair=dp[n-2]#friendsPairing(n-2,dp)
        dp[n]=al+((n-1)*pair)
    return dp[N]

# dp=[[-1 for _ in range(3)] for _ in range(5)]
dp=[-1]*5
mat=[[2,3,4],
       [1,4,5],
       [3,6,3],
       [7,6,3]
       ]

print(friendsPairingTab(4,dp))
# print(coinPermutationTab([2,3,5,7,11],5,12,dp))
# print(knapsackUnbounded(5,[15,14,10,45,30],[2,5,1,3,4],7,dp))


# print(mazePathMinimum(0,0,3,3,maze))

# print(minMovesForStairsTab(4,[2,3,3,3],dp))
#######################





















