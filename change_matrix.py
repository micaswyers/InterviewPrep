def make_zeros(list_of_lists):
    columns = []
    rows = []
    for i, sublist in enumerate(list_of_lists):
        if 0 in sublist:
            rows.append(i)
        for j, elem in enumerate(sublist):
                if elem == 0:
                    columns.append(j)
    new_list_of_lists = []
    for i, sublist in enumerate(list_of_lists):
        if i in rows:
            new_list_of_lists.append([0] * len(sublist))
        else:
            new_list_of_lists.append(list(sublist))
    for i, sublist in enumerate(new_list_of_lists):
        for i in columns:
            if sublist[i] != 0:
                sublist[i] = 0 
    return new_list_of_lists

def make_zeros2(list_of_lists):
    columns = []
    new_list_of_lists = []
    for i, sublist in enumerate(list_of_lists):
        new_sublist = []
        if 0 in sublist:
            new_sublist = [0] * len(sublist)
        else:
            new_sublist = list(sublist)
        for j, elem in enumerate(sublist):
            if elem == 0:
                columns.append(j)
        for i in columns:
            new_sublist[i] = 0
        new_list_of_lists.append(new_sublist)
    return new_list_of_lists

#try changing in-place

def make_zeros3(list_of_lists, columns=set()): #now with recursion!
    if len(list_of_lists) == 0:
        return list_of_lists
    new_list_of_lists = []

    sublist = list_of_lists[0]
    new_sublist = []
    if 0 in sublist:
        new_sublist = [0] * len(sublist)
    else:
        new_sublist = list(sublist)
    for j, elem in enumerate(sublist):
        if elem == 0:
            columns.add(j)

    new_list_of_lists = [new_sublist] + make_zeros3(list_of_lists[1:], columns)

    for i in columns:
        new_sublist[i] = 0

    return new_list_of_lists

#remove for-loops from make_zeros3 --> All recursion, all the time (Create helper-function for sublists that is itself recursive )
