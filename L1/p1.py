# a=10.0
# print(int(a))   #explicit type conversion

#string methods
a="1Naveen nnn nn"
# print(a.upper())

# print(a.lower())-------True or false
# print(a.endswith('n'))
# print(a.startswith('N'))
# print(a.startswith('N'))

# print(a.startswith('1'))

# print(a.replace("1e","kumar"))

# print(a.split(" "))     #comma seperate
print(a.split())     #comma seperate

print(a.split(","))    #no commas

print(a.split(" ",8)) 

para="hello\nworld\npython"
r=para.split(" ",2)
print(r)

a=" i love python programminng"
for word in a.split(" "):
    print(word)

# b="nn,jj,kkl,w"
# r=b.split()
# res=" ".join (r)
# print(res)

# b="jj kk ddk eke"     #separate woth comma
# a=b.split()
# c="   ".join (a)
# print(c)

# #count
# c="naveen"
# print(c.count("n"))

# #strip
# c="     naveen         "
# print(c.strip())
# print(c.lstrip())
# print(c.rstrip)

#remove suffix
a="python life"
# print(a.removesuffix('life'))
# # print((a.removeprefix('py')))

# #index ------number
# print(a.index("e"))

#find
print(a.find("i"))

# print(a.rfind("a"))


# a=int(input("enter year"))
# b=[]
# for i in range(0,a+1):
#     if (a%4==0 and a%100!=0) or a%400==0 :
#         b.append(i)
# print(b)
#     # else:
#     #     print("non-leap years:",b)

a = int(input("Enter year: "))
lp = []  # list to store leap years
nonlp=[]

for i in range(0, a + 1):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        lp.append(i)  # store leap year
    else:
        nonlp.append(i)
print("Leap years from 0 to", a, "are:")
print(lp)
print("non lp:",a,"are:")
print(nonlp)