# # 1.
# def add():
#     a=10
#     b=20
#     c=a+b
#     return c
# print(add())

# # 2.
# def even_or_odd(e):
#     if e%2==0:
#         print("even")
#     else:
#         print(e,"is odd")
# even_or_odd(15)


# # 3 leap year
# def leap(f):
#     if (f%4==0 and f%100!=0) or f%400==0:  #Example: 2020 → divisible by 4, not by 100 → leap year
#         print("leap year")
#     else:
#         print("not leap year")
# leap(2020)


# -----------2nd way
# year=int(input("enter:"))
# if year%4==0:
#      if year%100==0:
#           if year%400==0:
#                print("leap")
#           else:
#                print('not')
#      else:
#           print("lp")  
# else:
#      print("not ")    
        
# range leap years
# for i in range(1000,2100):
#     for j in range(i,i+1):
#         if (j%4==0 and j%100!=0) or j%400==0:
#              print(j)
#     else:
#      #     print("not ")
#           continue
# print("this are leap years")
    
# # 4
# def prime(g):
#     for i in range(1,g):
#         if i>1:
#             for j in range(2,i):
#                 if i%j==0:
#                     print(i,"not prime")
#                     break
#             else:
#                 print(i,"prime")
#         else:
#             print(i,"not prime")
# prime(33)

# # 5. Print Armstrong Numbers from m to n Using Function
# m=53
# n=500
# k=[]
# while m>0:
#     for i in range(m,n+1):

# # armstrong number check
# m=153
# n=m
# q=0
# p=str(m)
# power=len(p)

# while n>0:
#     digit=n%10
#     q+=digit**power
#     n//=10
# if m==q:
#   print(q,"armstrong")
# else:
#    print("not armstrong")


# m = 1000
# n = 10000
# for i in (m,n+1):
#     temp=i
#     length=0
#     while temp>0:
#         temp//=10
#         length+=1
#     print(length)
# # print(temp)


# fibanocci
# n=10
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,n):
#     c=a+b
#     a=b
#     b=c
#     print(c)

    
# # vowels check
# def name(a):
#    b="aeiou"
#    count=0
#    for i in a:
#       if i in b:
#          count+=1    
#    print(count)
# name("sreevani")

# neon
# a=9
# b=a*a
# sum=0
# while b>0:
#     ld=b%10
#     sum+=ld
#     b//=10
# if a==sum:
#   print("neon")
# else:
#    print("not neon")


# # factorial number
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return fact(n-1)*n
# print(fact(5))

# # fibanocci number
# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# for i in range(5):
#     print(fib(i))

# # sum of numbers
# def digit_sum(n):
#     if n==0:
#         return 0
#     else:
#         return n%10 + digit_sum(n//10)
# print(digit_sum(125))

# # reverse a number
# def reverse(n,rev=0):
#     if n==0:
#         return rev
#     else:
#         rev = rev*10 + n%10
#         return reverse(n//10,rev)
# print(reverse(1234))

# def is_palindrome(s):
#     if  len(s) <=1:
#         return True
#     elif s[0] !=s[-1]:
#         return False
#     else:
#         return is_palindrome(s[1:-1])
# inp="racecar"
# if is_palindrome (inp):
#     print('palindrome')
# else:
#     print("not a palindrome")