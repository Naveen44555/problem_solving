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

# # # 4. Convert Snake Case to Camel Case
# s="my_variable_name"
# res=""
# cond=False
# for i in range(len(s)):
#     if s[i] =="_":
#         cond=True
#     elif cond:
#         res+=s[i].upper()
#         cond=False
#     else:
#         res+=s[i]
# print(res)


## 5. Convert Snake Case to Pascal Case
# s="my_variable_name"
# res=""
# under_score = False
# for i in range(len(s)):
#     if i == 0:
#         res=s[i].upper()
#     elif s[i] == "_":
#         under_score = True
#     elif under_score:
#         res+=s[i].upper()
#         under_score=False
#     else:
#         res+=s[i]
# print(res)

# # 6. Convert Camel Case to Snake Case
# name4="myVariableName" 
# rev3=""
# condition=False
# for i in range(len(name4)):
#     if name4[i]==name4[i].upper():
#         rev3+="_"
#         rev3+=name4[i].lower()
#     else:
#         rev3+=name4[i]
# print(rev3)
    

# 7. Convert Camel Case to Pascal Case
# s="abc1234"
# res=""
# for i in s:
#     if i>="0" and i<="9":
#         res+=i
# print(res)

# # # 8. Convert Pascal Case to Camel Case
# str4="MyVariable"
# s=""
# cond=False
# for i in range(len(str4)):
#     if i==0:
#         s=str4[i].lower()
#     else:
#         s+=str4[i]
# print(s)

# # 9. Convert Pascal Case to Snake Case
# str5="MyVariable"   # "my_variable"
# s5=""
# cond=False
# for i in range(len(str5)):
#     if i==0:
#         s5=str5[i].lower()
#     elif str5[i]==str5[i].upper():
#         s5+="_"
#         s5+=str5[i].lower()
#         # cond=True
#     else:
#         s5+=str5[i]
# print(s5)

# # # # 10. Convert Text to Camel Case
# word="hello world example" 
# convert=""
# cond=False
# for i in range(len(word)):
#     if word[i]==" ":
#        cond=True
#     elif cond:
#         convert+=word[i].upper()
#         cond=False
#     else:
#         convert+=word[i]
# print(convert)

# # 11. Convert Text to Snake Case
# str6="hello world example"  # hello_world_example
# s6=""
# for i in range(len(str6)):
#     if str6[i]==" ":
#         s6+="_"
#     else:
#         s6+=str6[i]
# print(s6)

# # 12. Convert Text to Pascal Case
# str7="hello world example"  # HelloWorldExample
# s7=""
# cond=False
# for i in range(len(str7)):
#     if i==0:
#         s7=str7[i].upper()
#     elif str7[i]==" ":
#        cond=True
#     elif cond:
#          s7+=str7[i].upper()
#          cond=False
#     else:
#         s7+=str7[i]
# print(s7)

# # 13. Swap Upper and Lower Case
# str8="HeLLo" 
# s8=""
# for i in str8:
#     if i==i.upper():
#         s8+=i.lower()
#     else:
#         s8+=i.upper()
# print(s8)


# # 14. Separate Digits from Text
# str9="abc123d4"    #1234
# s9=""
# for i in str9:
#     if i>="0" and i<="9":
#         s9+=i
# print(s9)

# ------------second way
# str9="abc123d4"
# s9=""
# for i in str9:
#     b=ord(i)
#     if b>=45 and b<=57:
#         s9+=i
# print(s9)

# # 15. Print Uppercase, Lowercase, Digits, and Special Characters Separately
# s="Ab123c@"
# upper=""
# lower=""
# digits=""
# symbols=""
# for i in s:
#     if i>="A" and i<="Z":
#         upper+=i+" "
#     elif i>="a" and i<="z":
#         lower+=i
#     elif i>="0" and i<="9":
#         digits+=i
#     else:
#         symbols+=i
# print("upper:",upper)
# print("lower:",lower)
# print("digits:",digits)
# print("symbols:",symbols)


