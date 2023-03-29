class ListElement():
    def __init__(self, obj):
        self.obj = obj     
        self.next = None    
        self.prev = None   

class DoubleLinkedList():
    def __init__(self, head=None):
        self.head = head
        self.tail = head 
        self.count = 0

    def push(self, o):
        new_element = ListElement(o)
        
        if self.head is None:
            self.head = new_element
            self.tail = new_element  
        else:
            temp = self.tail
            temp.next = new_element
            new_element.prev = temp
            self.tail = new_element
            self.count += 1

    def printList(self):
        output = ""
        temp = self.head
        while temp is not None:
            output += str(temp.obj) + " "
            temp = temp.next
        
        print(output)

    

    

        

    
