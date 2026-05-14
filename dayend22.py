
# Break Amount into 1000s, 500s, and Remaining Change----
# amount=3700
# th=amount%1000
# thous=amount//1000
# f_hund=th//500
# rem=th%500
# print(thous,f_hund,rem)

# # 2
# tot_time=3672
# h=tot_time//60
# hours=h//60
# min=h//60
# sec=tot_time%60
# print(hours,min,sec)

# a=85
# b=90
# c=88
# print(round((a+b+c)/3,3))

# a=int(input())
# if a & 1==0:
#     print("even")
# else:
#     print("odd")

# if (a//2)*2==a:
#     print("even")
# else:
#     print("odd")

# a=int(input())
# b=int(input())
# c=int(input())
# if (a>=35 and b>=35) or (a>=35 and c>=35) or (b>=35 and c>=35):
#     print("pass")
# else:
#     print('fail')

# import math
# a=int(input())
# root=int(math.sqrt(a))
# if root*root == a:
#     print("square root")
# else:
#     print("not perf")


# people=int(input())
# cars=people//5
# if people%5!=0:
#     print(cars+1,"req")
# else:
#     print(cars,"req")


# a=int(input())
# if (a%4==0 and a%100!=0) or (a%400==0):
#     print(a,"leap")
# else:
#     print(a,"not leap")

# a=int(input())
# for i in range(a,0,-1):
#     print(i)

# a=int(input())
# b=1
# for i in range(1,a+1):
#     b*=i
# print(b)

# a=int(input())
# c=int(input())
# b=1
# for i in range(a,c+1):
#     b*=i
# print(b)

# a=int(input())
# if a>1:
#     for i in range(2,a):
#         if a%2==0:
#             print(a,"not")
#             break
#     else:
#         print(a,"prime")
# else:
#     print(a,"1 below not prime")

# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     if i>1:
#         for j in range(2,int(i**0.5)+1):
#             if i % j ==0:
#                 break
#         else:
#             print(i,end=" ")

# a="hello"
# b=""
# for i in a:
#     b=i+b
# print(b)
# print(a[::-1])

# a="madam"
# b=""
# for i in a:
#     b=i+b
# if b==a:
#     print(b)
# else:
#     print("not")


# a=int(input())
# c=1
# while a>0:
#     b=a%10
#     c*=b
#     a//=10
# print(c)

# a=int(input())
# b=a
# l=0
# while b>0:
#     l+=1
#     b//=10
# c=a
# tot=0
# while c>0:
#     d=c%10
#     tot+=d**l 
#     c//=10
# if tot == a:
#     print(tot,"armstr")
# else:
#     print(tot,"not")

# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     c=i
#     l=0
#     while c>0:
#         l+=1
#         c//=10
#     d=i
#     tot=0
#     while d>0:
#         e=d%10
#         tot+=e**l
#         d//=10
#     if tot==i:
#         print(tot,"arm")

# a=int(input())
# b=a
# c=0
# while b>0:
#     d=b%10
#     c=c*10+d
#     b//=10
# if c==a:
#     print(c,"pal")
# else:
#     print(c,"not")


# a=input()
# b="AEIOUaeiou"
# count=0
# cons=0
# for i in a:
#     if i in b:
#         count+=1
#     else:
#         cons+=1
# print(f"vowels {count}, Consonents: {cons}")

# . Perfect Number Check==------------
# a=int(input())
# tot=0
# for i in range(1,a):
#     if a%i==0:
#         tot+=i
# if tot==a:
#     print(tot,"perf")
# else:
#     print(tot,"not perf")

# a=int(input())
# b=a*a
# c=0
# while b>0:
#     d=b%10
#     c+=d
#     b//=10
# if c == a:
#     print(c,"neon")
# else:
#     print(c,"not neon")


# # strong num
# a=int(input())
# b=a
# tot=0
# while b>0:
#     d=b%10
#     e=1
#     for i in range(1,d+1):
#         e*=i
#     tot+=e
#     b//=10
# if tot ==a:
#     print(tot,"srong")
# else:
#     print(tot,"not srong")
    
# # harshad
# a=int(input())
# b=a
# d=0
# while b>0:
#     c=b%10
#     d+=c
#     b//=10
# if a%d==0:
#     print(d,"harshad")
# else:
#     print(d,"not ")


# n=int(input())
# a=0
# b=1
# for i in range(n):
#     print(a)
#     a,b=b,a+b


# n=int(input())
# b=n*n
# d=0
# while b>0:
#     c=b%10
#     d+=c
#     b//=10
# if d==n:
#     print(d,"neon")
# else:
#     print(d,"not ")


# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# b=int(input())
# print(is_prime(b))

# a=-1
# b=-1
# print(id(a))
# print(id(b))

# a="helloytghjkl;,.'fghjbkl;tfyghjiklhgjklgdsfjkljhbdfklfjhgsfkljgnkldfgjdfkl"
# b="helloytghjkl;,.'fghjbkl;tfyghjiklhgjklgdsfjkljhbdfklfjhgsfkljgnkldfgjdfkl"
# a=500
# b=500
# print(id(a))
# print(id(b))

# print(hash(10))
# print(hash("hello"))

# print("hi")
# print(10/5)
# print("hello")


# _aa=88
# print(_aa)

# if=99
# print(if)


# a=10.9,2,3
# print(a)
# print(type(a))

# import sys

# a = [1,2,3]
# b = (1,2,3)

# print(sys.getsizeof(a))
# print(sys.getsizeof(b))

# import sys
# print("start")
# sys.exit()
# print("end")

# l={"a",4,44.9,True,3+4j}
# print(l[3])

# t=(2,3,4,5)
# print(t[2])

# s = {1, 2, 3}
# s.remove(2)
# s.add(10)
# print(s)