# 16. Count of Uppercase, Lowercase, Digits, and Special Characters
# str="Abc@123"
# count1,count2,count3,count4=0,0,0,0
# upper=""
# lower=""
# digits=""
# symbols=""
# for i in str:
#     if i>="A" and i<="B":
#         upper+=i+" "
#         count1+=1
#     elif i>="a" and i<="z":
#         lower+=i
#         count2+=1
#     elif i>="0" and i<="9":
#         digits+=i
#         count3+=1
#     else:
#         symbols+=i
#         count4+=1
# print("upper:",upper,"total are",count1)
# print("lower:",lower,"total are",count2)
# print("digits:",digits,"total are",count3)
# print("symbols:",symbols,"total are",count4)


# 17. Check Password Strength
# strong="Abcd@1234"
# count1,count2,count3,count4=0,0,0,0
# upper=""
# lower=""
# digits=""
# symbols=""
# if (len(strong)>=8):
#     for i in strong:
#         if i>="A" and i<="Z":
#             upper+=i+" "
#             count1+=1
#         elif i>="a" and i<="z":
#             lower+=i
#             count2+=1
#         elif i>="0" and i<="9":
#             digits+=i
#             count3+=1
#         else:
#             symbols+=i
#             count4+=1
#     if count1>0 and count2>0 and count3>0  and count4>0 :
#         print("strong password")
#     else:
#          print("weak password")
# else:
#     print("password must be 8 characters or more ")
    

# second -----------------------way 

# pwd = "Abcd@234"
# upper = lower = digit = symbol = 0
# for ch in pwd:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
#     elif ch.isdigit():
#         digit += 1
#     else:
#         symbol += 1

# if len(pwd) >= 8 and upper and lower and digit and symbol:
#     print("strong password")
# else:
#     print("weak password")

# # 18. Remove Duplicates in a Given Input
# alpha1="aabbcc" 
# a1=""
# for i in alpha1:
#     if i not in a1:
#         a1+=i
#     else:
#         pass
# print(a1)


# # 19. Print Duplicates in a Given String
# alpha2="aabbccde" 
# a2=""
# a23=""
# for i in alpha2:
#     if i in a23:
#         a2+=i
#     else:
#         a23+=i
# print(a2)


# # 20. Print Next Characters in a Given String
# alpha3="abc"
# a3=""
# for i in alpha3:
#     print(chr(ord(i)+1),end="")



# a="he llo wo rld"
# for i in a:
#     if i==" ":
#         pass
#     else:
#         print(i,end="")

# a="he llo wo rld"
# b=len(a)-1
# c=0
# while b>=0:
#     if a[c]==" ":
#         pass
#     else:
#         print(a[c],end="")
#     b-=1
#     c+=1

# a="hello"
# b=""
# for i in a:
#     b=i+b
# print(b)

# a="hello"
# b=len(a)-1
# c=""
# while b>=0:
#     c+=a[b]
#     b-=1
# print(c)

# a="hello,world"
# b=a.split()
# print(b)

# a="he llo world"
# b=""
# for i in a:
#     if i==" ":
#         continue
#     b=i+b
# print(b)

# a="he llo world"
# b=len(a)-1
# c=""
# i=0
# while b>=0:
#     if a[b]==" ":
#         pass
#     else:
#         c+=a[b]
#     i+=1
#     b-=1
# print(c)

# 4.
# string1="my_variable_name"
# str2=""
# cond=False
# for i in string1:
#     if i=="_":
#         cond=True
#         continue
#     if cond:
#         str2+=i.upper()
#         cond=False
#     else:
#         str2+=i
# print(str2)

