hours=int(input('Enter Hours:'))
rate=float(input('Enter Rate:'))
if hours>40:
    rate=rate*1.5
pay=hours*rate
print('Pay:')
print(round(pay,2))