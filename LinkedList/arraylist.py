import copy
class ArrayList:
    def __init__(self):
        self.list = []

    def push(self, o):
        new_list = copy.deepcopy(self.list) + [0]
        if(len(new_list) == 0):
            new_list[0] = o
        else:
            new_list[len(new_list)-1] = o
        self.list = new_list
    def printList(self):
        output = ""
        for e in self.list:
            output += str(e) + " "
        print (output)