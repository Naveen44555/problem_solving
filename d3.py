# #1. Print Numbers from 1 to n
# for i in range(1,6):
#     print(i,end=" ")

# #while--------
# num=int(input("enter numbers:"))
# i=1
# while i<num+1:
#   print(i)
#   i+=1

# #2. Print Numbers from m to n
# m=3
# n=7
# for i in range(m-1,n+1):
#     print(i,end=" ")

# #3. Print Numbers from n to 1 in Reverse
# n=5
# for i in range(n,0,-1):
#     print(i)

# i=0
# m=5
# while i<m:
#     print(i)

   
# num=10
# sum=0
# for i in range(1,num+1):
#     sum+=i
# print(sum,"k")


# #4. Print Numbers from n to m in Reverse
# n=10
# m=6
# for i in range(n,m-1,-1):
#     print(i)
    
# #5.Sum of n Natural Numbers
# n=5
# b=0
# for i in range(n+1):
#     b=b+i
# print(b)

# #6. Factorial of a Number
# n=5
# b=1
# for i in range(1,n+1):
#     b=b*i
# print(b)

# #7. Sum of m to n Numbers
# m=3
# n=7
# b=0
# for i in range(m,n):
#     b=i+b
# print(b)

# m=3 
# n=7
# for i in (m,n+1):
#     n=n+i
# print(n)

# #8.Product of m to n Numbers
# m=2
# n=4
# product=1
# for i in range(m,n+1):
#     product=i*product
# print(product)

# #9. Print Factors of a Number
# n=6
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# #10.Count of Factors
# n=6
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#       count=count+1
# print(count)

# #11.Prime Number Check
# # number=int(input("enter a number: "))
# for i in range(2,100):
#     if i>1:
#      for j in range(2,i):
#         if i%j==0:
#             #   print(" not prime")
#               break
#      else:
#          print(i,"prime")
        

# # -----------
# num=int(input("enter number to check it prime or not:"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print('prime number')
# else:
#     print('not a prime')


# # 12
# m=3
# n=10
# for i in range(m,n+1):
#     if i%2==0:
#         print(i)

# # 13
# m=3
# n=10
# for i in range(m,n+1):
#     if i%2!=0:
#         print(i)

#14-------
# m=3
# n=7
# count1=0
# count2=0
# for i in range(m,n+1):
#     if i%2==0:
#         count1+=1
#     else:
#         count2+=1
# print(f'even numbers are {count1},odd numbers are:{count2}')

# #15
# a='hello'
# rev=a[::-1]
# print(rev)

str='python'
rev=""
for ch in str:
    rev=ch+rev
print(rev)

# n=4
# p=1
# for i in range(1,n+1):
#         p=p*i
# print(p)


# for i in range(7):
#  print(i) 



# ------------------============================------------
 # #1
# num=int(input("enter numbers:"))
# for i in range(0,num+1):
#     print(i)

# m=3
# n=7
# for i in range(m,n+1):
#     print(i)

# n=5
# for i in range(n,0,-1):
#     print(i)

# n=10
# m=6
# for i in range(n,m-1,-1):
#     print(i)
