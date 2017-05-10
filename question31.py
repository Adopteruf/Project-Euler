import numpy as np

base = np.array([1, 2, 5, 10, 20, 50, 100, 200])
# dynamic programming first type and then certain number
def calculate_combination_dp(n):
    arr = np.zeros(n)
    for x in base:
        arr[x - 1] += 1
        for k in range(x + 1, n + 1):
            arr[k - 1] += arr[k - x - 1]
    return arr[-1]

print(calculate_combination_dp(200))