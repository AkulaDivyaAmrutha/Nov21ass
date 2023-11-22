#Program to print separate even numbers one side and odd numbers one side
n=int(input())
l=list(map(int,input().split()))
o=[]
e=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
for i in e:
    print(i,end=' ')
for i in o:
    print(i,end=' ')
