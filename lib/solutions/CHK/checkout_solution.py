

# noinspection PyUnusedLocal
# skus = unicode string
from os import O_ACCMODE


def checkout(skus):
    prices = {
        'A':50,
        'B':30,
        'C':20,
        'D':15,
    }
    total = 0
    for item in skus:
        if item not in prices:
            return -1
    for item in prices.items():
        occurrences = skus.count(item[0])
        if item[0] == 'A':
            if occurrences >= 3:
                total += 130 * (occurrences // 3) + (prices[item[0]] * (occurrences%3))
            else:
                total += occurrences*prices[item[0]]
        elif item[0] == 'B':
            if occurrences >= 2:
                total += 45 * (occurrences//2) + (prices[item[0]] * (occurrences%2))
            else:
                total += occurrences*prices[item[0]]
        elif item[0] == 'C':
            total += occurrences*prices[item[0]]
        elif item[0] == 'D':
            total += occurrences*prices[item[0]]
    return total



