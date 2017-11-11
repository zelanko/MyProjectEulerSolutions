def maxParentValueOf(max_path_sums, member_index):
    start = 0

    if member_index > 1:
        start = member_index - 1

    end = member_index + 1

    max_value = max(max_path_sums[start: end])

    return max_value

def maximumPathSum(iterable_of_iterable_of_ints):
    max_path_sums = [0]

    for iterable_of_ints in iterable_of_iterable_of_ints:
        new_max_path_sums = []
        for i, v in enumerate(iterable_of_ints):
            new_max_path_sums.append(v + maxParentValueOf(max_path_sums, i))
        
        max_path_sums = new_max_path_sums
    print(max(max_path_sums))

pyramid_of_values = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]

maximumPathSum(pyramid_of_values)
