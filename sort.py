def greatest_in(t):
    res=t[0]
    for element in t:
        if element>res:
            res=element
    return res

def remove(t,i):
    res=[0](len(t)-1)
    for j in range (len(t)):
        if j<i:
            res [j]=t[j]
        if j>i:
            res [j-1]=t[j]
    return res

def my_selection_sort(t):
    res=[0]len(t)
    for i in range (len(t)):
        j=t[index_of_the_smallest(t)]
        res[i]=t[j]
        remove(t,i)
    return res

def selection_sort_in_place(t):
    for index in range (len(t))
        s=index_of_the_smallest_in(t,index,len(t)-1)
        if s>index:
            swap(t,index,s)
        return null

def insertion_sort_in_place(t):
    for index in range (1,len(t)):
        insert(t,index)
    return null

def insert (t,index):
    for current_index in range (index-1,-1,-1)
        if t[current_index]>t[current_index+1]
            swap (t,current_index,current_index-1)
        else:
            break
