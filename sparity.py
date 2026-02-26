# n=int(input("enter"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("not p")
#             break
#     else:
#         print("prime")
# else:
#     print("not")
    
# n=int(input("enter"))
# count=0
# if n>1:
#     for i in range(2,n+1):
#         if n%i==0:
#             count+=1
#     else:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("not")

# n=int(input("enter"))
# count=0
# i=1
# if n>0:
#     while i<=n:
#         if n%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         print("prime")
#     else:
#         print("not")
# else:
#     print("not p you entered zero")


# n=int(input("enter:"))
# if (n//2)*2==n:
#     print("even")
# else:
#     print("odd")

# n=int(input("enter:"))
# if n & 1 ==0:
#     print('even')
# else :
#     print("not")


# # while
# n=int(input("enter:"))
# count=0
# i=0
# if i>0:
#     while i<=n:
#         if n%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         print("prime")
#     else:
#         print("not")
# else:
#     print("not")


# a="radar"
# b=""
# for i in a:
#     b=i+b
# if b==a:
#     print("p")
# else:
#     print("not")
    

# a="radar"
# b=len(a)-1
# rev=""
# while b>=0:
    


# -------
# a="radar"
# b=""
# for i in a:
#     b=i+b
# if b==a:
#     print(b,"pal")
# else:
#     print("not")
    
# b="radar"
# c=""
# d=len(b)-1
# # print(d)
# e=d
# while e>=0:
#     c+=b[e]
#     e-=1
# print(c)
# if b==c:
#     print("pal")
# else:
#     print('not')


# a="racecar"
# b=""
# c=len(a)-1
# d=c
# while d>=0:
#     b+=a[d]
#     d-=1
# if b==a:
#     print("pal")
# else:
#     print('not')

# a="racecar"
# b=len(a)-1
# d=""
# while b>=0:
#     d=a[b]+d
#     b-=1
# if d==a:
#     print(d,"pal")

# -------
# a = "racecar"

# if a == a[::-1]:
#     print("Palindrome")

# # 3.armstrong
# a=153
# b=a
# leng=len(str(a))
# c=0
# while b>0:
#     temp=b%10
#     c+=temp**leng
#     b//=10
# print(c)


# a=9474
# b=a
# c=len(str(a))
# d=0
# while b>0:
#     temp=b%10
#     d+=temp**c
#     b//=10
# print(d)

# # 4
# a=10
# b=1
# for i in range(1,a+1):
#     b*=i
# print(b)


# a=10
# b=a
# d=1
# while b>0:
#    d=d*b
#    b-=1
# print(d)

# a=int(input("enter"))
# b=a
# c=1
# while b>0:
#     c=c*b
#     b-=1
# print(c)

# # 5.
# a=10
# b=5
# a,b=b,a
# print(a,b)

# c=2
# d=3
# c+=d
# d=c-d
# c=c-d
# print(c,d)

# 6
# a=int(input("enter:"))
# first=0
# second=1
# count=0
# while count<a:
#     print(first,end=" ")
#     next=first+second
#     first=second
#     second=next
#     count+=1


# a=int(input("enter:"))
# first=0
# second=1
# count=0
# while count<a:
#     print(first,end=" ")
#     next=first+second
#     first=second
#     second=next
#     count+=1

# a=int(input("enter:"))
# first=0
# second=1
# for i in range(a):
#     print(first,end=" ")
#     next=first+second
#     first=second
#     second=next

# array=[1,2,3,4]
# b=0
# # print(max(array))
# for i in array:
#     if i>b:
#         b=i
# print(b)

# array=[1,2,3,6,4]
# b=array[0]
# for i in array:
#    if i<b:
#        b=i    
# print(b)

# array=[300,5,26,33,3,339,8,4]
# b=array[0]
# c=[]
# for i in array:
#     if i>b:
#         b=i
#         c.append(b)
# print(c[-2],c)


