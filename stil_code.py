# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# index = 0
# while index < len(my_list):
#     if my_list[index] < 0:
#         break
#     elif my_list[index] > 0:
#         print(my_list[index])
#     index += 1

import names
from time import time

def decor(func,*args):
    ls = args[0]
    print('принял', ls)
    start = time()
    ans = func(*args)
    stop = time()
    if ans == None:
        ans = ls
    print('отдал', ans)
    print(stop-start)
    return ans

#0.1
def bubble_sort(ls, reverse = False):

    compare = (lambda x, y: x < y)
    if reverse:
        compare = (lambda x,y : x > y)

    swap = True
    while swap:
        swap = False
        for i in range(len(ls)-1):
            if compare(ls[i], ls[i+1]):
                ls[i], ls[i+1] =  ls[i+1],ls[i]
                swap = True

#0.03
def selection_sort(ls):
    for i in range(len(ls)): # i - кол проверенных символов
        low = i
        for j in range(i+1,len(ls)):
            if ls[low] > ls[j]:
                low = j
        ls[i],ls[low] = ls[low],ls[i]

#0.001
def quick_sort(ls):

    if len(ls) <= 1:
        return ls

    elem = ls[len(ls)//2]

    l = [i for i in ls if i < elem]
    m = [i for i in ls if i == elem]
    r = [i for i in ls if i > elem]
    return quick_sort(l) + m + quick_sort(r)

#0.03
def insert_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1

        while key < ls[j] and j >= 0:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = key


if __name__ == '__main__':
    book = [names.get_first_name() for i in range(1000)]
    book = decor(insert_sort,book)

    pass