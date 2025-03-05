import re

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CalculatorStack:
    def __init__(self, head:Node = None):
        self.head = head
        
    def push(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        
    def pop(self):
        if self.head == None:
            return None
        
        returnee = self.head.data
        self.head = self.head.next
        
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
ops = ['(', ')', '+', '-', '*', '/']

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

def main():
    operatorStack = CalculatorStack()
    numericStack = CalculatorStack()
    expression = input("Input a valid expression: ")
    
    for char in expression:
        if char in ops:
            operatorStack.push(char)
            expression = expression.replace(char, '')
            
    numberTokens = expression.split(" ")
    for token in numberTokens:
        numericStack.push(token)


main()
        
