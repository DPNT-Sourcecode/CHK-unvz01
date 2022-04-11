

# noinspection PyUnusedLocal
# skus = unicode string

def compute_groups(skus,prices):
    occs = (skus.count('S') + skus.count('T') + skus.count('X') +
            skus.count('Y') + skus.count('Z'))
    if occs < 3:
        return 0,skus
    else:
        # For every 3, add 45 to total and remove the 3 most
        # expensive from basket
        for i in range(occs // 3):
            


def checkout(skus):
    prices = {
        'A':50,
        'B':30,
        'C':20,
        'D':15,
        'E':40,
        'F':10,
        'G':20,
        'H':10,
        'I':35,
        'J':60,
        'K':80,
        'L':90,
        'M':15,
        'N':40,
        'O':10,
        'P':50,
        'Q':30,
        'R':50,
        'S':20,
        'T':20,
        'U':40,
        'V':50,
        'W':20,
        'X':90,
        'Y':10,
        'Z':50,
    }
    total = 0
    for item in skus:
        if item not in prices:
            return -1
    
    b_to_remove = (skus.count('E')) // 2
    for i in range(b_to_remove):
        skus = skus.replace('B','',1)

    f_to_remove = (skus.count('F')) // 3
    for i in range(f_to_remove):
        skus = skus.replace('F','',1)

    m_to_remove = (skus.count('N')) // 3
    for i in range(m_to_remove):
        skus = skus.replace('M','',1)

    q_to_remove = (skus.count('R')) // 3
    for i in range(q_to_remove):
        skus = skus.replace('Q','',1)

    u_to_remove = (skus.count('U')) // 4
    for i in range(u_to_remove):
        skus = skus.replace('U','',1)

    total,skus = compute_groups(skus,prices)

    for item in prices.items():
        occurrences = skus.count(item[0])
        if item[0] == 'A':
            if occurrences >= 5:
                if (occurrences%5) >= 3:
                    rem  = (occurrences - 5*(occurrences//5))%3
                    rem2 = occurrences - 5*(occurrences//5) 
                    total += 200*(occurrences//5) + 130*(rem2//3) + (prices[item[0]]*(rem))
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
            total += occurrences*prices[item[0]]
        elif item[0] == 'F':
            total += occurrences*prices[item[0]]
        elif item[0] == 'G':
            total += occurrences*prices[item[0]]
        elif item[0] == 'H':
            if occurrences >= 5 and occurrences < 10:
                total += 45*(occurrences//5) + (prices[item[0]]*(occurrences%5))
            elif occurrences >= 10:
                total += 80*(occurrences//10) + 45*((occurrences%10)//5) + (prices[item[0]]*((occurrences%10)%5))
            else:
                total += occurrences*prices[item[0]]
        elif item[0] == 'I':
            total += occurrences*prices[item[0]]
        elif item[0] == 'J':
            total += occurrences*prices[item[0]]
        elif item[0] == 'K':
            if occurrences >= 2:
                total += 150*(occurrences//2) + (prices[item[0]]*(occurrences%2))
            else:
                total += occurrences*prices[item[0]]
        elif item[0] == 'L':
            total += occurrences*prices[item[0]]
        elif item[0] == 'M':
            total += occurrences*prices[item[0]]
        elif item[0] == 'N':
            total += occurrences*prices[item[0]]
        elif item[0] == 'O':
            total += occurrences*prices[item[0]]
        elif item[0] == 'P':
            if occurrences >= 5:
                total += 200*(occurrences//5) + (prices[item[0]]*(occurrences%5))
            else:
                total += occurrences*prices[item[0]]
        elif item[0] == 'Q':
            if occurrences >= 3:
                total += 80*(occurrences//3) + (prices[item[0]]*(occurrences%3))
            else:
                total += occurrences*prices[item[0]]
        elif item[0] == 'R':
            total += occurrences*prices[item[0]]
        elif item[0] == 'S':
            total += occurrences*prices[item[0]]
        elif item[0] == 'T':
            total += occurrences*prices[item[0]]
        elif item[0] == 'U':
            total += occurrences*prices[item[0]]
        elif item[0] == 'V':
            if occurrences >= 2 and occurrences < 3:
                total += 90*(occurrences//2) + (prices[item[0]]*(occurrences%2))
            elif occurrences >= 3:
                total += 130*(occurrences//3) + 90*((occurrences%3)//2) + (prices[item[0]]*((occurrences%3)%2))
            else:
                total += occurrences*prices[item[0]]
        elif item[0] == 'W':
            total += occurrences*prices[item[0]]
        elif item[0] == 'X':
            total += occurrences*prices[item[0]]
        elif item[0] == 'Y':
            total += occurrences*prices[item[0]]
        elif item[0] == 'Z':
            total += occurrences*prices[item[0]]
        else:
            return -1
    return total



