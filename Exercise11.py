sum=0 
count=0
avg=0
while True:
        ip=input('Enter a number: ')
        try:
            if ip=='done':
                break   
            sum=sum+int(ip)
            count=count+1
        except:        
            print('bad data')    
            continue
print(str(sum)+' '+str(count)+' '+str(sum/count))