n = int(input("შემოიტანეთ თანხა თეთრებში: "))

def minNumOfCoins(n, coins):
    nums = [float('inf') for x in range (n+1)]
    nums[0] = 0
    for coin in coins:
        for amount in range (len(nums)):
            if coin <= amount:
                nums[amount] = min(nums[amount], 1 + nums[amount - coin])
    return nums[n] \
        if nums[n] != float('inf') \
        else -1

print(minNumOfCoins(n, [1, 5, 10, 20, 50]))
