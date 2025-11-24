# # 1. Add an Element to a List
# a=[1,2,3]
# a.append(4)
# print(a)

# # -----without append--- second way
# a=[1,2,3]
# b=[4]
# print(a+b)

# # 2. Remove an Element from a List
# a2=[1,2,3,4]   
# a2.remove(3)     #remove specific element
# a2.pop()        #last element
# print(a2)

# # 3. Find Maximum in List
# a3=[4,7,1,9]
# print(max(a3))

# # 4. Find Minimum in List
# a4=[4,7,1,9]
# print(min(a4))

# # # 5. Sum of All Elements in List
# a5=[1,2,3]
# sum1=0
# # print(sum(a5))   #method using

# # second ----way
# for i in a5:
#     sum1+=i
# print(sum1)

# # 6. Count Occurrence of an Element
# a6=[1, 2, 2, 3,2,]
# co1=[]
# count=1
# for j in a6:
#    if j in co1:
#       count+=1
#    else:
#       co1.append(j)
# print(count)

# # # 7. Reverse a List
# a7=[1,2,3]
# # # print(a7[2::-1])
#    #reverse
# print(a7.reverse())

# # # 8. Sort a List
# a8=[4,1,3,2]
# # a8.sort()
# print(a8)
# # descending order
# print(sorted(a8,reverse=True))


# # 9. Remove Duplicates from a List
# a9=[1,2,2,3]
# a9=list(set(a9))
# print(a9)

# a9=[1,2,2,3]
# a99=[]
# for i in a9:
#     if i not in a99:
#         a99.append(i)
#     else:
#         pass      
# print(a99)


# # 10. Merge Two Lists
# a=[1,2,3]
# b=[4,5]
# print(a+b)      

# # second way
# a.extend(b)
# print(a)

# # 11. Find Common Elements in Two Lists
# ab=[1,2,3,3]
# bc=[2,3,4]
# # ab.sort()

# # 12. Print Even Numbers in a List
# a10=[1,2,3,4]
# b=[]
# for i in a10:
#     if i%2==0:
#         b.append(i)
# print(b)

# # 13. Print Odd Numbers in a List
# a11=[1,2,3,4]
# b=[]
# for i in a11:
#     if i%2!=0:
#         b.append(i)
# print(b)

# 14. Check if List is Palindrome


# # 15. Count Positive, Negative, Zero
# a13=[0,-1,-2,-3,4]
# positive=[]
# zero=[]
# neg=[]
# for i in a13:
#     if i>0:
#         positive.append(i)
#     elif i==0:
#         zero.append(i)
#     else:
#         neg.append(i)
# print('positive:',positive)
# print('negative:',neg)
# print('zero:',zero)


# a133=[0,-1,2,-3,4]
# c1,c2,c3=0,0,0
# for i in a133:
#     if i>0:
#         c1+=1
#     elif i==0:
#         c2+=1
#     else:
#         c3+=1
# print('positive:',c1)
# print('negative:',c2)
# print('zero:',c3)


# # 16. Find Second Largest Number in List
# a14= [1, 3, 4, 5, 0] 
# aa=[]
# for i in a14:
     
a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))

# print(a is b)   # False  (stored in different memory locations)

