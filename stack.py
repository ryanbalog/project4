'''
Project 4
CS2420
Ryan Balog
'''

class Node:
    '''creates node object to hold data'''

    def __init__(self, data, next):
        self.data = data
        self.next = next


class Stack:
    '''creates stack object to hold and access nodes'''

    def __init__(self):
        self.top = None
        self.list_size = 0

    def push(self, top):
        '''adds new node to top of stack'''
        self.top = Node(top, self.top)
        self.list_size += 1

    def pop(self):
        '''removes top node from stack, returns node's data'''
        if self.list_size <= 0:
            raise IndexError("Stack is empty, cannot pop an empty stack")
        item = self.top.data

        self.top = self.top.next
        self.list_size -= 1
        return item

    def peek(self):
        '''returns the top node's data without modifying stack'''
        if self.list_size <= 0:
            raise IndexError("Stack is empty, cannot peek an empty stack")
        return self.top.data

    def size(self):
        '''returns list_size of stack'''
        return self.list_size

    def clear(self):
        '''clears out stack, sending nodes out for garbage collection and setting list_size to 0'''
        self.list_size = 0
        self.top = None
