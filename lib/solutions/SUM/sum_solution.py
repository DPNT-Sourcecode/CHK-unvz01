# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x,y):
    if ((x >= 0 and x <=100) and
        (y >= 0 and y <=100)):  
        return int(x+y)
    else:
        raise Exception('x and y must be integers between 0-100')



