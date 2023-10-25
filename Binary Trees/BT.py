from queue import Queue
class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

class Pair:
    def __init__(self,node=None,vis=None):
        self.node=node
        self.vis=vis

def construct(arr):
    st=[]
    root=Node(arr[0])
    rp=Pair(root,1)
    st.append(rp)
    idx=1

    while(len(st)>0):
        top=st[-1]

        if(top.vis==1):
            if arr[idx]!=None:
                lc=Node(arr[idx])
                top.node.left=lc
                p1=Pair(lc,1)
                st.append(p1)
            top.vis+=1
            idx+=1
        elif(top.vis==2):
            if(arr[idx]!=None):
                rc=Node(arr[idx])
                top.node.right=rc
                p2=Pair(rc,1)
                st.append(p2)
            top.vis+=1
            idx+=1
        else:
            st.pop()
    return root

def constructRec(arr,currIdx):
    if(currIdx==len(arr) or arr[currIdx]==None):
        return None,currIdx+1

    root=Node(arr[currIdx])
    #faith
    lc,index1=constructRec(arr,currIdx+1)
    rc,index2=constructRec(arr,index1)
    root.left=lc
    root.right=rc
    return root,index2

def display(root):
    if(root==None):
        return

    left= "." if root.left==None else str(root.left.data)
    right= "." if root.right==None else str(root.right.data)
    ans=left+"<-"+str(root.data)+"->"+right
    print(ans)
    #faith
    display(root.left)
    display(root.right)

def maxMinSize(root):

    #base
    if(root==None):
        return 0,float('-inf'),float('inf')

    #faith
    ls,lmax,lmin=maxMinSize(root.left)
    rs,rmax,rmin=maxMinSize(root.right)

    size=ls+rs+1
    maxans=max(lmax,rmax,root.data)
    minans=min(lmin,rmin,root.data)
    return size,maxans,minans

def levelorder(root):

    que=Queue()
    que.put(root)
    while(not que.empty()):
        # count=que.qsize()
        node=que.get()
        print(node.data,end=" ")
        if(node.left!=None):
            que.put(node.left)
        if(node.right!=None):
            que.put(node.right)
        print()

def traverslainprepost(root):
    st=[]
    rp=Pair(root,1)
    st.append(rp)
    pre, inOrder ,post="","",""
    while(len(st)>0):
        top=st[-1]
        if(top.vis==1):
            pre+= str(top.node.data)+" "
            top.vis+=1
            if(top.node.left!=None):
                lp=Pair(top.node.left,1)
                st.append(lp)
        elif(top.vis==2):
            inOrder+= str(top.node.data)+" "
            top.vis+=1
            if(top.node.right!=None):
                rp=Pair(top.node.right,1)
                st.append(rp)
        else:
            post+=str(top.node.data)+" "
            st.pop()
    print(pre)
    print(inOrder)
    print(post)

arr=[50,25,32,None,None,23,19,None,None,None,75,41,17,None,None,None,68,None,None]
root,ind=constructRec(arr,0)
traverslainprepost(root)