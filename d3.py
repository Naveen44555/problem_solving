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

# # -------
# m=3
# n=6
# b=0
# for i in range(m,n+1):
#     b+=i
# print(b)   
        
        

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

# -----------
# n=6
# b="  "
# for i in range(1,n+1):
#     if n%i==0:
#         b+=str(i)
# print(b)


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

# str='python'
# rev=""
# for ch in str:
#     rev=ch+rev
# print(rev)

# # 16 Check for Palindrome String
# a="madam"
# b=""
# for i in a:
#     b=i+b
# if a==b:
#     print("p")
# else:
#     print("not p")

# # 17. Sum of Digits
# a="123"
# b=0
# for i in a:
#     b+=int(i)
# print(b)

# # 18. product of Digits
# a="123"
# b=1
# for i in a:
#     b*=int(i)
# print(b)

# # 19. Armstrong Number Check
# num=153
# b=num
# length=0
# while b>0:
#     count=b%10
#     length+=1
#     b//=10
# sample=num
# arm=0
# while sample>0:
#     c=sample%10
#     arm+=c**length
#     sample//=10
# if arm==num:
#     print(arm,"armstrong")
# else:
#     print("not armstrong")


# # 20. Reverse a Number
# a='123'
# b=""
# for i in a:
#     b=i+b
# print(b)

# # 21. Palindrome Number Check
# a='121'
# b=""
# for i in a:
#     b=i+b
# if b==a:
#   print(b,"palindrome")
# else:
#     print("not ")

# # without converting string
# a=121
# b=a
# c=0
# while b>0:
#     d=b%10
#     c=c*10+d
#     b//=10
# if a==c:
#     print(c,"palindrome")
# else:
#     print(c,"not palindrome")

# # 22. Count Vowels in String
# fruit="apple"
# count=0
# vowels="aeiou"
# for i in fruit:
#     if i in vowels:
#         count+=1
#     else:
#         pass
# print(count)
    
# # 23. Count Consonants in String
# fruit="apple"
# count=0
# vowels="aeiou"
# for i in fruit:
#     if i in vowels:
#         pass
#     else:
#         count+=1
# print(count)

# # 24. Count Vowels and Consonants
# fruit="apple"
# count1=0
# count2=0
# vowels="aeiou"
# for i in fruit:
#     if i in vowels:
#         count1+=1
#     else:
#         count2+=1
# print("vowels are:",count1)
# print("consonents are:",count2)


# 25. Perfect Number Check
# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1,num):
#     if num%i==0:
#         sum+=i
# if sum==num:
#     print(sum,"is a perfect number")
# else:
#     print(sum,"is not a perfect number")

# # 26. Neon Number Check
# a=9
# b=a*a
# c=a
# sum=0
# while b>0:
#     digit=b%10
#     sum+=digit
#     b//=10
# if sum==a:
#     print('neon')
# else:
#     print("not")

# # 27.Strong Number Check
# num=145
# temp=num
# sum=0
# while temp>0:
#     fact=1
#     d=temp%10
#     for i in range(1,d+1):
#         fact*=i
#     sum+=fact
#     temp//=10
# if sum==num:
#     print(sum,"strong number")
# else:
#     print("not strong number")

# # 28. Harshad Number Check
# harsh=int(input("enter number:"))
# temp=harsh
# sum=0
# while temp > 0:
#     digit=temp%10
#     sum+=digit
#     temp//=10
# if harsh%sum==0:
#     print(sum,"is a harshed number")
# else:
#     print(sum,"is not a harshed number")


# # 29.. Fibonacci Series
# num=5
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,num+1):
#     c=a+b
#     a=b
#     b=c
#     print(c)

# # 2nd way
# num=5
# a=0
# b=1
# print(a,end=" ")
# for i in range(2,num+1):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c

# # 30. Check for Neon Number (Repeated)
# a=9
# temp=a
# b=a*a
# sum=0
# while b>0:
#     digit=b%10
#     sum+=digit
#     b//=10
# if a==sum:
#     print(sum,"is neon number")
# else:
#     print(sum,"not neon")


# separate letters,numbers,characters
# isalpha(),isdigit()

# caps=""
# small=""
# char=""
# num=""

# for i in string:
#     if i.isupper():
#         caps+=i
#     elif i.islower():
#         small+=i
#     elif i.isdigit():
#         num+=i
#     else:
#         char+=i
# print(caps)
# print(small)
# print(char)
# print(num)        


# ====----------letters and alphabets
# string="Abc123!@#"
# sy=""
# for i in string:
#     if not i.isalnum():   # if i.isalnum()
#       sy+=i
# print(sy)

# -------
# print(ord("a"))
# print(chr(97))


# string="ABcd@$%123"
# caps=" "
# small=" "
# num=" "
# symbols=" "
# count1=0
# for i in string:
#     asc=ord(i)
#     if asc>=65 and asc<=90:
#         caps+=i
#         count1+=1
#     elif asc>=97 and asc<=122:
#         small+=i
#     elif asc >=45 and asc<=57:
#         num+=i
#     else:
#         symbols+=i
# print("capital letters are:",caps,count1)
# print("small letters are:",small)
# print("digits :",num)
# print("symbols are:",symbols)


# ------------------print numbers from 1- 100
# 🔹 What is '\x01'?
# '\x01' is a special way to represent a character using its hexadecimal ASCII value.
# \x → means “hexadecimal escape sequence”
# 01 → means the hex value 1
# So '\x01' = the character with ASCII code 1

# for i in range(ord("\x01"),ord("e")):
#     print(i)




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


# a=20
# b=3
# c=15
# if (a>b and a<c):
#     print(f"{a} is second largest")
# elif (b>a and b<c):
#     print(f"{b} is second largest")
# else:
#     print(f"{c} is second largest")



# m,n=10,30
# k=" "
# for i in range(m,n):
#     for j in range(m,n):
#         if j%2==0:
#             # print("not prime")
#             pass
#             break
#     else:
#         print(j)

# for i in range(1,100):
#     for j in range(2,i):
#         if j%i==0:
#             print("no")
#         else:
#            print(j)



# a=int(input("enter:"))
# a=100
# for i in range(10,30):
#   if i>1:
#     for j in range(2,i):
#         if i%j==0:
#             # print("not prime")
#             break
#     else:
#         print(i,end=" ")
#   else:
#     print("not")    

# a=int(input("enter number:"))
# b=int(input("enter number:"))
# for i in range(a,b):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#               pass 
#               break
#         else:
#             print(i,end=" ")
#     else:
#         print("not ")

# list=[1,2,3,42,5,6,7,8]
# b=0
# # if b>list()
# for i in list:
#     if i>b:
#         b=i
#     else:
#         pass
# print(b)

# list1=[1,2,3,4]
# c=0
# tot=[ ]
# for i in list1:
#     c+=i
#     tot.append(c)
# print(tot)

# list=[1,2,3,4]
