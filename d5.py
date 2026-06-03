# num="53995"
# digit="5"
# max_num=""
# for i in range(len(num)):
#     if num[i] == digit:
#         new_num=num[:i] + num[i+1:]
#         if new_num > max_num:
#             max_num = new_num
# print(max_num)


# a=0
# print(type(a))
# a=(2,5,6)
# print(type(a))

# b={20,30,40,"naveen",2.6,True,3+4j,{10,20}}
# print(b)

# a=10
# b=[]
# for i in range(1,a+1):
#     if a%i==0:
#         b.append(i)
#     else:
#        print(i)
# print(b)



# a=10
# b=0
# for i in range(1,a+1):
#     if a%i==0:
#         b=b+1
#     else:
#         print("no")
# print("prime numbers are",i)


# print(ascii(0))
# print(chr(1072))
# print(chr(1071))
# for i in range(0)



# # # print(ord(3044))
# for chr in range(ord(a),ord(z)+1):
#     print(chr)

# print(ascii(A50))

# print(chr(97))
# # print(chr())

# for i in range(97,123):
#     print(chr(i),end=" ")


# a=20
# for i in range(0,a):
#   if a%i==0:
#     print(a,"it is prime")f
#   else:
#     print("not prime")




# a=1
# b=20
# for i in range(a,b+1):
#     is_prime=True
#     for j in range(2,i):
#         is_prime=True
#         if i<2:

# #-------
# count=0
# for i in range(1,100):
#    if i>1:
#     for j in range(2,i):
#       if i%j==0:
#         # print("not prime")
#         break
#     else:
#         print(i,"prime")
#         count+=1

#    else:
#      print("not prime")
# print(f"total prime numbers are:{count}")

# # total armstrong numbers 
# m=1
# n=500
# for i in range(m,n+1):
#     temp=i
#     count=0
#     while temp!=0:
#         count+=1
#         temp//=10
#     dummy=i
#     sum=0
#     while dummy!=0:
#         rem=dummy%10
#         sum+=rem**count
#         dummy=dummy//10
#     if sum==i:
#         print(i)

# a="Naveen"
# b=" "
# for i in a:
#     if i in "aeiouAEIOU":
#         b=i
#         print(f"first vowel is :{b}")
#         break

# a="Naveen"
# b=" "
# for i in a:
#     if i in "aeiouAEIOU":
#         b=i
# print(f"second vowel is {b}")

# a="Navien"
# b=" "
# for i in a:
#     if i in "aeiouAEIOU":
#         b+=i
# print(b)

# a=1
# b=11
# prime_count=0
# composite_count=0
# for i in range(a,b+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print("prime number:",i)
#     elif count>2:
#         print("composite number:",i)

# ---------------------nnnnnnew

# m=10
# n=30
# for i in range(m,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#        print(i)
    
# m=int(input())
# n=int(input())
# for i in range(m,n+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)

# m=int(input())
# n=int(input())
# count=0
# for i in range(m,n+1):
#     if i>1:
#         for j in range(2,i):
#                 if i%j==0:
#                     break
#         else:
#             print(i)
#             count+=1
# print("prime numbers:",count)

# a=153
# temp=a
# b=len(str(a))
# d=0
# while temp>0:
#    c=temp%10 #3
#    d+=c**b
#    temp//=10
#    print(temp,d)
# if d==a:
#     print(d,"arm")
# else:
#     print("not arm")


# a=2
# temp=a
# c=a
# leng=0
# while temp>0:
#     leng+=1
#     temp//=10
# tot=0
# while c>0:
#     e=c%10
#     tot+=e**leng
#     c=c//10
# if tot==a:
#     print(leng,tot)
# else:
#     print("not arm")
    

# m=int(input())
# n=int(input())
# for i in range(m,n+1):
#     temp=i
#     l=0
#     if temp==0:
#       l=1
#     else:
#       while temp >0:
#          l+=1
#          temp//=10
#     sec=i 
#     tot=0
#     while sec>0:
#           a=sec%10
#           tot+=a**l
#           sec//=10
#     if tot==i:
#       print(i)
         

# m=int(input())
# n=int(input())
# for i in range(m,n+1):
#     temp=i
#     l=0
#     if temp==0:
#         l=1
#     else:
#         while temp>0:
#             l+=1
#             temp//=10
#     real=i
#     tot=0
#     while real>0:
#         c=real%10
#         tot+=c**l
#         real//=10
#     if tot==real:
#         print(tot)


# m=10
# n=25
# for i in range(m,n+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)

# import math
# i=16
# print(math.sqrt(i))

# # last prime num
# m=10
# n=25
# last=0
# for i in range(m,n+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             last=i
# print(last)

# name="krishna"
# vowels="aeiouAEIOU"
# for i in name:
#     if i in vowels:
#         print(i)
#         break


# name="Ramakrishna"
# vowels="AEIOUaeiou"
# last=" "
# for i in name:
#     last=i
# print(last)

# for i in range(2,11):
#     if i%2==0:
#         continue
#     else:
#         print(i)


# m=1
# n=10
# comp=[]
# prime=[]
# for i in range(m,n+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 comp.append(i)
#                 break
#         else:
#             prime.append(i)
# print(comp,prime)


# m=int(input())
# n=int(input())
# for i in range(m,n+1):
#     if i>1:
#        for j in range(2,i): 
#            if i % j==0:
#                break
#        else:
#              print(i)
#              break

# m=int(input())
# n=int(input())
# count=0
# for i in range(m,n+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             count+=1
# print(count)


# m=int(input())
# n=int(input())
# for i in range(m,n+1):
#     num=i 
#     l=0
#     while num>0:
#         l+=1
#         num //=10
#     num2=i
#     tot=0
#     while num2>0:
#         e=num2%10
#         tot+=e**l
#         num2 //=10
#     if tot == i:
#         print(tot)

# # ------------------
# # 2.
# a=int(input())
# b=int(input())
# count=0
# for i in range(a,b+1):
#     if i > 1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             count+=1
# print(count)

# # 3
# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     c=i
#     len=0
#     while c>0:
#         len+=1
#         c=c//10
#     d=i
#     tot=0
#     while d>0:
#         e=d%10
#         tot+=e**len
#         d//=10
#     if tot == i:
#       print(tot)
 
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
#     print(tot,"arm")
# else:
#     print(tot,"not")

# a=int(input())
# b=int(input())
# last=0
# for i in range(a,b+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             last=i
# print(last)
            
# a="krishna"
# b="aeiou"
# c=""
# for i in a:
#     if i in b:
#         c=i
#         # break
# print(c)

# b=int(input())
# for i in range(1,b+1):
#     if i%2!=0:
#         print(i,end=" ")


# m = int(input())
# n = int(input())
# prime = []
# comp = []
# for i in range(m, n+1):
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 comp.append(i)
#                 break
#         else:
#             prime.append(i)
# print("Prime:", prime)
# print("Composite:", comp)

