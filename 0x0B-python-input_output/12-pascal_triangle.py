#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows for Pascal's triangle.

    Returns:
        list of lists: The Pascal's triangle as a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    n = 5
    triangle = pascal_triangle(n)

    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
