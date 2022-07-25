sample_array = [12, 3, 1, 2, -6, 5, -8, 6]
sample_target_sum = 0


def solution_001(array, target_sum):
    """ Time: O(N^3) | Space: O(N) """
    res = []
    array.sort()
    for a in range(len(array) - 2):
        for b in range(a + 1, len(array) - 1):
            for c in range(b + 1, len(array)):
                if array[a] + array[b] + array[c] == target_sum:
                    res.append([array[a], array[b], array[c]])
    return res


def solution_002(array, target_sum):
    """ Time: O(N^2) | Space O(N) """
    res = []
    array.sort()

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            cur_sum = array[i] + array[left] + array[right]
            if cur_sum < target_sum:
                left += 1
                continue
            if cur_sum > target_sum:
                right -= 1
                continue

            res.append([array[i], array[left], array[right]])
            left += 1

    return res


if __name__ == '__main__':
    # print(solution_001(sample_array, sample_target_sum))
    print(solution_002(sample_array, sample_target_sum))

