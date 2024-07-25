#!/usr/bin/python3
"""A script pascal's triangle"""


def pascal_triangle(n):

    triangle_list = []

    if (n <= 0):
        return triangle_list

    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if (j == 0) or (j == i):
                temp_list.append(1)

            else:
                temp_list.append(
                    triangle_list[i-1][j-1] + triangle_list[i-1][j])

        triangle_list.append(temp_list)

    return triangle_list
