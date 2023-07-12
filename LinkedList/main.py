from typing import Any


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        first_node = Node(value)
        self.head = first_node
        self.tail = first_node
        self.len = 1
        
    def print_linked_list(self):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.next is not None:
                print(cur_node.value, "-> ", end="")
            else:
                print(cur_node.value, end= '')

            cur_node = cur_node.next
    
    def append(self, value):
        added_node = Node(value)
        # if there's no node in the linked list
        if self.tail is None:
            self.tail = added_node
            self.head = added_node
            self.len = 1
        else: 
            self.tail.next = added_node
            self.tail = added_node
            self.len += 1 
        return True
    
    def pop(self):
        if self.head is None:
            # if the linked list is empty
            print("linked list is empty so nothing to pop")
        elif self.head is self.tail:
            # if only one node in linked list
                self.head = None
                self.tail = None
                self.len -= 1
        else:
            cur_node = self.head
            while cur_node.next != self.tail:
                cur_node = cur_node.next
            
            cur_node.next = None
            self.tail = cur_node
            self.len -= 1
        return True
    
    def prepend(self, value):
        added_node = Node(value)
        if self.head is None:
            self.tail = added_node
        added_node.next = self.head
        self.head = added_node
        self.len += 1
        return True
    
    def pop_first(self):
        if self.len == 0:
            print("no node to pop")
        elif self.len == 1:
            return_node = self.head
            self.head = None
            self.tail = None
            self.len -= 1
        else:
            return_node = self.head
            self.head = self.head.next
            return_node.next = None
            self.len -= 1
        return return_node.value
    
    def get(self, idx):
        if idx < 0 or idx >= self.len:
            # check if idx is valid
            return False
        else:
            cur = self.head
            cnt = 0
            while cnt != idx: 
                cur = cur.next
                cnt += 1
        return cur
    
    def insert(self, idx, value):
        if idx < 0 or idx > self.len:
            # check if idx is valid
            return False
        else:
            if idx == 0:
                self.len += 1
                return self.prepend(value)
            elif idx == self.len:
                self.len += 1
                return self.append(value)
            else:
                added_node = Node(value)
                temp = self.head
                for _ in range(idx-1):
                   temp = temp.next 
                temp_next = temp.next
                temp.next = added_node
                added_node.next = temp_next
                self.len += 1

                return True
            
    def remove(self,idx):
        if idx < 0 or idx >= self.len:
            # if not successful, no node(None) will be returned.
            return None
        else:
            if idx == 0:
                self.len -= 1
                return self.pop_first(idx)
            elif idx == 0:
                self.len -= 1
                return self.pop_first(idx)  
            elif idx == (self.len - 1):
                self.len -= 1
                return self.pop(idx)  
            else:
                prev_rm_node = self.get(idx - 1)
                rm_node = prev_rm_node.next
                next_rm_node = rm_node.next
                prev_rm_node.next = next_rm_node
                rm_node.next = None
                self.len -= 1
                return rm_node
        
    def reverse(self):
        if self.len == 0:
            return True
        else:
            temp = self.head
            self.head = self.tail
            self.tail = temp
            before = None
            after = temp.next
            for _ in range(self.len):
                temp.next = before
                before = temp
                temp = after
                if after is not None:
                    after = after.next
                
                

               
# my_linked_list = LinkedList(11)
# my_linked_list.append(12)
# print(my_linked_list.pop_first())
# my_linked_list.prepend(1)


# # my_linked_list.pop()
# # my_linked_list.pop()

# my_linked_list.print_linked_list()

# print(my_linked_list.head.value)
# print(my_linked_list.tail.value)
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()


my_linked_list.print_linked_list()
