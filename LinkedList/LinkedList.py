class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class LinkedList:
    def __init__(self,head=None):
        self.head=None

    def addLast(self,val):
        ptr=self.head
        newNode=Node(val)
        if(self.head==None):
            self.head=newNode
        else:
            while(ptr.next!=None):
                ptr=ptr.next
            ptr.next=newNode

    def displayList(self):
        ptr=self.head
        while(ptr!=None):
            print(ptr.val,end="->")
            ptr=ptr.next
        print()
    def removeFirst(self):
        if(self.head==None):
            return
        newHead=self.head.next
        oldHead=self.head
        oldHead.next=None
        self.head=newHead

    def addFirst(self,val):
        newNode=Node(val)
        newNode.next=self.head
        self.head=newNode

    def removeLast(self):
        if(self.head==None or self.head.next==None):
            self.head=None
            return
        ptr=self.head
        while(ptr.next.next!=None):
            ptr=ptr.next
        ptr.next=None

    def getLast(self):
        if (self.head==None):
            return None
        ptr=self.head
        while(ptr.next!=None):
            ptr=ptr.next
        return ptr

    def getFirst(self):
        head=self.head
        if(head==None):
            return None
        if(head!=None):
            return head

    def getAt(self,pos):
        if(pos<0 or self.head==None):
            return None
        ptr=self.head
        count=0
        while(ptr!=None and count<pos):
            ptr=ptr.next
            count+=1

        if(ptr!=None):
            return ptr
        else:
            return None

    def addAt(self,val,pos):
        if(pos==0):
            newNode=Node(val)
            self.head=newNode
            return

        if(pos<0 or self.head==None):
            return

        curr=self.head
        prev=None
        count=0
        while(curr!=None and count<pos):
            prev=curr
            curr=curr.next
            count+=1
        if(curr!=None):
            newNode=Node(val)
            prev.next=newNode
            newNode.next=curr

    def removeAt(self,pos):
        if(pos<0 or self.head==None):
            return
        if(pos==0):
            self.head=self.head.next
        curr=self.head
        prev=None
        count=0
        while(curr!=None and count<pos):
            prev=curr
            curr=curr.next
            count+=1
        if(curr!=None):
            prev.next=curr.next
            curr.next=None

    def getLength(self):
        if(self.head==None):
            return 0
        ptr=self.head
        count =0
        while(ptr!=None):
            count+=1
            ptr=ptr.next
        return count

    def reverseDI(self):
        li=0
        ri=self.getLength()-1

        while(li<ri):
            left=self.getAt(li)
            right=self.getAt(ri)

            temp=left.val
            left.val=right.val
            right.val=temp
            li+=1
            ri-=1

    #def reversePI(self):

    def getKthFromLast(self,k):
        if(k<1):
            return

        curr=self.head
        prev=self.head

        for i in range(k):
            if(curr==None):
                return
            curr=curr.next

        while(curr!=None):
            curr=curr.next
            prev=prev.next
        return prev.val

    def getMid(self):
        if(self.head==None):
            return
        ptr1=self.head
        ptr2=self.head

        while(ptr1!=None and ptr1.next!=None):
            ptr1=ptr1.next.next
            ptr2=ptr2.next

        return ptr2

    def mergeTwoLinkedList(self,l2):

        ansList=LinkedList()
        ptr1=self.head
        ptr2=l2.head

        while(ptr1!=None and ptr2!=None):
            if(ptr1.val<ptr2.val):
                ansList.addLast(ptr1.val)
                ptr1=ptr1.next
            else:
                ansList.addLast(ptr2.val)
                ptr2=ptr2.next

        while(ptr1!=None):
            ansList.addLast(ptr1.val)
            ptr1=ptr1.next
        while(ptr2!=None):
            ansList.addLast(ptr2.val)
            ptr2=ptr2.next
        return ansList

    def removeDuplicates(self):
        ans=LinkedList()
        while(self.getFirst()!=None):
            val=self.getFirst().val
            self.removeFirst()
            if(ans.head==None or val!=ans.getLast()):
                ans.addLast(val)

        self.head=ans.head

    def oddEven(self):
        odd=LinkedList()
        even=LinkedList()
        while(self.head!=None):
            val=self.getFirst().val
            self.removeFirst()
            if(val%2==0):
                even.addLast(val)
            else:
                odd.addLast(val)

        if(odd.head!=None and even.head!=None):
            odd.getLast().next=even.head
            self.head=odd.head
        elif odd.head!=None:
            self.head=odd.head
        elif even.head!=None:
            self.head=even.head

    def loopNode(self):
        slow=self.head
        fast=self.head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(fast==slow):
                break

        if(fast==None or fast.next==None):
            return None

        fast=self.head

        while(fast!=slow):
            fast=fast.next
            slow=slow.next

        return slow




def intersection(ll1,ll2):
    l1=ll1.getLength()
    l2=ll2.getLength()
    ptr1=ll1.head
    ptr2=ll2.head
    diff=abs(l1-l2)
    if(l1>l2):
        while(diff!=0):
            ptr1=ptr1.next
            diff-=1
    else:
        while(diff!=0):
            ptr2=ptr2.next
            diff-=1

    while(ptr1!=None and ptr2!=None and ptr1!=ptr2):
        ptr1=ptr1.next
        ptr2=ptr2.next

    return ptr1

def displayReverse(h1):
    if(h1==None):
        return
    #faith
    displayReverse(h1.next)
    print(h1.val,end="->")


def getMid(l1):
    if(l1.head==None):
        return
    ptr1=l1.head
    ptr2=l1.head

    while(ptr1.next!=None and ptr1.next.next!=None):
        ptr1=ptr1.next.next
        ptr2=ptr2.next

    return ptr2


def mergeSortLinkedList(l1):
    if(l1.head==None or l1.head.next==None):
        return l1

    midNode=getMid(l1)

    leftPart=LinkedList()
    leftPart.head=l1.head
    rightPart=LinkedList()
    rightPart.head=midNode.next
    midNode.next=None

    leftHalf=mergeSortLinkedList(leftPart)
    rightHalf=mergeSortLinkedList(rightPart)

    sortedList=leftHalf.mergeTwoLinkedList(rightHalf)
    return sortedList



l1=LinkedList()
l1.addLast(13)
l1.addLast(14)
l2=LinkedList()
l2.addLast(11)
l2.addLast(10)
l2.addLast(9)
l2.addLast(8)
l2.addLast(7)

l3=LinkedList()
l3.addLast(2)
l3.addLast(3)
l3.addLast(4)
l3.addLast(5)
l3.addLast(6)

l1.getLast().next=l3.head
l2.getLast().next=l3.head
l3.getLast().next=l2.head

print(l1.loopNode().val)


# res=intersection(l1,l2)

# if(res!=None):
#     print(res.val)
# l1.removeDuplicates()
# l1.oddEven()
# l1.displayList()
# ans=mergeSortLinkedList(l1)
# ans.displayList()

