sample_array = [2, 1, 2, 2, 2, 3, 4, 2]
sample_to_move = 2


def solution_001(array, toMove):
    """ Time: O(N) | Space: O(1) """
    left = 0
    right = len(array) - 1
    cur_index = 0

    while left < right:
        if array[left] != toMove:
            array[cur_index] = array[left] + array[cur_index]
            array[left] = array[cur_index] - array[left]
            array[cur_index] = array[cur_index] - array[left]
            cur_index += 1
        left += 1
    return array


if __name__ == '__main__':
    print(solution_001(sample_array, sample_to_move))
