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


# # sorted ascending order ---b d d h j r s s
# def char(s):
#     name ="".join(sorted(s))
#     return name
# user_input=input("give:")
# res=char(user_input)
# print(list(res))

# # strong number
num=145
dum=num
res=0
while dum>0:
    n=dum%10
    fact=1
    for i in range(1,n+1):
        fact*=i
    res+=fact
    dum//=10
if res==num:
    print(res,"strong number")
else:
     print("not strong number")


# perfect number 
n=int(input("enter:"))
b=0
for i in range(1,n):
       if  n%i==0:
            b+=i
if b==n:
    print(n,"is perfect number")
else:
      print(n,"is not perfect number")

# -----------buzz number
def buzz(n):
    div=(n%7==0)
    ends=(n%10==7)
    if div or ends:
        print(div,"buzz")
    else:
        print("not buzz")
buzz(7)

# -------2nd way
num=int(input("enter:"))
if num%7==0:
    print("buzz number")
else:
    d= num%10
    if d==7:
        print(num,"it buzz number")
    else:
        print("not buzz number")


# -------3rd way
num4=int(input("enter:"))
value=1
if num4%7==0:
    print("buzz")
else:
    while True:
        value1=num4%10
        if value1==7:
            print("buzz num")
            break
        else:
            print("not buzz")
            break

# -------------
def val(num):
    if num%7==0:
        print("buzz")
    elif num%10==7:
        print("buzz")
    else:
        print("not buzz")
val(int(input("number")))


def merge(s1,s2):
    list1=[]
    i=0
    j=0
    while(i<len(s1) or j<len(s2)):
        if i<len(s1):
            list1.append(s1[i])
            i+=1
        if j<len(s2):
            list1.append(s2[j])
            j+=1
    return "".join(list1)
print(merge("pavan","kalyan"))

# two dict add--------
n1={'name':"naveeen"}
n2={"age":33}
n3={**n1,**n2}
print(n3)

# n1={1,2,3}
# n2={5,6,7}
# n3={*n1,*n2}
# print(n3)

# num=int(input("enter:"))
# dum=num
# res=0
# while dum > 0:
#     d=dum%10
#     fact=1
#     for i in range(1,d+1):
#         fact*=i
#     res+=fact
#     dum//=10
# if res==num:
#     print(res,"strong number")
# else:
#     print(res,"not strong numbere")
 
# num=int(input("enter:"))
# perfect=0
# for i in range(1,num):
#     if num%i==0:
#         perfect+=i
# if perfect==num:
#     print(perfect,"perfect number")
# else:
#     print(perfect," not perfect number")


# def names(s1,s2):
#     lst=[]
#     i=0
#     j=0
#     while(i<len(s1) or j<len(s2)):
#         if i<len(s1):
#             lst.append(s1[i])
#             i+=1
#         if j<len(s2):
#             lst.append(s2[j])
#             j+=1
#     return "".join(lst)
# print(names("pavan","kalyan"))


                  


