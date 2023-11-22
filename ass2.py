#Program to print duplicate odd numbers
n=int(input())
l=list(map(int,input().split()))
num=[]
for i in l:
    if i%2!=0:
        num.append(i)
        num.append(i)
    else:
        num.append(i)
print(num)
