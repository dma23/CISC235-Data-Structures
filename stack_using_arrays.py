""" 
Implmentation of Stack using built-in python list
"""

class Stack():

    def __init__(self):
        # initialize the stack as an list
        self.stack = []
    
    def isEmpty(self):
        # if the length of stack is 0, then it's empty and return True
        if len(self.stack) == 0: 
            return True
        # otherwise, return false 
        else:
            return False
    
    def push(self, data):
        # takes data as an input and inserts it into the top of the stack
        self.stack.insert(0, data)

    def pop(self):
        # returns the first element in the stack and removes it from the list 
        value = self.stack[0]
        self.stack = self.stack[1:]
        return value

    def top(self):
        # returns the first element in the stack
        return self.stack[0]
    
    def size(self):
        # returns the size of the stack
        return len(self.stack)

    def fullStack(self):
        # not required, only for testing purposes
        # returns the full list of values
        return self.stack

if __name__ == "__main__":
    stack = Stack()

    # returns True
    print("Is the stack empty? T/F ",stack.isEmpty())

    stack.push(10)
    
    stack.push(20)
    # returns 20
    print("The first value in the stack is: ", stack.top())
    # returns size = 2 
    print("The size of the stack is :", stack.size())
    # returns 20
    print("Popped: ", stack.pop())
    # returns size = 1
    print("The size of the stack is :", stack.size())

    stack.push(19)
    stack.push(36)
    stack.push(26)
    stack.push(53)
    stack.push(11)
    stack.push(32)
    # returns [32, 11, 53, 26, 36, 19, 10]
    print(stack.fullStack())
    # returns size = 7, top = 32
    print(stack.size(), stack.top())
    # returns 32
    print(stack.pop())
