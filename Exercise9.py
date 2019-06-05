def compute_pay(hours,rate):   
        print('inside function compute pay') 
        if hours>40:
            rate=rate*1.5
        return hours*rate    
    
try:
    hours=int(input('Enter Hours:'))
    rate=float(input('Enter Rate:'))
    pay=compute_pay(hours,rate)
    print('Pay: '+str(round(pay,2)))
except:
    print('Error, please enter numeric input')