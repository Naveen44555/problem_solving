# a=12321
# b=a
# c=0
# while b>0:
#     temp=b%10
#     c+=temp
#     b//=10
# print(c)


# b=int(input("enter"))
# if b>1:
#     for i in range(2,b):
#         if b%i==0:
#             print("not")
#             break
#     else:
#         print("prime")
# else:
#     print("num 1 or less than 1")


# c=int(input("enter"))
# if c<=1:
#     print('num 1 or less')
# else:
#     for i in range(2,c+1):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i,end=" ")
    

# a=int(input("enter"))
# count=1
# if a>1:
#     for i in range(2,a+1):
#         if a%i==0:
#             count+=1
# if count==2:
#     print("prime")
# else:
#     print("noott")


# # 2
# a="madam"
# b=""
# for i in a:
#     b=i+b
# if b==a:
#     print("pal")
# else:
#     print("not")

# a=12321
# b=a
# c=0
# while b>0:
#     temp=b%10
#     c=c*10+temp
#     b//=10
# if c==a:
#     print(c)
# else:
#     print("not p")


# # 3 armstrong
# b=153
# c=len(str(b))
# d=b
# e=0
# while d>0:
#     temp=d%10
#     e+=temp**c
#     d//=10
#     print(d)
# if e==b:
#     print(e,"arm")
# else:
#     print("not")

# # 4 factorial
# a=int(input("enter"))
# b=1
# for i in range(1,a+1):
#     b*=i
# print(b)

# # 5 swap
# a=2
# b=3
# a,b=b,a
# print(a,b)

# a=4
# b=5
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

# 6 fibonacci
# n=int(input("enter"))
# a=0s
# b=1
# stop=0
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# while n>stop:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     stop+=1

# a=[44,666,433,35,6,39,44]
# b=a[0]
# c=0
# for i in a:
#     if i>b:
#         b=i
# print(b)


# b=a[0]
# c=0
# d=0
# for i in a:
#     if i>b:
#         d=c
#         c=b
#         b=i
# print(b,c,d)

# while
# a=[44,666,888,888,433,35,6,39,44]
# first=a[0]
# i=0
# # print(len(a))
# while i<len(a):
#     if a[i] > first :
#         first = a[i]
#     i+=1
# print(first)

# a=[44,6660,8880,888,433,3335,6,39,44]
# first=a[0]
# sec=0
# third=0
# i=0
# while i < len(a):
#     if a[i] >  first:
#         third=sec
#         sec=first
#         first = a[i]
#     if a[i]>sec and a[i]!=first:
#         sec=a[i]
#     if a[i]>third and a[i]!=first and a[i]!=sec:
#        third=a[i] 
#     i+=1
# print(first,sec,third)

# a=[44,6660,8880,888,433,3335,6,39,44]
# first=sec=third=float("-inf")
# i=0
# while i < len(a):
#     if a[i] >  first:
#         third=sec
#         sec=first
#         first = a[i]
#     if a[i]>sec and a[i]!=first:
#         sec=a[i]
#     if a[i]>third and a[i]!=first and a[i]!=sec:
#        third=a[i] 
#     i+=1
# print(first,sec,third)

# 7 square
# n=int(input("enter"))
# for i in range(n):
#     for j in range(n+2):
#         print("*",end=" ")
#     print()


# n=int(input("num"))
# # for i in range(n):
# #     for j in range(n):
# #         print("*",end=" ")
# #     print()
# i=1
# while i<=n:
#         # print(" "*(n-i) + "*"*(2*i-1))
#         print(" "*i + "*"*(2*(n-i)-1))
#         i+=1

# s1 = "listen"
# s2 = "silent"
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")


# s1 = "listen"
# s2 = "silent"
# s1=s1.lower()
# s2=s2.lower()
# if len(s1)!=len(s2):
#     print("not anagram")
# else:
#     dict1={}
#     dict2={}
#     for i in s1:
#         if i in dict1:
#             dict1[i]+=1
#         else:
#              dict1[i]=1
#     for j in s2:
#         if j in dict2:
#             dict2[j]+=1
#         else:
#             dict2[j]=1
#     if dict1 == dict2:
#         print("anagram",dict1)    
#     else:
#         print("not anagram")


# s1=str(input("enter"))
# s2=str(input("enter"))
# s1=s1.lower()
# s2=s2.lower()
# if len(s1)==len(s2):
#     dict1={}
#     dict2={}
#     for i in s1:
#         if i in dict1:
#             dict1[i]+=1
#         else:
#             dict1[i]=1
#     for j in s2:
#         if j in dict2:
#             dict2[j]+=1
#         else:
#             dict2[j]=1
#     if dict1==dict2:
#         print("an")
#     else:
#         print("not")
# else:
#     print("nnnot")

# s1=str(input("enter"))
# s2=str(input("enter"))
# if sorted(s1) == sorted(s2):
#     print("an")
# else:
#     print('not')


# x=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         print(x[j][i], end=" ")
#     print()


# x=[[1,2,3],[4,5,6],[7,8,9]]
# t=[]
# for i in range(len(x)):
#     row=[]
#     for j in range(len(x[0])):
#         row.append(x[j][i])
#     t.append(row)
# print(t)

# x=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         print(x[i][j],end=" ")
#     print()




# x=[[1,2,3],[4,5,6],[7,8,9]]
# t=[]
# for i in range(len(x)):
#     row=[]
#     for j in range(len(x[0])):
#         row.append(x[i][j])
#     t.append(row)

# for r in t:
#     print(r)


# num=[2,3,4,5]
# res=list(mai8p(lambda x : x*2, num))
# print(res)  


# a=[33,2,4,456,333,77,99]
# b=a[0]
# for i in a:
#     if i > b:
#         b=i
# print(b)

# a=[33,2,4,456,3303,77,99]
# first=a[0]
# i=0
# while i< len(a):
#     if a[i]>first:
#         first= a[i]
#     i+=1
# print(first)


# second larg
# a=[33,2,4,456,3303,777,99]
# first=a[0]
# second=first
# i=0
# while i < len(a):
#     if a[i]>first:
#         second=first
#         first=a[i]
#     elif a[i]>second and a[i]!=first:
#         second=a[i]
#     i+=1
# print(first,second)


# a=[333,2,0,4,456,3303,777,999]
# first=second=third=float("inf")
# i=0
# while i < len(a):
#     if a[i]<first:
#         third=second
#         second=first
#         first=a[i]
#     elif a[i]<second and a[i]!=first:
#         third=second
#         second=a[i]
#     elif a[i]<third and a[i]!=first and a[i]!=second:
#         third=a[i]
#     i+=1
# print(first,second,third)


# a=[1,2,3,4]
# b=list(map(lambda x:x+2,a))
# print(b)

# a=[1,2,3,4]
# b=list(filter(lambda x:x%2==0,a))
# print(b)

# from functools  import reduce
# a=[1,2,3,4]
# b=reduce(lambda x,y : x+y,a)
# print(b)

a=(11,)
print(type(a))

