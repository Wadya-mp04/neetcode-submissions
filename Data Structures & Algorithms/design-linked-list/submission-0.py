class node:

    def __init__(self,value):
        self.val = value
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.right = node(0)
        self.left = node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index>0:
            cur = cur.next
            index-=1
        if cur != self.right and cur and index == 0:
            return cur.val
        return -1
    
    def addAtHead(self, val: int) -> None:
        head = self.left.next
        new = node(val)
        head.prev = new
        self.left.next = new
        new.next = head
        new.prev = self.left
        

    def addAtTail(self, val: int) -> None:
        tail = self.right.prev
        new = node(val)
        tail.next = new
        self.right.prev = new
        new.next = self.right
        new.prev = tail

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        new = node(val)
        while cur and index>0:
            cur = cur.next
            index-=1
        if cur and index == 0:
            new.prev = cur.prev
            new.next = cur
            cur.prev.next = new
            cur.prev = new

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index>0:
            cur = cur.next
            index-=1
        if cur != self.right and cur and index == 0:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur.prev = None
            cur.next = None
            del cur


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)