# # 1. Remove Spaces from Given Text

# a="naveen kum ar"
# b=" "
# for i in a:
#     if i==" ":
#         pass
#     else:
#         b+=i
# print(b)

# def space(n):
#     b=""
#     for i in n:
#         if i ==" ":
#             pass
#         else:
#             b+=i
#     print(b)
# space("he llo world")

# # 2. Reverse a String
# def name(str):
#     a=""
#     for i in str:
#         a=i+a
#     print(a)
# name("hello")

# str="hello"
# rev=" "
# for i in range(len(str)-1,-1,-1):
#     rev=rev+str[i]
# print(rev)


# def name(str):
#     rev=""
#     for i in range(len(str)-1,-1,-1):
#         rev+=str[i]
#     print(rev)
#     # return rev
# name("hello")


# def name2(str3):
#     a=""
#     b=""
#     for i in name2:
#         if i==" ":
#             # rev+=i
#             pass
#         else :
#             rev+=i
#     for i in range(len(rev-1),-1,-1):
#         b+=i
#     print(b)
# name2("he llo wo rld")


s="my_variable_name"
res=""
under_score = False
for i in range(len(s)):
    if i == 0:
        res=s[i].upper()
    elif s[i] == "_":
        under_score = True
    elif under_score:
        res+=s[i].upper()
        under_score=False
    else:
        res+=s[i]
print(res)


    




