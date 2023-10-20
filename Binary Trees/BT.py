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
        elif(top.state==2):
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
