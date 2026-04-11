# # format of Logical questions
# a=10
# for i in range(a):
#     print(i)

# a="naveen"
# for i in a:
#     print(i)

# # 2.testing
# n=10
# for i in n+1:
#     if i==n:
#         print("stop")

# # # to perform operation, then we need data with programmer structure / data structure are :
# #   integer  structure
# #    float structure
# #   boolean structure
# #  string structure
# #  list  structure
# #  dict(object) structure
# # === advanced data structure
# #     linked list structure
# #    stack object structure
# #    array list & vector structure

# # ===set  structure are
# #    hashmap structure
# #    linkedhashset structure
# #   treeset structure
# #  === key & value  structure
# #  hashmap  structure
# #   linkedhashmap structure
# #    structure
# #    structure


# # starting
# # a=10 int
# # b=11.3 float
# # c=True boolean
# # d="honey" string

# a=1056
# value=str(a)
# print(f"highest_value: {max(value)}")
# print(f"Lowest_value: {min(value)}")

a = 1056
b = a
highest = 0
lowest = 9
while b > 0:
    digit = b % 10   
    if digit > highest:
        highest = digit
    if digit < lowest:
        lowest = digit
    b = b // 10     
print("Highest digit:", highest)
print("Lowest digit:", lowest)

# 2
b="raavi"
rev=""
dict1={}
for i in b:
    rev=rev+i
for i in rev:
    if i in dict1:
      dict1[i]+=1
    else:
       dict1[i]=1
print(dict1)


# 3.
# a=[10,20,30,50,67,43]
# # first_lar=sec_larg=float("-inf")
# first_lar=a[0]
# sec_larg=first_lar
# for i in a:
#    if i>first_lar:
#        sec_larg=first_lar
#        first_lar=i
#    elif i>sec_larg and i!=first_lar:
#        sec_larg=i
# print("sec_largest:",sec_larg)


# a=[10,20,30,50,67,43]
# b=len(a)
# for i in range(b):
#     for j in range(i+1,b):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)


# a=[10,20,30,50,67,43]
# b=len(a)
# for i in range(b):
#     for j in range(i+1,b):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)


# class student:
#     def names(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
# b=student()
# b.names("naveen","raju","honey")
# print(b.a,b.b,b.c)


class student:
    def names(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
b=student()
b.names("naveen","raju","honey")
print(b.a,b.b,b.c)



