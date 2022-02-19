# knapsack with memoization
def knapsack(values, weights, capacity):
    memo = [[None] * (capacity+1)] * len(values)

    return recurse(values, weights, capacity, 0, memo)


def recurse(v, w, c, i, memo):
    if c <= 0 or i >= len(w):
        return 0
    if memo[i][c] != None:
        return memo[i][c]

    profitWith = 0
    if w[i] <= c:
        profitWith = recurse(v, w, c - w[i], i+1, memo) + v[i]

    profitWithout = recurse(v, w, c, i+1, memo)

    memo[i][c] = max(profitWith, profitWithout)

    return memo[i][c]


w = [2, 3, 6, 8, 9, 11]
v = [2, 5, 7, 9, 10, 12l]
c = 10

print(knapsack(v, w, c))
