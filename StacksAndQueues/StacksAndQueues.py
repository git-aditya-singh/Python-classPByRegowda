#====================balanced bracket
def balancedBracket(expression):
    st=[]
    for i in range (len(expression)):
        ch=expression[i]
        if(ch=='(' or ch=='{' or ch=='['):
            st.append(ch)
        elif(ch ==')'):
            if(len(st)!=0 and st[-1] =='('):
                st.pop()
            else:
                print(False)
                return
        elif(ch== '}'):
            if(len(st)!=0 and st[-1] =='{'):
                st.pop()
            else:
                print(False)
                return
        elif(ch== ']'):
            if(len(st)!=0 and st[-1] =='['):
                st.pop()
            else:
                print(False)
                return

    if(len(st)==0):
        print(True)
    else:
        print(False)


#=================================duplicate brackets

def duplicateBrackets(exp):

    st=[]
    for ch in exp:
        if(ch==')'):
            if(len(st)!=0 and st[-1]=='('):
                print(True)
                return
            else:
                while(len(st)!=0 and st[-1]!='('):
                    st.pop()
                st.pop()
        else:
            st.append(ch)
    print(False)

#===========================nge

def nge(arr):
    st=[]
    nge= [0]* len(arr)

    nge[-1]=-1
    st.append(arr[-1])

    for i in range(len(arr)-2,-1,-1):
        while(len(st)>0 and arr[i]>=st[-1]):
            st.pop()
        if(len(st)==0):
            nge[i]=-1
        else:
            nge[i]=st[-1]

        st.append(arr[i])

    return  nge

#==========stock span=====================

def stockSpan(arr):
    st=[]
    span=[0]* len(arr)
    # span[0]=1
    # st.append(0)
    for i in range(0,len(arr)):
        while(len(st)>0 and arr[i]>= arr[st[-1]]):
            st.pop()
        if(len(st)==0):
            span[i]=i+1
        else:
            span[i]=i-st[-1]
        st.append(i)

    return  span


#===========largest area histogram

def max_area_histogram(arr):
    st=[]
    n=len(arr)
    rb=[0]*n
    lb =[0]*n
    for i in range(n-1,-1,-1):
        while(len(st)>0 and arr[i]<=arr[st[-1]]):
            st.pop()
        if(len(st)==0):
            rb[i]=n
        else:
            rb[i]=st[-1]
        st.append(i)

    st=[]
    for i in range(0,n):
        while(len(st)>0 and arr[i]<=arr[st[-1]]):
            st.pop()
        if(len(st)==0):
            lb[i]=-1
        else:
            lb[i]=st[-1]
        st.append(i)
    maxArea=0
    for i in range(n):
        width=rb[i]-lb[i]-1
        area=arr[i]*width
        if(area>maxArea):
            maxArea=area
    print(maxArea)

#=================sliding window

