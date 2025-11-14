# # vowels check
# a="Naveen"
# c=0
# b="aeiouAEIOU"
# for i in a:
#     if i in b:
#         c+=1
# print(c)


# ---------- vowels  & consonents

# a="hanvitha"
# consonents=0
# vowels=0
# c="aeiouAEIOU"
# for i in a:
#     if i in c:
#         vowels+=1
#     else:
#         consonents+=1
# print(f"total vowels are {vowels}")
# print(f"total consonents are {consonents}")

# a='102030'
# b=""
# c=" "
# for i in a:
#     if i=='0':
#        b+=i
#     else:
#         c+=i
# print(c+b)

# ----------zeros will be last
# a=str(input("enter a number"))
# b=""
# c=""
# for i in a:
#     if i=='0':
#         b+=i
#     else:
#         c+=i
# print(c+b)


# # -------------
# a=102030
# b=""
# c=""
# while a>0:
#     a=str(a)
#     if a=='0':
#         b+=a
#     else:
#         c+=a
# print(b)

# a=int(input("Enter a number: "))
# if a>1:
#     for i in range(2,a):
#         if a%i==0:
#              print(a,"not prime")
#              break
#     else:
#         print(a,"prime")
# else:
#     print(a,"not prime")


for i in range (1,100):
 if i>1:
    for j in range(2,i):
        if i%j==0:
            print(i,"not prime")
            break
    else:
        print(i,"prime")
else:
    print("not prime")


# n=int(input('enter number:'))
# c=1
# for k in range(2,n+1):
#     if n%k==0:
#         c+=1
# if c==2:
#     print("prime")
# else:
#     print("not prime")

# # ----------total prime numbers
# a=int(input("enter number:"))
# c=0
# d=0
# # for a in range(1,100):
# if a>1:
#     for i in range(2,a):
#         if a%i==0:
#             print(a,"not prime")
#             c+=1
#             break
#     else:
#         print(a,"prime")
#         d+=1   
# else:
#     print("total prime numbers are:",d)
#     print("non-prime numbers are:",c)

# # --------method 2
# a=int(input("enter number:"))
# c=1
# for i in range(2,a+1):
#     if a%i==0:
#         c+=1
# if c==2:
#     print(a,"is a prime number")
# else:
#     print(a,"is not a prime number")




# a="z"
# # b=(ord(a)-55)
# # print(chr(b))

# b="zab"
# for i in b:
#     print(chr(ord(i)-32))
    
# print(ord("A"))
# print(ord("B"))
# print(ord("Z"))
# print(ord("a"))
# print(ord("z"))

# num=4700
# b=num
# t=b%1000    #600
# thous=b//1000   #3
# fiv=t%500
# f=t//500
# hun=fiv//100

# print(thous,f,hun)

