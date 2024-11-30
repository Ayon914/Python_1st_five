class Stack:
    def __init__(self):
        self.stack = []
 
    def is_empty(self):
        return len(self.stack) == 0
    def push(self,item):
        self.stack.append(item)
        print(f"{item} Pushed to stack")
 
    def pop(self):
        if self.is_empty():
            return "The Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "The Stack is empty"
        return self.stack[-1]
    def size(self):
        return len(self.stack)
 
 
 
 
 
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(150)
 
stack1 = Stack()
stack1.push(30)
 
print("Top element of stack1 is:", stack1.peek())
print("Top element is:", stack.peek())
print("Stack size is:", stack.size())
print("Popped element :", stack.pop())
print("Stack is empty:", stack.is_empty())
 