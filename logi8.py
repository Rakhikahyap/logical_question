a=[7,9,11,3,17,4,440,40,2]
i=0
while i<len(a):
    if a[i]%2==0:
        print("even",a[i])
    else:
        print("odd",a[i])
    i=i+1

def fun():
    c=3+6
    print()
    fun()
fun()




def fun():
    e=2+3
    return e
    fun()
a=fun()
print(a)

a=[2,5,1,3,4,7]
i=0
n=[]
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
j=1
while j<=max:
    if j in a:
        n.append(j)
    j=j+1
print(n)   

mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

x = 5

def fun():
    x = 10
    print("local x:", x)
fun()
print("global x:", x)

i=0
while i<7:
    i+=1
    if i==3:
        continue
    print(i)
    if i==6:
        break
    print(i)
    pass


i=0
while i<8:
    i+=1
    if i==4:
        break
    print(i)


