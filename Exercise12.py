import sys

max = -sys.maxsize-1  
min = sys.maxsize

while True:
        ip=input('Enter a number: ')
        try:
            if ip=='done':
                break   
            ip=int(ip)    
            if max<ip:
                max=ip
            if min>ip:
                min=ip    
        except:        
            print('bad data')    
            continue

print('max: '+str(max)+' '+'min: '+str(min))