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


# while
n=int(input("enter:"))
count=0
i=0
if i>0:
    while i<=n:
        if n%i==0:
            count+=1
        i+=1
    if count==2:
        print("prime")
    else:
        print("not")
else:
    print("not")


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

# array=[89,499,6,984,33,56]
# b=array[0]
# c=b
# for i in array:
#     if i>b:
#         c=b
#         b=i
# print(c)

# array=[89,499,6,984,33,56]
# array.sort(reverse=True)
# print(array)

# words = ["banana", "apple", "cherry"]
# words.sort()
# print(words)

# numbers = [5, 2, 9, 1, 7]
# new_list = sorted(numbers)
# print(new_list)

# array=[89,499,6,84,33,56]
# largest=array[0]
# i=1
# while i<len(array):
#     if array[i]>largest:
#         largest=array[i]
#     i+=1
# print(largest)


# a=[33,0,988,3,43,323,4]
# first=a[0]
# second=0
# i=1
# while i<len(a):
#     if a[i]>first:
#         second=first
#         first=a[i]
#     elif a[i]>second and a[i]!=first:
#         second=a[i]
#     i+=1
# print(first)
# print(second)

# float('inf') → biggest possible value
# float('-inf') → smallest possible value

# a=[3045,3,45,6,7,33,5866,798]
# first=second=third=float('-inf')
# print(first)
# i=0
# while i<len(a):
#     if a[i]>first:
#         third=second
#         second=first
#         first=a[i]
#     elif a[i]>second and a[i]!=first:
#         third=second
#         second=a[i]
#     elif a[i]>third and a[i]!=second and a[i]!=first:
#         third=a[i]
#     i+=1
# print(first,second,third)


# a=[33,4600,74,3,19,2,9087]
# first=a[0]
# sec=first
# i=0
# while i <len(a):
#     if a[i]<first:
#         sec=first
#         first=a[i]
#     elif a[i]<sec and a[i]!=first:
#         sec=a[i]
#     i+=1
# print(first,sec)

# a=[333,223,650,7,344,56,987]
# first=sec=third=float("inf")
# i=0
# while i<len(a):
#     if a[i]<first:
#         third=sec
#         sec=first
#         first=a[i]
#     elif a[i]<sec and a[i]!=first:
#         third=sec
#         sec=a[i]
#     elif a[i]<third and a[i]!=sec and a[i]!=first:
#         third=a[i]
#     i+=1
# print(first,sec,third)

# a=4
# b=4
# for i in range(a):
#     for j in range(b+3):
#         print("*",end=" ")
#     print()

# n=4
# for i in range(0,n+1):
#     for j in range(n-i):
#         print("#",end=" ")
#     print()

# # pyramid
# n=4
# for i in range(1,n+1):
#     for j in range(n):
#         print(" " ,end=" ")
#     for k in range(i):
#         print("* ",end=" ")
#     print()



# a={"name":"naveen","age":23}
# print(a[0])
# print(a.keys())
# print(a.values())
# print(a.items())


# a=10
# for i in range(1,a+1):
#     for j in range(1,a+1):
#          print(f'{i} x {j} = {i*j}')
#     print()

# a=int(input("enter:"))
# temp=a
# c=0
# while temp>0:
#     d=temp%10
#     c+=d**len(str(a))
#     temp//=10
# if c==a:
#     print(c,"armstrong")
# else:
#     print("not")


# roman_values = {
#     'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000,
# }

# def roman_to_int(s):
#     s = s.upper()
#     total = 0
#     prev_value = 0
#     for ch in reversed(s):
#         value = roman_values.get(ch, 0)
#         if value < prev_value:
#             total -= value
#         else:
#             total += value
#         prev_value = value
#     return total

