n=int(input())
k=0
for i in range(1,n+1):
    a=int(input())
    if a%2!=0:
        print(i)
        k+=1
print(k)
