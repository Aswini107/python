arr=list(map(int,input().split()))
sum1=0
sum2=0
for i in arr:
    if i%2==0:
        sum1=sum1+i
    else:
        sum2=sum2+i
print("Even sum:",sum1,"Odd sum:",sum2,end=" " )
        
