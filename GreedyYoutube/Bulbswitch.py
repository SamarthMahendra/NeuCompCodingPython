# Given n bulbs either 0 and 1, turning on ith bulb causes all remaining bulbs to switch

# find min number of switches to turn all bulbs on

def bulbswitch(nums):
    cost = 0

    for i in nums:
        if cost%2==0:
            i = i
        else:
            i = not i
        if i ==1:
            continue
        else:
            cost += 1

    return cost



nums = [1, 4, 6, 2]
print(bulbswitch(nums))


