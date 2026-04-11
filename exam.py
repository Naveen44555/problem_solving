import copy
# # list comphresnsion
# sq=[x*x for x in range(1,6)]
# print(sq)


# # shallow copy
# a = [1, 2, [3, 4]]
# b=copy.copy(a)
# print(b)

# b[2][0] = 99

# print(a)   # [1, 2, [99, 4]]
# print(b) 

# # set - does not allow duplicates
# a={1,2,3,4}
# b={5,5,6,7}
# print(*a,*b)    #op - 1 2 3 4 5 6 7
# # print(a,b)  {1, 2, 3, 4} {5, 6, 7}

# cc={33,4,5,66,34}
# dd={32,45,54,66,223}
# print(cc.union(dd))
# # print(cc | dd)
# cc.update(dd)
# print(cc)


bb={"name":"naveen","batch":53}
cc={"village":"ndcl"}
print(*bb,*cc)
dd={**bb,**cc}
print(dd)

