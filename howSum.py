# howSum memoized
def howSum(target, numbers, memo={}):
    if target in memo:
        # return memo[target]
        pass
    if target == 0:
        return []
    if target < 0:
        return None

    for num in numbers:
        result = howSum(target-num, numbers, memo)
        if result != None:
            memo[target] = result + [num]
            return memo[target]

    memo[target] = None
    return None


t = 3000
nums = [7, 14]

print(howSum(t, nums))
