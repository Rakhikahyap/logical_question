def fun(a,b):
    e=a+b
    print(e)
    def sum(a,b):
        r=a*b
        print(r)
    sum()

dic={"a":"5","b":"8","c":"6"}
n={}
for i in dic:
    l=dic[i]
    n[l]=i
print(n)

a=int(input("enter a number"))
i=1
b=[]
while i<=a:
    b.append([i])
    i=i+1
print(b)

a=[27,2,7,4,8,1]
i=0
while i<len(a):
    x=a[0]-a[1]
    y=a[2]-a[3]
    z=a[4]-a[5]
    i=i+1
j=[x,y,z]
print(j)