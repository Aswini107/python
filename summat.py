m,n=map(int,input().split())
mat=[]
sum1=[]
for i in range(m):
    row=list(map(int,input().split()))
    mat.append(row)
    sum1.append(sum(row))
print(mat)
print(sum1)
