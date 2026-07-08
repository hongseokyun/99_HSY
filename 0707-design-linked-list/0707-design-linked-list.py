from collections import deque

class MyLinkedList(object):

    def __init__(self):
        self.q = deque()
        
    def get(self, index):
        if len(self.q) > abs(index):
            return self.q[index]
        else :
            return -1
        
    def addAtHead(self, val):
        self.q.appendleft(val)
    
    def addAtTail(self, val):
        self.q.append(val)
        
    def addAtIndex(self, index, val):
        if index > len(self.q):
            return
        if index < 0:
            index = 0
        lst = list(self.q)
        lst.insert(index, val)
        self.q = deque(lst)

    def deleteAtIndex(self, index):
        if len(self.q) > abs(index):
            del self.q[index]
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)