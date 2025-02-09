import Spaceship

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def delfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def dellast(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


# TODO : Write function insert_at_index to insert a new node at any given index. Consider all edge cases, including missing nodes.
    def insert_at_index(self, index, value):
        # IF OUT OF BOUNDS, DON'T MODIFY
        if index < 0 or index > self.length:
            return False
        # ADDS NEW VALUE
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        # MODIFIES LIST
        new_node = Node(value)
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

# TODO : Write function delete_at_index to delete a new node at any given index. Consider all edge cases, including missing nodes.
# Make sure to reuse existing function for the correct edge cases for both TODOs
# Write appropriate test function below to test for the new functions.
    def delete_at_index(self, index):
        # CHECKS BOUNDS
        if index < 0 or index >= self.length:
            return None
        # DELETES VALUE
        if index == 0:
            return self.delfirst()
        if index == self.length - 1:
            return self.dellast()

        # MODIFIES LIST
        prev = self.head
        for j in range(index - 1):
            prev = prev.next
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


s1 = Spaceship.Spaceship("Voyager", 300)
s2 = Spaceship.Spaceship("Enterprise", 300)
s3 = Spaceship.Spaceship("Atlantis", 300)
s4 = Spaceship.Spaceship("Challenger", 300)
s5 = Spaceship.Spaceship("Artemis", 300)

mylinkedlist = LinkedList(s1)
# FIRST LIST
mylinkedlist.append(s2)
mylinkedlist.append(s3)
mylinkedlist.prepend(s4)
mylinkedlist.prepend(s5)
mylinkedlist.print_list()
print("\n")

# TEST CASE W/ INSERT INDEX
mylinkedlist.insert_at_index(1, Spaceship.Spaceship("RANDOM", 200))
mylinkedlist.print_list()
print("\n")
# Expected: Artemis → Challenger → Voyager → Enterprise → Atlantis

# TEST CASE W/ DELETE INDEX
mylinkedlist.delete_at_index(2)
mylinkedlist.print_list()
# Expected: Artemis → Challenger → Enterprise → Atlantis

