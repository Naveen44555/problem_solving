# a={1,2,3,3,4,4}
# print(a)

# a={1,2,3,3,4,4}
# a.add(7)
# a.remove(9)
# a.discard(9)
# print(a)

# a={1,2,3,3,4,4}
# b={5,2,4,8}
# a=a.union(b)  #union() → returns new set 
# # a=a | b
# print(a)

# c=a&b
# c=a.intersection(b)
# print(c)

# --
# a={1,2,3,8}
# b={5,2,3}
# # c=a.difference(b)
# print(a - b)

# a={1,2,3}
# b={2,3,4}
# print(a.issubset(b))
# print(len(a))
# a.clear()
# c=a^b
# print(c)

# a=[1,2,3,4,2]
# b=set(a)
# print(b)

# keys=["a","b"]
# values=[1,2]
# c=dict(zip(keys,values))
# print(c)

# a={"a":1}
# a["a"]=2
# print(a)

# a={"a":1,"b":2}
# # v=a.pop("b")
# del a["b"]
# print(a)

# b={"x":1}
# print("x" in b)

# a={"a":1,"b":2,"c":4}
# print(len(a))
# for i in a.keys():
#     print(i)

# for i in a.values():
#     print(i)

# for i in a.items():
#     print(i)

# a={"a":1}
# b={"b":2}

# c={**a,**b}
# print(c)

# c=a | b
# print(c)

# a.update(b)
# print(a)

# ---
# a={"a":1}
# print(a.get("b",0))

# a=[1,2,3,4,4,2]
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)

# a={"a":1,"b":2,"c":4}


# -------------- neww222
# a={1,2,3}
# b={3,4,5}
# a.add(4)
# a.remove(5)
# a.discard(5)
# a=a.union(b)
# a=a | b
# a.update(b) 
# print(a)

# a={1,2,3}
# b={2,3,4}
# print(a & b)
# print( a.intersection(b))
# print(a-b)
# print(a.difference(b))


# a={1,2,3}
# b={2,1,3,4}

# print(a.issubset(b))
# print(len(a))

# a.clear()
# print(a)
# print(a)


# print(a^b)
# print(a.symmetric_difference(b))
# print(set(a))

# a=["a","b"]
# b=[1,2]
# print(dict(zip(a,b)))

# a={"a":1}
# a["b"]=2
# print(a)

# a={"a":1,"b":2,"c":3}
# # a.pop("d")
# # del a["c"]
# print(a)


# a={"z":1,"x":2}
# nn="x"
# print(nn in a)

# a={"a":1,"b":3,"c":3,"a":2,"b":4}
# for i,j in a.items():
#     print(i,j)
# print(len(a))
# print(a)
# b={"z":2,"b":2}
# print (a | b)
# a.update(b)
# print(a.get("b"))

# a=[1,2,3,3,4,4,5,6]
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)

a={"a":1,"b":3,"c":3}
# b={}
# for i,j in a.items():
#     b[j]=i
# print(b)
# 

# a={"a":1,"b":3,"c":3}
# max_val=float("-inf")
# result=[]
# for k,v in a.items():
#     if v>max_val:
#         max_val=v
#         result=[k]
#     elif v==max_val:
#         result.append(k)
# print(result)


# a={"a":3,"b":3,"c":1}
# max_key=[]
# max_value=0
# for k,v in a.items():
#     if v>max_value:
#         max_value=v
#         max_key=[k]
#     elif v==max_value:
#         max_key.append(k)
# print(max_key)


# a={"a":3,"b":3,"c":1}
# print(sorted(a.items(),key=lambda x:x[1]))

# a=(1,4)
# d={i:i*i for i in range(1,4)}
# print(d)

# a={"a": 10, "b": 5, "c": 15}
# great=10
# op={}
# for k,v in a.items():
#     if v > great:
#         op[k] = v
# print(op)

# a={"a": 1, "b": 2}
# b={"a": 3, "c": 4}
# res=a.copy()
# for k,v in b.items():
#     if k in res:
#         res[k]+=v
# print(res)

# a="apple apple banana"
# words=a.split()
# d={}
# for w in words:
#     d[w] = d.get(w,0) + 1
# print(d)

# a={"a": 1, "b": 2, "c": 1}
# key=1
# for k,v in a.items():
#     if v ==k:
        
# a={"a":1,"b":2}
# b={}
# for k,v in a.items():
#     if k not in b:
#         b[v]=k
# print(b)

a={"a":1,"b":2,"c":1}
b={}
val=1
for k,j in a.items():
    if j!=val:
          b[k]=j
print(b)

