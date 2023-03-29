from linked import *
from doublelinked import *
from arraylist import *
import random

list = LinkedList()
list_d = DoubleLinkedList()
arraylist = ArrayList()


for i in range(6000):
    list.push(random.randint(0,100))
    list_d.push(random.randint(0,100))
    arraylist.push(random.randint(0,100))

print("Verkettet")
list.printList()
print("Doppelt Verkettet")
list_d.printList()
print("ArrayList")
arraylist.printList()
