import copy
# # list comphresnsion
# sq=[x*x for x in range(1,6)]
# print(sq)


# # shallow copy
# a = [1, 2, [3, 4]]
# b=copy.copy(a)

# b[2][0] = 99

# print(a)   # [1, 2, [99, 4]]
# print(b) 

# # set - does not allow duplicates
# a={1,2,3,4}
# b={5,5,6,7}
# print(*a,*b)    #op - 1 2 3 4 5 6 7

bb={"name":"naveen","batch":53}
cc={"village":"ndcl"}
dd={**bb,**cc}
print(dd)


