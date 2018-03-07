def get_max_gain( prices ):
    max_gain = 0
    min_val = prices[0]
    index = 1
    for index in range (1, len(prices)):
        min_val = min(min_val, prices[index])
        gain = prices[index] - min_val
        max_gain = max(max_gain, gain)
    return max_gain

my_prices = [10, 2, 20, 12, 1, 7, 9, 30, 5]
max_gain = get_max_gain(my_prices)
print "Maximum gain is: ", max_gain

