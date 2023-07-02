#!/usr/bin/python3
"""
pascal triangle script
"""


def pascal_triangle(n):
    """
    this function generates list of pascal triangle of the input n.
    """
    Result = []
    if n == 0:
        return Result
    for i in range(1, n+1):
        row = [1]
        if len(row) == i:
            Result.append(row)
        else:
            prev_row = Result[-1]
            for a in range(1, i+1):
                try:
                    new = prev_row[a-1] + prev_row[a]
                    row.append(new)
                except IndexError:
                    new = prev_row[a-1] + 0
                    row.append(new)
                    Result.append(row)
                    break
    return Result
