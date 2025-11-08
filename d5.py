# a=1,2,3,4
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
