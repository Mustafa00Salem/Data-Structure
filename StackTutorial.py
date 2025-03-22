
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def __len__(self):
        return self.size
    def __repr__(self):
        items = []
        currect_item = self.top
        while currect_item is not None:
            items.append(str(currect_item.value))
            currect_item = currect_item.next
        return ', '.join(items)
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        pop_value = self.top.value
        self.top = self.top.next
        
        self.size -= 1
        return pop_value
    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        return self.top.value
    def is_empty(self):
        return self.top is None
    
    
if __name__  == '__main__':
    stack = Stack()
    
    stack.push(10)
    stack.push(12)
    stack.push(14)
    stack.push(16)
    stack.push(18)
    stack.push(19)
    print(stack)
    print(stack.peek())
    print(stack)
    
    print(stack.pop())
    print(stack)
    print(stack.is_empty())
    print(stack)
    