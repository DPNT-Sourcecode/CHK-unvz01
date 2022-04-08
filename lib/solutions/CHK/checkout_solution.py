

# noinspection PyUnusedLocal
# skus = unicode string
from os import O_ACCMODE


def checkout(skus):
    prices = {
        'A':50,
        'B':30,
        'C':20,
        'D':15,
        'E':40,
    }
    total = 0
    for item in skus:
        if item not in prices:
            return -1
    for item in prices.items():
        occurrences = skus.count(item[0])
        if item[0] == 'A':
            if occurrences >= 5:
                if (occurrences%5) >= 3:
                    rem  = (occurrences - 5*(occurrences//5))%3
                    total += 200*(occurrences//5) + 130*((5*(occurrences//5) - (occurrences//3))//3) + (prices[item[0]]*(rem%3))
                else:
                    total += 200*(occurrences//5) + (prices[item[0]]*(occurrences%5))
            elif occurrences >= 3:
                total += 130*(occurrences//3) + (prices[item[0]]*(occurrences%3))
            else:
                total += occurrences*prices[item[0]]
        elif item[0] == 'B':
            if occurrences >= 2:
                total += 45*(occurrences//2) + (prices[item[0]]*(occurrences%2))
            else:
                total += occurrences*prices[item[0]]
        elif item[0] == 'C':
            total +=  occurrences*prices[item[0]]
        elif item[0] == 'D':
            total +=  occurrences*prices[item[0]]
        elif item[0] == 'E':
            if occurrences >= 2 and ('B' in skus):
                total += -30*(occurrences//2) + (prices[item[0]]*(occurrences))
            else:
                total += occurrences*prices[item[0]]
        else:
            return -1
    return total


