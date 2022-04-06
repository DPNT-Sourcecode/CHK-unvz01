class sum_solution():

    def compute(self,x,y):
        if ((x >= 0 and x <=100) and
             y >= 0 and y <=100):  
            return int(x+y)
        else:
            print(('Parameters must be positive integers' 
                   + 'greater than 0 and lower than 100'))
            return False
