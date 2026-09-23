class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index):
            if curr == None:
                return -1
            
            curr = curr.next
        if curr == None:
            return -1
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        currHead = self.head
        newHead = Node(val, currHead)
        self.head = newHead
        if self.tail == None:
            self.tail = self.head
        self.length += 1
        


    def addAtTail(self, val: int) -> None:
        currTail = self.tail
        if currTail == None:
            currTail = self.head
        newTail = Node(val, None)

        currTail.next = newTail
        self.tail = newTail
        self.length += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next

            currNext = curr.next
            curr.next = Node(val, currNext)

            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        print("before")
        self.printList()
        if index == 0:
            oldHead = self.head
            self.head = self.head.next
            oldHead.next = None
            
        
        elif index == self.length - 1:
            curr = self.head
            while curr.next.next != None:
                curr = curr.next
            
            self.tail = curr
            curr.next = None

        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            print(index)
            print(curr.val)
            currNext = curr.next.next
            curr.next = currNext

        self.length -= 1
        print("after")
        self.printList()
            
    def printList(self):
        curr = self.head
        length = 0
        while curr != None:
            print(curr.val, end=" ")
            curr = curr.next
            length += 1
        print()
        print("length:" + str(length))
        print("length2 " + str(self.length))

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)