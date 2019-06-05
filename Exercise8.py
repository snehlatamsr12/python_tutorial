inp=float(input('Enter score:'))
try:
    if(inp<=1.0):
        if inp>=0.9:
            print('A')
        elif inp>=0.8:
            print('B')
        elif inp>=0.7:
            print('C')
        elif inp>=0.6:
            print('D')
        else:
            print('F')
    else:
         print('Bad score')       
except:
    print('Bad score')
