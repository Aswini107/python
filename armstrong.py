num=int(input())
arm=0
a=num
while num>0:
    rem=num%10
    arm=(rem*rem*rem)+arm
    num=num//10
if a==arm:
    print("Armstrong Number")
else:
    print("Not Armstrong")
