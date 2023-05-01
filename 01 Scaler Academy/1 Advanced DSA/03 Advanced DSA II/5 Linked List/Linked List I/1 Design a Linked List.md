### Design a Linked List;

### Problem Description

Design and implement a Linked List data structure.
A node in a linked list should have the following attributes - an integer value and a pointer to the next node. It should support the following operations:

insert_node(position, value) - To insert the input value at the given position in the linked list.
delete_node(position) - Delete the value at the given position from the linked list.
print_ll() - Print the entire linked list, such that each element is followed by a single space.
Note:

If an input position does not satisfy the constraint, no action is required.
Each print query has to be executed in a new line.

```

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return self.val

class LinkedList:
    def __init__(self):
        self.head = None
        self.ll_len = 0

    def __repr__(self):
        n = self.head
        nodes = []
        while n:
            nodes.append(str(n.val))
            n = n.next
        return ' '.join(nodes)

    def __get_node(self, index):
        if index == 0:
            return None, self.head
        else:
            prev = None
            cur = self.head
            while index > 0:
                prev = cur
                cur = cur.next
                index -= 1
            return prev, cur

    def insert_at(self, index, val):
        if index > self.ll_len:
            return
        p, c = self.__get_node(index)
        if not p and not c:
            self.head = ListNode(val)
        else:
            new = ListNode(val)
            if not p:
                new.next = c
                self.head = new
            else:
                temp = p.next
                p.next = new
                new.next = temp
        self.ll_len += 1
    
    def delete_at(self, index):
        if index >= self.ll_len:
            return
        else:
            dummy = prev = ListNode(0)
            prev.next = self.head
            cur = self.head
            while index:
                prev = cur
                cur = cur.next
                index -= 1
            prev.next = cur.next
            self.head = dummy.next
            self.ll_len -= 1

ll = LinkedList()

def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    ll.insert_at(position-1, value)

def delete_node(position):
    # @param position, integer
    # @return an integer
    ll.delete_at(position-1)


def print_ll():
    # Output each element followed by a space
    print(ll.__repr__())


```

Similar Problem -- 

https://leetcode.com/problems/design-linked-list/
