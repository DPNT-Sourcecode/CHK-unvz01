

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        'A':50,
        'B':30,
        'C':20,
        'D':15,
    }
    total = 0
    for item in prices.item():
        occurrences = skus.count(item[0])
        if item[0] == 'A':
            if occurrences >= 3:
                total += 130 * (occurrences // 3) + (prices[item[0]]*occurrences%3)
            else:
                total += occurrences*prices[item[0]]
        if item[0] == 'B':
            if occurrences >= 2:
                total += 45 * (occurrences//2)

