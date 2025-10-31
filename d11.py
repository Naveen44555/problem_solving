# #1 area of square
# side=5
# area=side*side
# print(area)

# #2.area of rectagle
# length=6
# breadth=4
# total=length*breadth
# print(f"area of rectagle {total}")

# #3 area of triangle
# base=8
# height=5
# area=(1/2*base*height)
# print(area)

# #4 perimeter of sq
# side=6
# perimeter=4*side
# print(f"perimeter of sq:{perimeter}")

# #5 perimeter of rectangle
# length=5
# breadth=3
# perimeter=2*(length+breadth)
# print(f"perimeter of rectangle:{perimeter}")

# #6.perimeter of triangle
# side1=5
# side2=6
# side3=7
# perimeter=side1+side2+side3
# print(f"perimeter of triangle {perimeter}")

#7 break amount into 1000s 500s,and rem change

# amount=3700
# # th=amount/1000
# thou=amount//1000     #hours
# hund=amount%1000        #min
# five_h=hund//500        #sec
# rem=hund%500
# print(f"thousands are:{thou},five hundreds are:{five_h},remaining change:{rem}")

# #8
# t_seconds=3672
# hour=t_seconds//60
# hours=hour%60
# minutes=hour%60
# seconds=t_seconds%60
# # min=hour%60
# print(f"total {hours} hour,{minutes} minute,{seconds} seconds")

# #9sum of marks (m,p,ch)
# m=85
# p=90
# ch=88
# total=m+p+ch
# print(f"total marks:{total}")

# #10.average of marks
# m=85
# ph=90
# ch=88
# total=(m+ph+ch)/3
# print("rem",round(total,3))

# #1.check even or odd
# num=int(input("enter a number:"))
# if num%2==0:
#     print('even')
# else:
#     print('odd')

# #2.
# num=int(input("enter number:"))
# if (num%5==0 and num%10!=0):
#     print("it is divisible by only 5")
# else:
#     print("satisy")

# #3 check biggest 
# a=4
# b=7
# if a>b:
#     print(f"biggest is {a}")
# else:
#     print(f"biggest is {b}")

# #4
# a=4 
# b=7
# if a<b:
#     print(f"smallest is {a}")
# else:
#     print(f"smallest is {b}")

# #5
# num=int(input("enter number:"))
# if num%2==0 and num%3==0 and num%6==0:
#     print('it is divisible by all ')
# else:
#     print("not divisible by all")

# #6
# age=int(input("enter number:"))
# if (age>=18):
#     print('you are eligible to vote')
# else:
#     print('not eligible for vote')

# #7
# m=40
# p=36
# ch=30
# if m>=35 and p>=36 and ch>=35:
#     print('you are failed in one or more subjects')
# else:
#     print('you are pass')

# #8
# m=28
# p=38
# ch=25
# if m>35 or p>=35 or ch>=35:
#     print('you pass')
# else:
#    print('you fail in all subjects') 

# #9
# m=35
# p=20
# ch=36
# if (m>=35 and p>=35) or (m>=35 and ch>=35) or (p>=35 and ch>=35):
#     print("you pass in 2 subjects or more")
# else:
#     print("you fail ")

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

# #10
# a=7
# b=4
# c=9
# if a>b and b>c:
#     print(f"a is bigger")
# elif b>a and b>c:
#     print(f'b is bigger')
# else:
#     print(f'c is bigger')

# #11
# a=7
# b=4
# c=9
# if a<b and b<c:
#     print(f"smallest is {a}")
# elif b<a and b<c:
#     print(f'smallest is {b}')
# else:
#     print(f'smallest is {c}')

# #12
# num=int(input("enter number:"))
# sq=num*num
# if num*num==sq:
#     print(f'{sq} it is perfect square for {num}')
# else:
#     print('not p-square')

# num=int(input("enter number:"))
# sq=(num**0.5)
# print(sq)


# #13
# memb=int(input("enter members:"))
# members_per_car=5
# cars_req=memb//members_per_car
# if memb%members_per_car!=0:
#     cars_req+=1
# print(cars_req)

# #14
# a=int(input("enter numbers:"))
# b=int(input("enter numbers:"))
# c=int(input("enter numbers:"))
# if (a>b and a<c) or (a<b and a>c):
#     print('a is second largest')
# elif (b>a and b<c) or (b<a and b>c):
#     print('b is second largest ')
# else:
#      print('c is second largest ')


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

