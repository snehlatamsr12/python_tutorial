def computeGrade(score):
        if(inp<=1.0):
            if inp>=0.9:
                return('A')
            elif inp>=0.8:
                return('B')
            elif inp>=0.7:
                return('C')
            elif inp>=0.6:
                return('D')
            else:
                return('F')
        else:
            return('Bad score')       
    
try:
    inp=float(input('Enter score:'))
    print(computeGrade(inp))
except:
    print('Bad score')