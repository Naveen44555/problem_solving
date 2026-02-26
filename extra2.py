# import calendar
# import pywhatkit

# -----------
# print(calendar.month(2025,12))
# print(calendar.month(2025,1))

# -----------
# pywhatkit.sendwhatmsg('+91 9381121111','happy birthday',11,1)


# n=3
# m=0
# for i in range(1,n+1):
#     m+=i
# print(m)


# num=12
# if num <25:
#     print("real")
# else:
#     print("fake")


# num=int(input("enter"))
# for i in range(num):
#     if i>1:
#       for j in range(2,num):
#         if (j%1==0):
#             print(j,"it prime")
#             break
#         else:
#              print(j,"not prime")
#     print(i,"--not prime")


# 
# num=int(input("enter: "))
# if num>=2:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"not prime") 
#             break
#     else:
#         print(num,"prime")
# else:
#     print("not prime")


# for i in range(48, 58):   # 48 to 57
#     print(chr(i), end=" ")

# str="2a3b2c"
# for i in str:
#     if i in range(0,9+1):
#         if i==
#         print(i)
        


# a="megha mohan"
# b=a.split()
# c=len(b)
# d=b[0]
# # print(b[0],c)

# print(d.sort())



# a="naveen raju"
# b=a.split()
# c=len(b)-1
# d=b[c]
# print(b[0],(d[::-1]))

# # one way
# a="naveen raju"
# b=a.split()
# c=b[0]
# d=(b[-1][::-1])
# print(c,d)

# # reverse only last name
# a="Honey raju king hanvitha"
# b=a.split()
# first=b[0]
# sec=b[-1]
# last=""
# for i in sec:
#     last=i+last
# for i in range(len(b)-1):
#     print(b[i],end=" ")
# print(last)



# # reverse only last name

# names="Honey raju king hanvitha"
# b=names.split()
# last=""
# for i in b[-1]:
#     last=i+last
# for j in range(len(b)-1):
#     print(b[j],end=" ")
# print(last)
# # output : Honey raju king ahtivnah

names="Honey raju king hanvitha"
b=names.split()
last=''
for i in b[-1]:
    last=i+last
for j in range(len(b)-1):
    print(b[j],end=" ")
print(last)

# output : Honey raju king ahtivnah


# num=[1,2,3,100,4,400]
# # op:4[1,2,3,4]
# a=''
# for i in num:
#     if i%100==i:
#         a=str(i)
#         print(a)
#     elif i%100==0:
#         value=i//100
#         if i//100==value:
#             b=""
#             b=str(value)           
# print(a)        
# # print(b)        

num=[1,2,3,100,400]
res=[]
for i in num:
    if i<100:
        res.append(i)
res.append(len(res)+1)
print(len(res),res)

# op: 4 [1, 2, 3, 4]

# name = "naveenkumarjj"
# last = ""
# i = len(name) - 1
# # reverse last 5 letters dynamically (kumar length)
# count = 0
# while i >= 0 and count < 5:
#     last += name[i]
#     i -= 1
#     count += 1
# print(name[:i+1] + last)
