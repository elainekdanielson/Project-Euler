# Project Euler, Problem 18: Maximum Path Sum I
# Find the maximum total from top to bottom of the triangle

# each row of the triangle is a list within the following list
# the triangle has 15 rows
triangle = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

new_triangle_base = []

def two_tri_max(a, b, c):
    if a + b > a + c:
        return(a + b)
    else:
        return (a + c)

for entry in triangle[13]:
    new_triangle_base.append(two_tri_max(entry, triangle[14][triangle[13].index(entry)], triangle[14][triangle[13].index(entry) + 1]))

print(new_triangle_base)

for row_num in range(14):
    for entry_num in range(14 - row_num):
        triangle[13 - row_num][entry_num] = two_tri_max(triangle[13 - row_num][entry_num], triangle[13 - row_num + 1][entry_num], triangle[13 - row_num + 1][entry_num + 1])
    print(triangle[13 - row_num])

print("The maximum total from top to bottom of the triangle is ", triangle[0][0])
