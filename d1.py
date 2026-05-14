# # find second largest
# arr=[2,23,4,35,4,469,3,22,42,624,252]
# first=sec=float("-inf")
# for i in arr:
#     if i>first:
#         sec=first
#         first=i
#     elif i>sec:
#         sec=i
# print(f"Second largest: {sec}")


# 3
# 4 5 6 7 8

# n=int(input())
# values = list(map(int,input().split()))
# # for i in len(values):
# print(values)


# a, b = map(int, input().split())
# print(a + b)


# arr=input().strip("[]").replace("'","").split("")
# print(arr)

# arr=input().replace("'","")
# print(arr)


# n1=int(input())
# arr=[]
# for i in range(n1):
#     n2=int(input("enter:"))
#     arr.append(n2)
# print(arr)


# arr2=[2,23,4,35,4,46,3,22,42,24,252]
# first=sec=float("-inf")
# for i in arr:
#     if i>first:
#         sec=first
#         first=i
#     elif 
        













# #1.area of square
# side=5
# area=side*side
# print(f"Area of square is:{area}")

# #2.area of rectangle
# length=6
# breadth=4
# area=length*breadth
# print(f"Area of rectangle is :{area}")

# #3.area of triangle
# base=8
# height=5
# area=1/2*base*height
# print(f"Area of triangle:{area}")

# #4.perimeter of square 
# side=6
# perimeter=4
# print(f"perimeter of square is {side*perimeter}")

# #5.perimeter of rectangle
# length=5
# breadth=3
# print(f"perimeter of rectangle is :{2*(length+breadth)}")

# #6.perimeter of triangle
# side1=5
# side2=6
# side3=7
# print(f"perimeter of triangle is:{side1+side2+side3}")

# #7. Break Amount into 1000s, 500s, and Remaining Change
# amount=3700
# thousnds=amount//1000
# th=amount%1000

# five_h=th//500
# f_h=th%500

# change=f_h
# print(f"1000s:{thousnds} 500s : {five_h} Remaining : {change}")

# #---------------------second type
# money=3700
# th=money//1000
# rem=money%1000
# fiv=rem//500
# change=rem%500
# print(f"1000s {th} 500s {fiv} rem {change}")

# #8.Convert Seconds into Hours, Minutes, and Seconds
# seconds=3672
# min=seconds//60     
# hours=min//60       #hours
# minutes=min%60      #minutes
# h=seconds%60        #seconds
# sec=h
# print(f" Hours {hours} - minutes {minutes} - sec {sec}")

# #9. Sum of Marks (Maths, Physics, Chemistry)
# m=90
# p=90
# ch=88
# print(f"Total marks : {m+p+ch}")

# #10.. Average of Marks (Maths, Physics, Chemistry)
# m=85
# p=90
# ch=88
# t=(m+p+ch)/3
# # print(f"Average marks : {(m+p+ch)/3}")
# print("average :",round(t,4))


# members=int(input("enter"))
# memb=members//5


# # ---------------
# side =5
# area = side * side
# print(area)

# amount=3700
# th=amount //1000
# rem=amount % 1000
# hun=rem //500
# change=rem%500
# print(th,hun,change)

# tot=3672
# h=tot //60
# hours=h // 60
# min = h % 60
# sec = tot % h
# print(hours,min,sec)

# tot =3672
# h= tot // 60
# hours = h//60
# min=h%60
# sec=tot % h
# print(hours,min,sec)

# m,p,ch=85,90,88
# tot=(m+p+ch)/3
# print(round(tot,3))
