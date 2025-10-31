# #1. Check Even or Odd
# num=6
# if num % 2==0:
#     print('even number')
# else:
#     print("odd")

# #2. Divisible by 5 but Not by 10
# num=25
# if num%5==0 and num%10!=0:
#     print("satisfy")
# else :
#     print("not satisfy")

# #3. Biggest Among Two Numbers
# a=4
# b=7
# if a>b:
#     print(f"biggest is :{a}")
# else:
#     print(f"biggest is : {b}")

# #4. Smallest Among Two Numbers
# a=4
# b=7
# if a<b:
#     print(f"smallest is :{a}")
# else:
#        print(f"smallest is :{b}")

# #5.  
# num=18
# if num%2==0 and num%3==0 and num%6==0 :
#         print("satisfy")
# else:
#     print("not satisfy")
    
# #6.Voting Eligibility
# age=int(input("enter your age: "))
# if age >=18:
#     print("eligible to vote")
# else:
#     print("not eligible for vote")

# #7.Student Pass/Fail Based on All Subjects >= 35
# m=40
# p=36
# ch=30
# if m>=35 and p>=35 and ch>=35:
#     print("pass")
# else:
#     print("fail")

# #8.Student Pass if Passed Any One Subject (>= 35)
# m=20
# p=38
# ch=25
# if m>=35 or p>=35 or ch>=25:
#     print("pass")
# else:
#     print('fail')

# #9.Student Pass if Passed Any Two Subjects
# m=40
# p=20
# ch=36
# if (m>=35 and p>=35) or (m>=35 and ch>=35) or (p>=35 and ch>=35):
#     print("pass")
# else:
#     print("fail")

#2nd way
#---------------------
# m=35
# p=20
# ch=36
# if (m>=35):
#     if(p>=35 or ch>=35):
#         print('pass')
#     else:
#         print('fail')
# else:
#     if(p>=35 and ch>=35):
#         print('pass')
#     else:
#         print('fail')


# #10. Biggest Among Three Numbers
# a=7
# b=4
# c=9
# if a>b and a>c:
#     print("bigger is",a)
# elif b>a and b>c:
#     print("bigger is",b)
# else:
#     print(" bigger is ",c)

# #11. Smallest Among Three Numbers
# a=7
# b=4
# c=9
# if a<b and a<c:
#     print("smallest is",a)
# elif b<a and b<c:
#     print("smallest is ",b)
# else:
#     print("smallest is ",c)

# #12. Perfect Square or Not
# # num=int(input("enter a number: "))
# num=7
# sq=num*num
# if num*num==sq:
#     print("perfect square")
# else:
#     print("not perfect square")

#  #13. Cars Required for Members (Max 5 per car)
# members=int(input("enter members:"))
# cars=(members+4)//5
# print(f"total members are {members} and cars needed ={cars}")

# memb=59
# c=memb/5
# d=memb//5
# if memb%5==0:
#     print("c need:",c)
# elif memb%5!=0:
#     print("c need",d+1)

# #-------------type 2
# import math
# members=int(input("enter members:"))
# cars=math.ceil(members/5)
# print(f"total members are {members} and cars needed ={cars}")

# #14. Second Biggest Among Three Numbers
# a=10
# b=25
# c=18
# if (a>b and a<c) or (a<b and a>c):
#     print("second largest",a)
# elif(b>a and b<c) :
#     print("seecond largest",b)
# else:
#     print("second largest :",c)

# #15.Leap Year or Not
# year=int(input("enter year:"))
# if (year%4==0 and year%100!=0) or  year%400==0 :
#     print(f"{year} is leap year")
# else:
#     print(f"{year} not leap year")

#second way
# y=int(input("ent"))
# if (y%4==0 and y%100!=0):
#     print("leap y")
# elif(y%400==0):
#     print("lp")
# else:
#     print("not lp")


# num=134
# rev=0
# while num>0:
#     if num%10==0:
    
# year=2028
# leap=False
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             leap=True
#         else:
#             leap=False
#     else:
#         leap=True
# else:
#     leap=False


