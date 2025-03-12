import sys

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CalculatorStack:
    def __init__(self, head:Node = None):
        self.head = head
        self.size = 0 if head == None else 1
        
    def push(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        
    def pop(self):
        if self.head == None:
            return None
        
        returnee = self.head.data
        self.head = self.head.next
        self.size -= 1
        
        return returnee
    
    def peek(self):
        if self.head != None:
            return self.head.data
        else:
            return None
        

# TESTING STACK IMPLEMENTATION
'''
test = CalculatorStack(Node(15))
test.push(12)
test.push('i')

pointer = test.head
while pointer != None:
    print(pointer.data)
    pointer = pointer.next


print(test.pop())
print("**********************")

pointer = test.head
while pointer != None:
    print(pointer.data)
    pointer = pointer.next
    
print("****************")
print(test.peek())
'''

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    if b != 0:
        return a/b
    
doOp = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

prio = {
    "+": 1,
    "-": 1,
    "*": 0,
    "/": 0,
    None: 9999
}

# this implementation is a (slightly modified and probably misunderstood) version of the shunting yard alogrithm.
def main():
    shunt = CalculatorStack()
    postfix = CalculatorStack() # I'm pretty sure this is supposed to be a queue normally but since that doesn't seem to be allowed, we'll have to reverse this lol
    
    if len(sys.argv) != 2:
        print("need to have an expression as a single string!")
        exit(0)
    expression = sys.argv[1]
    
    # arrange into correct order of operations
    for char in expression:
        if char == '(':
            shunt.push(char)
            
        if char in doOp:
            if shunt.peek() in doOp and prio[char] > prio[shunt.peek()]:
                postfix.push(shunt.pop())
            shunt.push(char)    
                
        elif char == ')':
            while shunt.peek() != '(':
                postfix.push(shunt.pop())
                
            # and get rid of the closing bracket as well.
            if shunt.peek() == '(':
                shunt.pop()
                
        elif char.isnumeric():
            postfix.push(char)
            
    # Now reverse the postfix
    truePostfix = CalculatorStack()
    while postfix.size != 0:
        truePostfix.push(postfix.pop())
    
    # and finally, for some actual caclulations...
    numStack = CalculatorStack()
    while truePostfix.size != 0:
        
        if truePostfix.peek().isnumeric():
            numStack.push(truePostfix.pop())
        
        elif truePostfix.peek() in doOp:
            num2 = int(numStack.pop())
            num1 = int(numStack.pop())
            res = doOp[truePostfix.pop()](num1, num2)
            numStack.push(res)
            
    print(numStack.pop())
              
main()
        
