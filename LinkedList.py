
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head
            return_string = f'[{last.value}'
            
            while last.next:
                last = last.next
                return_string += f', {last.value}'
            return_string += ']'
                
            return return_string 

        
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False
    def __len__(self):
        last = self.head
        counter = 0 
        while last is not None:
            counter += 1
            last = last.next
    
        return counter
            
    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            self.size = 1
        else:
            last = self.head 
            while last.next:    
                last = last.next
            last.next = Node(value)
            self.size += 1
            
    def prepend(self,value):
        firs_node = Node(value)
        firs_node.next = self.head
        self.head = firs_node
    def insert(self,value , index):
        if index == 0: 
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError ('Index out of bound')
            else:
                last = self.head
                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError ('Index out of bound')
                    last = last.next
                    
                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node
                
    def delete(self , value):
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        last.next = last.next.next
                        break
                    last = last.next
                    
    def pop(self, index):
        if self.head is None:
            raise ValueError ('Index out of bound')
        else:
            last = self.head
            for i in range(index -1):
                if last.next is None:
                    raise ValueError ('Index out of bound')
                last = last.next
            if last.next is None:
                raise ValueError ('Index out of bound')
            else:
                last.next = last.next.next           
    def get(self, index):
        if self.head is None:
            raise ValueError ('Index out of bound')
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError ('Index out of bound')
                last = last.next
            return last.value
                



                
if __name__ == "__main__":
    ll =LinkedList()
    ll.append(12)
    ll.append(16)
    ll.append(8)
    ll.append(2)
    ll.append(7)
    ll.insert(198, 2)
    ll.delete(8)
    ll.pop(1)
    
    print(ll)
