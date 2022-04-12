a=[1,2,3,4,6,7,8,9,12]
i=0
m=[]
while i<len(a):
    if i==5:
        m.append(i)
    i=i+1
print(m)



a=[1,2,3,4,5,6,7,8,9,12]
m=[]
for n in range(1,13):
    if n not in a:
        m.append(n)
print(m)

a=[1,2,3,4,6,7,8,9,12]
i=0
m=[]
while i <len(a):
    if i==10:
        m.append(i)
    i=i+1
print(m)
j=0
n=[]
while i<len(a):
    if i==11:
        n.append(i)
    j=j+1
print(n)

a={'bijendra':45,'deepak':60,'param':20,'anjili':30}
b=sorted (a.items(),key=lambda t:t[1],reverse=True)
print(b)

a=[{"V":"SOO1"},{"V":"SOO2"},{"VI":"SOO1"},{"VI":"SOO5"},{"VII":"SOO5"},{"V":"SOO9"},{"VIII":"SOO7"}]
b=[]
for a1 in (a):
    a2=(a1.values())
    if a2 not in b:
        b.extend(a2)
    print(b)

a=[2,4,5,7]
my_dict={}
sum=0
i=0
while i<len(a):
    sum+=a[i]
    my_dict.update({i:sum})
    i+=1
print(my_dict)

a=[1,2,3,4,6,7,8,9,12]
m=[]
for n in range(1,13):
    if n not in a:
        m.append(n)
print(m)

dic1=[1,2,3,4,5]
dic2=["6","7","8"]
n={}
for i in range(len(dic1)):
    for i in range(len(dic2)):
        k=dic1[i],dic2[i]
        n.update({k})
        i=i+1
print(n)





a=8
print(complex(a))


s="Hello rakhi"
print(s.replace("H","J"))


a="aanu"
print(a.replace("a","v"))




def fun():
    global a
    a=5
    print(a)
fun()
print(a)

dic1=[1,2,3,4,5,6,7]
dic2=["6","7","8","9"]
n={}
for i in  range(len(dic1)):
    for i in range(len(dic2)):
        k=dic1[i],dic2[i]
        n.update({k})
        i=i+1
print(n)

thisdict={
    "brand":"ford",
    "model":"Mustang",
    "year":1956
}
print(thisdict)


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["year"]
print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)