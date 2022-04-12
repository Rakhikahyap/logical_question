# def sum(a,b):
#   c=a+b
#   return c
# def multi():
#   e=sum(3,4)
#   return e
# print(multi())


# def sum(a,b):
#     c=a+b
#     print(c)
#     def mul(a,b):
#         d=a*b
#         print(d)
#     mul(4,8)
# sum(3,2)

# def sum(a,b):
#     c=a+b
#     print(c)
# def mul(a,b):
#     d=a*b
#     print(d)
# def call():
#     sum(2,3)
#     mul(4,6)
# call()

# a="2.4"
# b=4
# c=5.6
# d=int(float(a))
# e=int(b)
# f=int(c)
# print(d,e,f)

# a="rakhi"
# b=7.8
# c=9
# d=str(a)
# e=int(b)
# f=int(c)
# print(d,e,f)

# arbitry k
# def sum(**p):
#     return p
# print(sum(a=5,b=6,c=3,d=4))

# pos
# def sum(a,b):
#     return a+b
# print(sum(5,6))


# keyword
# def sum(a,b):
#     return a+b
# print(sum(a=6,b=5))

# def
# def add(a=5,b=7,c=2):
#     e=a+b+c
#     print(e)
# add(9,8,7)

# arbi argu
# def sum(*k):
#     return k
# print(sum(99,20,56,25))



# a=5.0
# b="rakhi"
# c=6.9
# d=int(a)
# e=str(b)
# f=int(c)
# print(b,a+c)



# a="6.0"
# b="geeta"
# c=7
# d=int(float(a))
# e=str(c+d)
# print(b+e)

# a=int(input("enter a number"))
# b=int(input("enter a number"))


# a=int(input("enter a number"))
# b=int(input("enter a number"))




# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# if a>b and a>c:
#     print(a,"a , this is a maximum nu")
# elif b>c and d>c:
#     print(b,"b , this is maximum  nu")
# elif c>a and c>a:
#     print(c, "this is maximum nu")

# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# if a<b>c:
#     print(b,"this is a maximum nu")
# elif b<c>a:
#     print(c,"this is maximum  nu")
# elif c<a>c:
#     print(a,"this is maximum nu")



# a=int(input("enter a num"))
# i=1
# while i<=100:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     i+=1
#     if c==2:
#         print("prime number",i)
#     else:
#         print("not prime no",i)
#     i+=1

# a=int(input("enter a num"))
# i=1
# while i<=a:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     i+=1
#     if c==2:
#         print("prime num",i)
#     else:
#         print("not prime num",i)
#     i=i+1

# def sum(a,b):
#   c=a+b
#   return c
# def multi():
#   e=sum(3,4)
#   return e
# print(multi())


# def sum(a,b):
#     return a+b
# def sub(d):
#     p=d-sum(3,1)
#     print(p)
# sub(15)

# def sum(a,b):
#   return a+b
# def sub(a,b):
#   return a-b
# def main(a,b):
#   a=sum(4,5)+a
#   b=sub(6,4)+b
#   return a,b
# print(main(2,3))

# def fun():
#    e=2+3
#    return e
#    fun()
# a=fun()
# print(a)

# def fun():
#     c=2+4
#     print(c)
#     fun()
# fun()

# x = lambda a : a + 10
# print(x(5)) 

# pop
# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# thisdict.pop("year")
# print(thisdict)

# clear

# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# thisdict.clear()
# print(thisdict)

# popitem

# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# thisdict.popitem()
# print(thisdict)

# def sum(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def main(a,b):
#     a=sum(4,5)+a
#     b=sub(2,1)+b
#     return a,b
# print(main(6,8))


d1={"a":100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
k={}
for x in d1:
    for y in d2:
        if x==y:
            p=(d1[x]+d2[y])
            k.update({x:p})
k.update({'c':300})
k.update({'d':400})
print(k)


     


