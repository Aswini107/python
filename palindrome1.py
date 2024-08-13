num=int(input("enter a number:"))
a=str(num)[::-1]
if num==int(a):
    print("Palindrome")
else:
    print("Not a palindrome")