# # 5
# str1="my_variable_name"
# str2=""
# cond=False
# for i in range(len(str1)):
#     if i==0:
#         str2+=str1[i].upper()
#     elif str1[i]=="_":
#         cond=True
#     elif cond:
#         str2+=str1[i].upper()
#         cond=False
#     else:
#         str2+=str1[i]
# print(str2)
          
    
# # 6
# a="myVariableName"
# b=""
# cond=False
# for i in range(len(a)):
#     if a[i]==a[i].upper():
#         b+="_"
#         b+=a[i].lower()
#     else:
#        b+=a[i]
# print(b)

# 7
# a="myVariable"
# b=""
# for i in range(len(a)):
#     if i==0:
#         b+=a[i].upper()
#     else:
#         b+=a[i]
# print(b)

# # 8
# a="MyVariable"
# b=""
# for i in range(len(a)):
#     if i==0:
#         b+=a[i].lower()
#     else:
#         b+=a[i]
# print(b)

# # 9
# a="MyVariable"
# b=""
# for i in range(len(a)):
#     if i==0:
#         b+=a[i].lower()
#     elif a[i]==a[i].upper():
#         b+="_"
#         b+=a[i].lower()
#     else:
#         b+=a[i]
# print(b)

# 10
# a="hello world example"
# b=""
# cond=False
# for i in range(len(a)):
#     if a[i]==" ":
#          cond=True 
#         #  continue 
#     elif cond:
#          b+=a[i].upper()
#          cond=False
#     else:
#          b+=a[i]
# print(b)

# 11   
# a="hello world example"
# b=""
# for i in range(len(a)):
#     if a[i]==" ":
#         b+="_"
#     else:
#         b+=a[i]
# print(b)

# # 12
# a="hello world example"
# b=""
# cond=False
# for i in range(len(a)):
#     if i==0:
#         b+=a[i].upper()
#     elif a[i]==" ":
#         cond=True
#     elif cond:
#         b+=a[i].upper()
#         cond=False
#     else:
#         b+=a[i]
# print(b)

# a="HeLLo"
# b=""
# for i in a:
#     if i==i.upper():
#         b+=i.lower()
#     else:
#         b+=i.upper()
# print(b)

# print(ord("Z"))
# print(chr(99))

# a="HeLLo"
# b=""
# for i in a:
#     if "A" <=i <="Z":
#         b+=chr(ord(i)+32)
#     else:
#         b+=chr(ord(i)-32)
# print(b)

# # 14
# a="abc1234d"
# b=""
# for i in a:
#     if "0"<=i<="9":
#         b+=i
# print(b)

# char="ABcd123!@#"
# caps=""
# small=""
# digits=""
# symb=""
# for i in char:
#     if "A"<=i<="Z":
#         caps+=i
#     elif "a"<=i<="z":
#         small+=i
#     elif "0"<=i<="9":
#         digits+=i
#     else:
#         symb+=i
# print(caps,small,digits,symb)

# char="ABcd123!@#"
# caps=""
# small=""
# digits=""
# symb=""
# for i in char:
#     if "a"<=i<="z":
#         small+=i
#     elif "A"<=i<="Z":
#         caps+=i
#     elif "0" <=i<="9":
#         digits+=i
#     else:
#         symb+=i
# print(caps,small,digits,symb)


# password=input()
# caps=0
# small=0
# dig=0
# symb=0
# if len(password):
#     for i in password:
#         if "A"<=i<="Z":
#             caps+=1
#         elif "a"<=i<="z":
#             small+=1
#         elif "0"<=i<="9":
#             dig+=1
#         else:
#             symb+=1
#     if caps>=1 and small>=1 and dig>=1 and symb>=1:
#         print("strong password")
#     else:
#         print("weak password")
# else:
#      print("weak password")

# 18
# a="aabbcc"
# b=""
# for i in a:
#     if i not in b:
#        b+=i
# print(b)

# a="aabbcced"
# b=""
# c=""
# for i in a:
#     if i not in b:
#         b+=i
#     else:
#         c+=i
# print(c)

# a="abc"
# b=""
# for i in a:
#     if "a"<=i<="z":
#         b+=chr(ord(i)+1)
# print(b)
    
