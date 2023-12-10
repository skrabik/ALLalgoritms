weights = [6, 4, 3, 2, 5]
costs = [5, 3, 1, 3, 6]


def task_about_backpack(weights, costs, W):
    # W - вместимость рюкзака
    I = len(weights) # количество предметов

    dp = [[0 for i in range(W+1)] for i in range(I+1)]

    for i in range(1, I+1): # по всем предметам
        for x in range(W+1): # по всем возможным весам находящимся в рюкзаке
            if x >= weights[i-1]:
                dp[i][x] = max(dp[i-1][x], dp[i-1][x-weights[i-1]] + costs[i-1])
            else:
                dp[i][x] = dp[i-1][x]
    # for i in dp:
    #     print(i)
    return dp[-1][-1]

def opti_task_about_backpack(weights, costs, W):
    # W - вместимость рюкзака
    I = len(weights)  # количество предметов

    dp = [[0 for _ in range(W + 1)] for _ in range(2)]


    for i in range(1, I+1):  # по всем предметам
        dp.append([0 for _ in range(W + 1)])
        for x in range(W + 1):  # по всем возможным весам находящимся в рюкзаке
            if x >= weights[i - 1]:
                dp[1][x] = max(dp[0][x], dp[0][x-weights[i - 1]] + costs[i - 1])
            else:
                dp[1][x] = dp[0][x]
        dp.pop(0)
    # for i in dp:
    #     print(i)
    return dp[-2][-1]
print(task_about_backpack(weights, costs, 15))
print(opti_task_about_backpack(weights, costs, 15))
