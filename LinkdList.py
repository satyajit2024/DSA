# # import pdb
# # pdb.set_trace()
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

#     def __repr__(self):
#         return f"{self.value} and {self.next}"


# a = Node(1)
# b = Node(2)
# c = Node(3)

# a.next = b
# b.next = c


# print(a)
# print(b)
# print(c)

# print("\n")

# print(a.next)
# print(b.next)
# print(c.next)

# print("\n")

# print(id(a))
# print(id(b))
# print(id(c))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value} and {self.next}"
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        # new_node
        new_node = Node(value)
        # new_node.next = self.head
        new_node.next = self.head
        self.head = new_node
        self.n += 1


l = LinkedList()
# print("Empty list:\n", L)
print(len(l))
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)

print(len(l))
