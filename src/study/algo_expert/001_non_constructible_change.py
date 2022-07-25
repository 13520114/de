sample_coins = [5, 7, 1, 1, 3, 22]


def solution_001(coins):
    cur_min = 0
    coins.sort()
    print(coins)

    for i in range(len(coins)):
        if coins[i] <= cur_min + 1:
            cur_min += coins[i]
            continue
        break

    return cur_min + 1


if __name__ == '__main__':
    print(solution_001(sample_coins))
