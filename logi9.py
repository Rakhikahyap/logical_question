i=0
while i<=10:
    i=i+1
    if i==2:
        continue
    if i==5:
        break
    print(i)
    pass

 

i=1
sum=0
while i<=10:
    a=int(input("entre a number"))
    sum=sum+a
    i=i+1
print(sum)

i=0
while i<7:
    i=i+1
    if i==2:
        break
    print(i)
while i<6:
    i=i+1
    if i==3:
        continue
    print(i)

a=int(input("enter a number"))
i=0
while i<=a:
    print("odd")
    i=i+1

i=1
while i<=3:
    a=1
    while a<=i:
        print('*',end='')
        a=a+1
    print()
    i=i+1

i=1
while i<=5:
    a=1
    while a<=5:
        print(a,end='')
        a=a+1
    print()
    i=i+1
list=[1,2,3,1,2,2]
i=0
a=[]
while i<len(list):
    if list[i]not in a:
        a.append(list[i])
    i=i+1
print(a)
    

x=[1,2,3,4,5,56,34,23,78,56,2,1,3,5,6,5]
i=0
b=[]
while i<len(x):
    if x[i] not in b:
        b.append(x[i])
    i=i+1
print(b)

def even():
    a=[1,2,3,4,5,6,7,8,9]
    i=1
    while i<=9:
        if i%2==0:
            print("even",i)
        else:
            print("odd",i)
        i=i+1
even()

def fun():
    a=int(input("enter a number"))
    if a%5==0 and a%3==0:
        print("fizzbuzz")
    elif a%3==0:
        print("fizz")
    elif a%5==0:
        print("buzz")
    elif a%5!=0 and a%3!=0:
        print("22")
fun()

i=5
while i>=1:
    a=1
    while a<=i:
        print('*',end='')
        a=a+1
    print()
    i=i-1

a=[[2,3,2,4],[5,6,2,3],[11,23,4,5]]
i=0
n=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    i=i+1
    n.append(sum)
print(n)



# default
def add(a=5,b=7,c=2):
    e=a+b+c
    print(e)
add (9,8,7)
a=5
def rakhi():
    b=4
    print(a)
rakhi()
print(b)


def fun(a,b):
    e=3+5
    print(e)
    def sum(a,b):
        d=a-b
        print(d)
        sum(2,1)
fun(3,6)

a=5
def rakhi():
    b=4
    print(b)
rakhi()
print(a)

a1={'a':100,'b':200}
a2={'x':300,'y':200}
a=a1.copy()
a.update(a2)
print(a)

a={'aanuvi':58,"avni":87,"aarohi":88}
sum=0
for i in (a):
    sum=sum+(a[i])
print(sum)

x={'12':22,'13':56,'16':77}
sum=0
for i in (x):
    sum=sum+(x[i])
print(sum)

def fun():
    a=int(input("enter a number"))
    if a%5==0 and a%3==0:
        print("fizzbuzz")
    elif a%3==0:
        print("fizz")
    elif a%5==0:
        print("buzz")
    elif a%5!=0 and a%3!=0:
        print("22")
fun()

a=int(input("enter a number"))
i=0
while i<=10:
    if i%2==0:
        print("even",i)
    elif i%2!=0:
        print("odd",i)
i=i+1

x=int(input("enter a num"))
if x%2==0:
    print("even")
else:
    print("odd")

a=[2,33,4,5,1,6,57]
i=0
min=a[0]
while i<len(a):
    if a[i]<min:
        min=a[i]
    i=i+1
print(min)

x=[232,45,7,87,45,100]
i=0
max=0
while i<len(x):
    if x[i]>max:
        max=x[i]
    i=i+1
print(max) 

