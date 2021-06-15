import sys
sys.setrecursionlimit(10**6)

class Backtrack:
    def __init__(self):
        #10 digit problem so lets consider number_of_digits as 10
        self.number_of_digits = 10
        self.vars = ['0','1','2','3','4','5','6','7','8','9']
        self.domain = ['0','1','2','3','4','5','6','7','8','9']
        self.temp = []
        
    def backtrack_search(self):
        """ Implementation of Back track search """
        
        #variable assignment and constraint validation
        solution = assign4.var_assignment()
    
        if solution != None:
            print("Solution to 10 Digit problem is {}".format(solution))
            
        else:
            print(solution)
            assign4.backtrack_search()

    def var_assignment(self):
        # Range is different for each digit because of the domain reduction, 
        # having self.number_of_digits in all range functions would also yeild same solution but takes longer time and consumes more memory
        for digit1 in range(1, self.number_of_digits):
            for digit2 in range(self.number_of_digits):
                for digit3 in range(6): 
                    for digit4 in range(4):
                        for digit5 in range(3):
                            for digit6 in range(3):
                                for digit7 in range(2):
                                    for digit8 in range(2):
                                        for digit9 in range(2):
                                            for digit10 in range(2):
                                                #check for valid variable assignment and constraints
                                                if digit1 + digit2 + digit3 + digit4 + digit5 + digit6 + digit7 + digit8 + digit9 + digit10 == self.number_of_digits:
                                                    output = [digit1, digit2, digit3, digit4, digit5, digit6, digit7, digit8, digit9, digit10]
                                                    
                                                    flag = True
                                                    for i in range(self.number_of_digits):
                                                        if output[i] == output.count(i):
                                                            continue
                                                        flag = False
                                                        break
                                                    if flag:
                                                        solution = "".join(str(x) for x in output)
                                                        return solution
                                                    
                                                    

# Main Class and method calls
btsearch = Backtrack()
btsearch.backtrack_search()

