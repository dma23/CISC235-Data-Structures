class linkedList:

    # initializes a linkedlist
    def __init__(self, data=None):
        self.data = data
        self.next = None
    

    class Stack:

        def __init__(self):
            # initializes the head/first node of the stack 
            self.head = None

        def isEmpty(self):
            # if there is no value in the head, there are no nodes
            if self.head == None:
                return True
            else:
                return False

        def push(self, x):
            # if there are no nodes, create the first one
            if self.isEmpty() == True:
                self.head = linkedList(x)
            # otherwise, create a new node. Connect the old head node to the tail (next) of the new head
            else:
                new = linkedList(x)
                new.next = self.head
                self.head = new
            
        def pop(self):
            # remove and return the head node
            if self.isEmpty() == True:
                return None
            # save the data in a variable, set the next node to the new head node
            else:
                data = self.head.data
                self.head = self.head.next
                return data

        def top(self):
            # return the data from the head node
            return self.head.data

        def size(self):
            # returns the size of the linkedlist
            temp = self.head
            count = 0
            # searches through each node until there is no next (i.e. next = None)
            while(temp != None):
                count += 1
                temp = temp.next
            return count

if __name__ == '__main__':

    # initializes a new object
    a = linkedList.Stack()
    # adds 21
    a.push(21)
    # displays top node = 21
    print(a.top())
    # add 22
    a.push(22)
    # display head node 22
    print(a.top())
    # add 23
    a.push(23)
    # take out 23
    b = a.pop()
    print(b)
    # returns size = 2
    print(a.size())