def sldingWindow(arr,k):
    st=[]
    nge=[0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while(len(st)>0 and arr[i]>=arr[st[-1]]):
            st.pop()
        if(len(st)==0):
            nge[i]=len(arr)
        else:
            nge[i]=st[-1]
        st.append(i)

    for j in range(0,len(arr)-k+1):
        i=j
        while(nge[i]<j+k):
            i=nge[i]
        print(arr[i])




#================= infix evaluation==================
def precedence(op):
    if(op=='+' or op=='-'):
        return 1
    elif(op=='/' or op=='*'):
        return 2
def calculate(v1,v2,opr):
    if(opr=='+'):
        return v1+v2
    if(opr=='-'):
        return v1-v2
    if(opr=='*'):
        return v1*v2
    if(opr=='/'):
        return v1/v2

def evaluateExpression(exp):
    opr=[]
    oprnds=[]

    i=0
    while(i<len(exp)):
        ch=exp[i]

        if(ch=='('):
            opr.append(ch)
        elif(ch.isdigit()):
            oprnds.append(ord(ch)-ord('0'))
        elif(ch==')'):
            while(len(opr)>0 and opr[-1]!='('):
                val2=oprnds.pop()
                val1=oprnds.pop()
                op=opr.pop()
                #calculate
                res=calculate(val1,val2,op)
                oprnds.append(res)
            opr.pop()
        elif( ch=='+' or ch=='-' or ch=='*' or ch=='/'):
            while(len(opr)>0 and opr[-1]!='(' and precedence(ch)<=precedence(opr[-1])):
                val2=oprnds.pop()
                val1=oprnds.pop()
                op=opr.pop()
                #calculate
                res=calculate(va1l,val2,op)
                oprnds.append(res)
            opr.append(ch)
        i+=1

    while(len(opr)>0):
        val2=oprnds.pop()
        val1=oprnds.pop()
        op=opr.pop()
        #calculate
        res=calculate(val1,val2,op)
        oprnds.append(res)

    return oprnds[0]

#=============================infix conversion

def infixConversion(exp):
    pre=[]
    post=[]
    opr=[]

    for ch in exp:
        if(ch=='('):
            opr.append(ch)
        elif(ch.isalnum()):
            pre.append(ch)
            post.append(ch)
        elif(ch=='+'or ch=='-' or ch=='/' or ch=='*'):
            while(len(opr)>0 and opr[-1]!='(' and precedence(ch)<=precedence(opr[-1])):

                op=opr.pop()
                preval2=pre.pop()
                preval1=pre.pop()
                pre.append(op+preval1+preval2)

                postval2=post.pop()
                postval1=post.pop()
                post.append(postval1+postval2+op)
            opr.append(ch)
        elif(ch==')'):
            while(len(opr)>0 and opr[-1]!='('):
                op=opr.pop()
                preval2=pre.pop()
                preval1=pre.pop()
                pre.append(op+preval1+preval2)

                postval2=post.pop()
                postval1=post.pop()
                post.append(postval1+postval2+op)
            opr.pop()

    while(len(opr)>0):
        op=opr.pop()
        preval2=pre.pop()
        preval1=pre.pop()
        pre.append(op+preval1+preval2)

        postval2=post.pop()
        postval1=post.pop()
        post.append(postval1+postval2+op)
    print("pre "+pre[-1])
    print("post "+post[-1])

#====================Celebrity problem

def findCelebrity(arr):
    st=[]
    for i in range (len(arr)):
        st.append(i)

    while(len(st)>1):
        val1=st.pop()
        val2= st.pop()
        if(arr[val1][val2]==1):
            st.append(val2)
        else:
            st.append(val1)
    potCelebrity=st.pop()

    for i in range(len(arr)):
        if(i!=potCelebrity):
            if(arr[i][potCelebrity]==0 or arr[potCelebrity][i]==1):
                print("None")
                return
    print(potCelebrity)

def evaluateAndCovertPrefix(exp):
    vstack=[]
    infix=[]
    postfix=[]

    for i in range(len(exp)-1,-1,-1):
        ch=exp[i]
        if(ch=='/'or ch=='*' or ch=='+' or ch=='-'):
            v1=vstack.pop()
            v2=vstack.pop()
            val=     calculate(v1,v2,ch)
            vstack.append(val)

            in1=infix.pop()
            in2=infix.pop()
            inv="("+in1+ch+in2+")"
            infix.append(inv)

            post1=postfix.pop()
            post2=postfix.pop()
            post=post1+post2+ch
            postfix.append(post)
        else:
            infix.append(ch)
            postfix.append(ch)
            vstack.append(int(ch))

    print("calculated  value : "+str(vstack[-1]))
    print("infix   value : "+infix[-1])
    print("postfix  value : "+postfix[-1])
#============================================================
#============================================================

evaluateAndCovertPrefix("-+2/*6483")

# arr=[
#         [0,1,0,0],
#     [0,0,0,0],
#     [1,1,0,1],
#     [0,1,0,0]
# ]
# findCelebrity(arr)
# infixConversion("a+b/c")
# print(evaluateExpression("((1)-(-2)*(3))"))
# arr=[4,5,2,10,8,2]
# sldingWindow(arr,3)
# print(nge(arr))
# balancedBracket("{a+b}+c+d)")
# duplicateBrackets("(a+b+(c+d))")