#1.1 Implement an algorithm to determine if a string has all unique characters.
def all_unique(some_string):
    chars = {}
    for char in some_string:
        if not chars.get(char):
            chars[char] = chars.get(char, "here")
        else:
            return False
    return True

#What if you can't use additional data structures?
def all_unique2(some_string):
    for i in range(len(some_string)):
        char = some_string[i]
        for j in range(i+1, len(some_string)):
            if char == some_string[j]:
                return False
    return True

#Now, with faster run-time (but more memory usage)
def all_unique3(some_string):
    chars = [False] * 256
    for char in some_string:
        if chars[ord(char)]:
            return False
        else:
            chars[ord(char)] = True
    return True 

#Similar problem : Given a list of integers containing one duplicate. The maximum value in the list is the length of the list-1 [Could be an arbitrarily chosen upper bound.]. Return the value of the duplicate item.
def unique_list(list_of_ints):
    items = [False] * (len(list_of_ints) - 1)
    for item in list_of_ints:
        if items[item-1]:
            return item
        else:
            items[item-1] = True
    return "No duplicates found."

def unique_list2(list_of_ints):
    list_total = sum(list_of_ints)
    consecutive_total = sum(range(max(list_of_ints)+1))
    duplicate = list_total - consecutive_total
    return duplicate

#1.2 Write code to reverse a C-style string
def reverse_Cstring(some_Cstring):
    chars = []
    for char in some_Cstring:
        chars.append(char)
    null = chars.pop()
    for i in range(len(chars)/2):
        temp = chars[i]
        chars[i] = chars[len(chars) - 1 - i]
        chars[len(chars) - 1 - i] = temp
    chars.append(null)
    new_Cstring = ""
    for char in chars:
        new_Cstring += char
    return new_Cstring

#1.3 Remove duplicates from a string with no additional buffer (Extra variables are permitted; a copy of the string is not.)

def remove_duplicates(some_string):
    i = 0
    while i < len(some_string): #use a while-loop to avoid length-of-list errors 
        some_string = some_string[:i+1] + some_string[i:].replace(some_string[i], "")
        i += 1
    return some_string

def remove_duplicates2(some_string):
    #probably not valid -- recreated the string with unique characters
    holder = ""
    for i in range(len(some_string)):
        if some_string[i] not in holder:
            holder += some_string[i]
    return holder

#1.4 Decide if two strings are anagrams or not
def is_anagram(s1, s2):
    chars1 = {}
    chars2 = {}
    for char in s1.lower(): #Consider case
        chars1[char] = chars1.get(char, 0) + 1
    for char in s2.lower():
        chars2[char] = chars2.get(char, 0) + 1
    if chars1 == chars2:
        return True
    return False

def is_anagram2(s1,s2):
    return list(s1.lower()).sort() == list(s2.lower()).sort()

#1.5 Write a method to replace all spaces in a string with "%20"
def replace_spaces(some_string):
    new_string = ""
    for char in some_string:
        if char == " ":
            new_string += "%20"
        else:
            new_string += char
    return new_string

#1.6 Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rote the image by 90 degrees.
def rotate_matrix_CW(some_matrix):
    n = len(some_matrix)
    new_matrix = []
    for i in range(0,n):
        row = []
        for j in range((n-1), -1, -1):
            row.append(some_matrix[j][i])
        new_matrix.append(row)
    return new_matrix

def rotate_matrix_CCW(some_matrix):
    n = len(some_matrix)
    new_matrix = []
    for i in range((n-1), -1, -1):
        row = []
        for j in range(0,n):
            row.append(some_matrix[j][i])
        new_matrix.append(row)
    return new_matrix
#Can you do it in place? 

#1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
def set_to_zero(some_matrix):
    rows = []
    columns = []
    for i in range(len(some_matrix)):
        row = some_matrix[i]
        for j in range(len(row)):
            if row[j] == 0:
                rows.append(i)
                columns.append(j)
    for i in range(len(some_matrix)):
        if i in rows:
            some_matrix[i] = [0] * len(some_matrix[i])
        else:
            for j in columns:
                some_matrix[i][j] = 0
    return some_matrix

#Chapter 2 - Creating a linked list

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list(object):
    def __init__(self):
        self.head = None

    def delete_node(self, deprecated_node):
        #Should I do this with current.next or make a previous variable?
        if self.head:
            current = self.head
            if current == deprecated_node:
                self.head = current.next 
                print "I deleted the head."
            while current.next:
                print "I found a node"
                if current.next == deprecated_node: 
                    current.next = deprecated_node.next
                    print "I deleted a node."
                else:
                    current = current.next
            print "I got to the end."
        else:
            print "There is nothing to delete."

    def append_node(self, new_node):
        if self.head:
            current = self.head
            print "Looking at the head node."
            while current.next:
                current = current.next
                print "Moving to the next node."
            print "I got to the end of the list."
            current.next = new_node
            print "I added the new node to the end of the list."
        else:
            self.head = new_node
            print "There wasn't a head, so the new node is the head now."

    def remove_duplicates(self):
        seen_data = []
        if not self.head:
            print "This linked list has no head."
        else:
            current = self.head
            seen_data.append(current.data)
            print "I'm currently looking at the head of the linked list."
            while current.next:
                if current.next.data in seen_data:
                    print "The next node has already been seen."
                    current.next = current.next.next
                else:
                    seen_data.append(current.next.data)
                    print seen_data
                    current = current.next
                    print "Moving to the next node."
            print "I got to the end."

    def count_length(self):
        if self.head:
            length = 1
            current = self.head
            while current.next:
                current = current.next
                length += 1
            return length
        else:
            return 0

    def retrieve_nth_from_last(self, n):
        length = self.count_length()
        if length < n:
            print "Nope, that's not going to work."
        elif n <= 0:
            print "Negatives & 0 are confusing. Go eat a sandwich."
        else: 
            if self.head:
                current = self.head
                while length > n:
                    current = current.next
                    length -= 1
                return current.data
            else:
                return "This list has no head."

    def remove_node(self, n): #with only access to that node
        n.data = n.next.data
        n.next = n.next.next

    def find_last(self):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            last = current
            return last

    def reverse(self):
        # head = self.head
        last = self.find_last()
        while self.head != last:
            temp_head = self.head
            self.head = self.head.next
            temp_head.next = last.next
            last.next = temp_head
            self.print_list()
            print "*****"

    def reverse2(self): #now with recursion
        if self.next == None:
            return self.data
        else:
            current = self.head
            node = current
            if node.next.next == None:
                temp = node
                node = node.next
                node.next = temp
            else:
                self.reverse2()



    def print_list(self):
        if self.head:
            current = self.head
            while current.next:
                print current.data
                current = current.next
            print current.data

    def print_backwards(self):
        if self.head:
            current = self.head
            current.last = None
            while current.next:
                temp = current
                current = current.next
                current.last = temp
            print current.data
            while current.last:
                print current.last.data
                current = current.last

#Working with trees:
class Node = 

#Testing things hurr.

a = Node("a")
b = Node("b")
d = Node("d")
o = Node("o")
m = Node("m")
e = Node("e")
n = Node("n")
a.next = b
b.next = d
d.next = o
o.next = m
m.next = e
e.next = n

abdomen = Linked_list()
abdomen.head = a
