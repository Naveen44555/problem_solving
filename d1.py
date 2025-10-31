#1.area of square
side=5
area=side*side
print(f"Area of square is:{area}")

#2.area of rectangle
length=6
breadth=4
area=length*breadth
print(f"Area of rectangle is :{area}")

#3.area of triangle
base=8
height=5
area=1/2*base*height
print(f"Area of triangle:{area}")

#4.perimeter of square 
side=6
perimeter=4
print(f"perimeter of square is {side*perimeter}")

#5.perimeter of rectangle
length=5
breadth=3
print(f"perimeter of rectangle is :{2*(length+breadth)}")

#6.perimeter of triangle
side1=5
side2=6
side3=7
print(f"perimeter of triangle is:{side1+side2+side3}")

#7. Break Amount into 1000s, 500s, and Remaining Change
amount=3700
thousnds=amount//1000
th=amount%1000

five_h=th//500
f_h=th%500

change=f_h
print(f"1000s:{thousnds} 500s : {five_h} Remaining : {change}")

#---------------------second type
money=3700
th=money//1000
rem=money%1000
fiv=rem//500
change=rem%500
print(f"1000s {th} 500s {fiv} rem {change}")

#8.Convert Seconds into Hours, Minutes, and Seconds
seconds=3672
min=seconds//60     
hours=min//60       #hours
minutes=min%60      #minutes
h=seconds%60        #seconds
sec=h
print(f" Hours {hours} - minutes {minutes} - sec {sec}")

#9. Sum of Marks (Maths, Physics, Chemistry)
m=90
p=90
ch=88
print(f"Total marks : {m+p+ch}")

#10.. Average of Marks (Maths, Physics, Chemistry)
m=85
p=90
ch=88
t=(m+p+ch)/3
# print(f"Average marks : {(m+p+ch)/3}")
print("average :",round(t,4))


