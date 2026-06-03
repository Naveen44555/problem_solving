# a=int(input())
# if a%2==0 and a%3==0 and a%6==0 :
#     print("ye")
# else:
#     print("no")

# a=int(input())
# cars=a//5
# if a%5==0:
#     print(cars,"req")
# else:
#     print(cars+1,"rqllll")

# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     if (i%4==0 and i%100!=0) or (i%400==0):
#         print(i,"leap")
#     # else:
#     #     print("no")

# for i in range(a,-1,-1):
#     print(i)


# a="helllo"
# print(a[1::-1])

# a=int(input())
# b=1
# # i=0
# while a>0:
#     c=a%10
#     b*=c
#     a//=10
#     # i+=1
# print(b)


# a=int(input())
# b=a
# leng=0
# while b>0:
#     leng+=1
#     b//=10
# c=a
# value=0
# while c>0:
#     d=c%10
#     value+=d**leng
#     c//=10
# if value==a:
#     print(value,"arm")
# else:
#     print(value,"not")

    
# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     b=i
#     leng=0
#     while b>0:
#         leng+=1
#         b//=10
#     c=i
#     value=0
#     while c>0:
#         d=c%10
#         value+=d**leng
#         c//=10
#     if value==i:
#         print(value,"arm")
#     # else:
#     #     print(value,"not")


# a=int(input())
# c=0
# while a>0:
#     d=a%10
#     c=c*10+d
#     a//=10
# print(c)


# a=int(input())
# b=0
# for i in range (1,a):
#     if a%i==0:
#         b+=i
# if b==a:
#     print(b,"perfect num")
# else:
#     print(b,"not")


# a=int(input())
# b=a*a
# c=0
# while b>0:
#     d=b%10
#     c+=d
#     b//=10
# if c==a:
#     print(c,"neon")
# else:
#     print(c,"not")


# a=int(input())
# b=a
# c=0
# while b>0:
#     d=b%10
#     fact=1
#     for i in range(1,d+1):
#         fact=fact*i
#     c+=fact
#     b//=10
# if a==c:
#     print(c,"strong")
# else:
#     print(c,"not strong")


# a=int(input())
# b=a
# d=0
# while b>0:
#     c=b%10
#     d+=c
#     b//=10
# if a%d==0:
#     print(d,"ha")
# else:
#     print(d,"not")

# n=int(input())
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b




# a=[0,2,4,0,5,0,66,45,0,33,0,32]
# j=0
# for i in range(len(a)):
#     if a[i]!=0:
#         a[i],a[j]=a[j],a[i]
#         j+=1
# print(a)


# a=[1,2,3,5]
# for i in range(len(a)-1):
#     if a[i]+1 != a[i+1]:
#         print(a[i]+1,"missing")
        
# # print("even" if 10%2==0 else "odd")
# op=lambda:print("hello")
# # print(op())
# op()

# op=lambda x : x+2
# print(op(4))

# def ad(a,b):
#     return a+b
# print(ad(2,8))



# a=int(input( ))
# b=int(input( ))
# for i in range(a,b+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i,end=" ")
