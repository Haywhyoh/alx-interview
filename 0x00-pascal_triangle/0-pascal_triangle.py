#!/usr/bin/python3
"""Pascal Triangle"""

def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    pascal_list = [[1], [1, 1]]
    if n == 1:
        pascal_list = [1]
        return (pascal_list)
    if n == 2:
        return pascal_list
    for i in range(3, n+1):
        previous = pascal_list[-1]
        prev_len = len(previous)
        temp = list(range(prev_len + 1))
        for x in range(prev_len):
            if x == 0:
                temp[x] = previous[x]
            else:
                temp[x] = previous[x] + previous[x-1]
        temp[-1] = 1
        previous = temp
        pascal_list.append(temp)
    return pascal_list
