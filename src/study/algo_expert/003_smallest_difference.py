array_one = [-1, 5, 10, 20, 28, 3]
array_two = [26, 134, 135, 15, 17]


def solution_001(arrayOne, arrayTwo):
    """ Time: O(N^2) | Space: O(N) """
    cur_min = None
    min_abs = []

    for a in arrayOne:
        for b in arrayTwo:
            if cur_min is None or cur_min > abs(a - b):
                cur_min = abs(a - b)
                min_abs = [a, b]

    return min_abs


def solution_002(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    one = 0
    two = 0
    min_diff = abs(arrayOne[one] - arrayTwo[two])
    min_pair = [arrayOne[one], arrayTwo[two]]
    while one < len(arrayOne) or two < len(arrayTwo):
        one_index = one
        two_index = two

        if one == len(arrayOne):
            one_index = one - 1
        if two == len(arrayTwo):
            two_index = two - 1

        cur_diff = abs(arrayOne[one_index] - arrayTwo[two_index])
        cur_pair = [arrayOne[one_index], arrayTwo[two_index]]

        if cur_diff < min_diff:
            min_diff = cur_diff
            min_pair = cur_pair

        if arrayOne[one_index] < arrayTwo[two_index]:
            if one < len(arrayOne):
                one += 1
            else:
                two += 1
            continue

        if arrayOne[one_index] > arrayTwo[two_index]:
            if two < len(arrayTwo):
                two += 1
            else:
                one += 1
            continue

        if arrayOne[one_index] == arrayTwo[two_index]:
            return [arrayOne[one_index], arrayTwo[two_index]]

    return min_pair


if __name__ == '__main__':
    # print(solution_001(array_one, array_two))
    print(solution_002(array_one, array_two))
