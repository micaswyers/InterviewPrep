def reverse_list(some_list):
    for i in range(len(some_list)/2):
        temp = some_list[i]
        some_list[i] = some_list[len(some_list)-1-i]
        some_list[len(some_list)-1-i] = temp
    return some_list

def reverse_list2(some_list):
    new_list = []
    while len(some_list):
        new_list.append(some_list.pop())
    return new_list

def reverse_list3(some_list):
    new_list = []
    for i in range((len(some_list)-1), -1, -1):
        new_list.append(some_list[i])
    return new_list

def reverse_string(some_string):
    chars = []
    for char in some_string:
        chars.append(char)
    chars = reverse_list(chars)
    new_string = ""
    for char in chars:
        new_string += char
    return new_string

def wordcount(list_of_words):
    d = {}
    for word in list_of_words:
        d[word] = d.get(word, 0) + 1
    l2 = []
    for word, count in d.iteritems():
        l2.append([word, count])
    return sorted(l2, key=lambda item: item[0])

def make_table(rows):
    html_table = "<table><tbody>"
    for row in rows:
        for item in row:
            html_table += "<tr><td>%s</td></tr>" % item
    html_table += "</tbody></table>"
    return html_table

def bubble_sort(some_list):
    for i in range(len(some_list)):
        for j in range(i+1, len(some_list)):
            if some_list[i] > some_list[j]:
                temp = some_list[i]
                some_list[i] = some_list[j]
                some_list[j] = temp
    return some_list    

def sort_files(some_list):
    #just what in the actual fuck is this problem?? 
    bs = []
    ks = []
    ms = []
    gs = []
    for item in some_list:
        if "K" in item:
            ks.append(item)
        elif "M" in item:
            ms.append(item)
        elif "G" in item:
            gs.append(item)
        else:
            bs.append(item)
    some_list = sorted(bs) + sorted(ks) + sorted(ms) + sorted(gs)
    return some_list

def print_primes(number):
    for i in range(2, (number + 1)):
        if is_prime(i):
            print i

def is_prime(number):
    if number <= 3:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
            else:
                return True
def find_anagrams(word, some_list):
    d = {}
    anagrams = []
    for letter in word:
        d[letter] = d.get(letter, 0) + 1
    for word in some_list:
        letters = {}
        for letter in word:
            letters[letter] = letters.get(letter, 0) + 1
        if letters == d:
            anagrams.append(word)
    return anagrams

def render_template(template, values):
    words = template.split()
    for pair in values:
        for word in words:
            if pair[0] == word.strip("{}"):
                word = pair[1]
    s = ""
    for word in words:
        s += word
    return s

template = "{name} uses {product}? I use {product} too!"
values = [["name", "John"], ["product", "vim"]]

#Recursion practice

#Multiple all items in a list
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    return l[0] * multiply_list(l[1:])

#Return n!
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

#Count all the elements in a list
def count_list(l):
    if len(l) == 0:
        return 0
    return 1 + count_list(l[1:])

#Sum all the elements in a list
def sum_list(l):
    if len(l) == 0:
        return 0
    return l[0] + sum_list(l[1:])

#Reverse a list without slicing or loops
def reverse_list(l):
    if len(l) == 1:
        return l
    temp = l.pop(0)
    return reverse_list(l) + [temp]

#Reverse a list recursively
def reverse_list2(l):
    if len(l) == 1:
        return l
    return [l[-1]] + reverse_list2(l[:-1])

#Determine if a string s is a palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

#Given the width (w), height (h) of a sheet of paper and the number of times (f) to fold it, return the final dimensions of the sheet as a tuple
def fold_paper(w,h,f):
    if f == 0:
        return (w,h)
    if w >= h:
        return fold_paper((w/2), h, (f-1))
    return fold_paper(w, (h/2), (f-1))

#Print all the #'s from n to a target
def count_up(target, n):
    if target == n:
        print target
    else:
        print n
        return count_up(target, n+1)


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    return l

def merge_sort(l):
    if len(l) == 1:
        return l
    left = []
    right = []
    for i in range(len(l)/2):
        left.append(l[i])
    print "LEFT ", left
    for j in range(len(l)/2, len(l)):
        right.append(l[j])
    print "RIGHT ", right

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(l1,l2):
    result = []
    while len(l1) > 0 or len(l2) > 0:
        print "l1 ", l1
        print "l2 ", l2
        if len(l1) > 0 and len(l2) > 0:
            if l1[0] <= l2[0]:
                result.append(l1[0])
                l1 = l1[1:]
            else:
                result.append(l2[0])
                l2 = l2[1:]
        elif len(l1) > 0:
                result.append(l1[0])
                l1 = l1[1:]
        else:
                result.append(l2[0])
                l2 = l2[1:]
        print "merged ", result
    return result

def print_list_recursively(l):
    if len(l) <= 1:
        return l[0]
    print l[0],
    return print_list_recursively(l[1:])

def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print item,
        print

def print_perimeter(matrix):
    for i in range(len(matrix[0])):
        print matrix[0][i],
    print

    for row in matrix[1:4]:
        print row[3]

    for i in range((len(m[4])-1),0,-1):
        print matrix[4][i],

    for row in matrix[4:0:-1]:
        print row[0]

#Given a matrix, print it along the diagonals (left to right)
def print_one_diagonal(m, row, col):
    while row >= 0 and col <= (len(m[0])-1):
        print m[row][col],
        row -= 1
        col += 1
    print

def print_matrix_diagonals(m):
    for i in range(len(m)):
        print_one_diagonal(m, i, 0)
    for j in range(1, len(m[0])):
        print_one_diagonal(m, len(m)-1,j)


l = [1,2,3,4,5]
l2 = [5,3,1,4,2]
m = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16], [17,18,19,20]]

print_perimeter(m)
