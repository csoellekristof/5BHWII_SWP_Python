
#Objekt die die Listenelemente abbildet
class ListElement():

    def __init__(self, obj):
        self.obj = obj     
        self.next = None    

class LinkedList():
    #Konstruktor
    def __init__(self, head = None):
        self.head = head
        self.count = 0

    #Element am Ende der Liste hinzufügen
    def push(self, o):
        new_element = ListElement(o)
        
        if self.head == None:
            self.head = new_element
        
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            temp.next = new_element
            self.count += 1

    #Alle Elemente ausgeben
    def printList(self):
        output = ""
        temp = self.head
        while temp != None:
            output += str(temp.obj) + " "
            temp = temp.next
        
        print(output)

    

    

        

    
