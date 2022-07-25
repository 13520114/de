sample_array = [
    # [4, 2, 3, 6, 7, 8, 1, 9, 5, 10],
    # [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]


def solution_001(array):
    start_row = 0
    start_col = 0
    end_row = len(array) - 1
    end_col = len(array[0]) - 1

    i = 0
    res = [None] * len(array) * len(array[0])

    while start_row <= end_row and start_col <= end_col:
        row = start_row
        col = start_col

        while col <= end_col and i < len(res):
            res[i] = array[row][col]
            i += 1
            col += 1
        col -= 1
        row += 1

        while row <= end_row and i < len(res):
            res[i] = array[row][col]
            i += 1
            row += 1
        row -= 1
        col -= 1

        while col >= start_col and i < len(res):
            res[i] = array[row][col]
            i += 1
            col -= 1
        col += 1
        row -= 1

        while row > start_row and i < len(res):
            res[i] = array[row][col]
            i += 1
            row -= 1
        col += 1
        row += 1

        start_row += 1
        start_col += 1
        end_row -= 1
        end_col -= 1

    return res


if __name__ == '__main__':
    print(solution_001(sample_array))
