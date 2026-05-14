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
     
# a = [1, 2, 3]
# b = [1, 2, 3]

# print(id(a))
# print(id(b))

# print(a is b)   # False  (stored in different memory locations)

# a=[1,2,3]
# a.append(4)
# print(a)

# a=[1,2,3]
# a.remove(3)
# print(a)

# a=[3,2,343,2,4,10,2]
# print(max(a))
# print(min(a))

# print(sum(a))
# print(a.count(2))

# a=[3,2,343,2,4,10,2]
# l=len(a)-1
# b=[]
# for i in range(l,-1,-1):
#     b.append(a[i])
# print(a)


# print(a[::-1])

# # 8
# a=[2,1,4,3]
# a.sort()
# print(a)

# a=[1,2,2,3,4,4]
# b=[]
# # a.set()
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# print(list(set(a)))

# print(list(dict.fromkeys(a)))

# a=[1,2,3]
# b=[4,5,6]
# print(a+b)

# a.extend(b)
# print(a)

# a=[1,2,3]
# b=[2,3,6]
# c=[]
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

# a=[1,2,3,4]
# b=[]
# for i in a:
#     if (i//2)*2==i:
#         b.append(i)
# print(b)

# a=[2,3,4,5,6]
# b=[]
# for i in a:
#     if i & 1!=0:
#         b.append(i)
# print(b)


# a=[1,2,3,10]
# b=[]
# for i in range(len(a)-1):
#     if a[i]>1:
#         for j in range(2,a[i]):
#             if a[i]%j==0:
#                  break                 
#         else:
#             b.append(a[i])
# print(b)    
    

# a=[0,3,4,0]
# pos=neg=zero=0
# for i in a:
#     if i==0:
#         zero+=1
#     elif i>0:
#         pos+=1
#     elif i<0:
#         neg+=1
# print(pos,neg,zero)


# a=[-2,-44,-23,-54,-43,9,0,-37]
# largest=a[0]
# for i in a:
#     if i>largest:
#         largest=i
# print(largest)

# a=[2,844,23,54,8,43,99,37]
# largest=a[0]
# sec_largest=largest
# for i in a:
#     if i>largest:
#         sec_largest=largest
#         largest=i
#     elif i>sec_largest and i!=largest:
#         sec_largest=i
# print(sec_largest)

# a=[-2,844,23,94,8,43,-99,37]
# largest=sec_largest=third_larg=float("-inf")
# for i in a:
#     if i>largest:
#         third_larg=sec_largest
#         sec_largest=largest
#         largest=i
#         print(largest,"ll")
#     elif i>sec_largest and i!=largest:
#         third_larg=sec_largest
#         sec_largest=i
#     elif i>third_larg and i!=largest and i!=sec_largest:
#         third_larg=i
# print(largest,sec_largest,third_larg)

# a=[-2,-844,23,94,0,43,99,37]
# smallest=sec_small=third_small=float("inf")
# for i in a:
#     if i<smallest:
#         third_small=sec_small
#         sec_small=smallest
#         smallest=i
#     elif i<sec_small and i!=smallest:
#         third_small=sec_small
#         sec_small=i
#     elif i<third_small and i!=sec_small and i!=smallest:
#         third_small=i
# print(smallest,sec_small,third_small)

# a=[1,2,3]
# b=a.copy()
# c=a[:]
# # b.append(4)
# print(b,a,c)

# a=[1,2,3,4,5]
# b=[]
# for i in a:
#     if i>1:
#       for j in range(2,i):
#          if i%j==0:
#             break
#       else:
#          b.append(i)
# print(b)

# a=[0,2,0,3]
# for i in range(len(a)):
#     if a[i]==0:
#         a[i]=-1
# print(a)

# a=[5,5,5,5]
# b=a[0]
# c=True
# for i in range(len(a)):
#     if a[i]!=b:
#         c=False
# print(c)

# a=[1,2,3,4,2,1,4]
# freq={}
# for i in a:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)

# ------------------------
# a=[1,2,3,3,4,4,2]
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)

# a=[[1,2],[3,4]]
# b=[]
# for i in a:
#     for j in i:
#        b.append(j)
# print(b)

# a=[1,2,3,4,5]
# even=[]
# odd=[]
# for i in a:
#     if (i//2)*2==i:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even,odd)

# a=[1,2,3,4]
# target=5
# pairs=[]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==target:
#             pairs.append((a[i],a[j]))
# print(pairs)

# a=[1,2,3,4,5]
# b=[]
# c=[]
# for i in a:
#     if (i//2)*2==i:
#         b.append(i)
#     else:
#         c.append(i)
# print(b,c)

# a=[1,2,3,4,5]
# b=[]
# for i in a:
#     e=i*2
#     b.append(e)
# print(b)

# a=[4,1,2,7]
# larg=max(a)
# smal=min(a)
# for i in range(larg):
#     if i+smal==larg:
#         print(i,"diff")

# a=[2]
# # if len(a)==0:
# #     print("empty")

# if not a:
#     print("emp")

# def empty(a):
#     if len(a)==0:
#        return True
#     else:
#         return False
# print(empty([]))

# a=[1,2,3,4]
# a.insert(2,33)
# print(a)

# a=[1,2,2,3,3]
# # a.remove(2)
# # print(a)

# while 2 in a:
#     a.remove(2)
# print(a)

# # 32
# a=[2,3,4,5]
# print(a.index(4))

# a=[2,3,4]
# b=[]
# for i in a:
#     e=i**2
#     b.append(e)
# print(b)
    
# # 35
# a=[2,-3,-6,9,-8]
# b=[]
# for i in a:
#     if i>0:
#         b.append(i)
# print(b)

# a=[2,4,64,33,557,7,4]
# b=[]
# for i in a:
#     if i>33:
#         b.append(i)
# print(b)

# a=[1,22,22,33,22,5,33]
# b=[]
# c=[]
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
#         # continue
#     else:
#         b.append(i)
# print(c)

# a=[1,2,3,4]
# k=2
# b=[]
# for i in range(k,len(a)):
#     b.append(a[i])
# for j in range (k):
#     b.append(a[j])
# print(b)

a=[1,2,3,4,5,6]
b=[]
c=0
size=2
for i in range(c,len(a)//2):
    b.append([a[c],a[c+1]])
    c+=2
print(b)

a = [1,2,3,4,5,6,7,8]
b = []
for i in range(0, len(a), 2):
    b.append([a[i], a[i+1]])
print(b)
