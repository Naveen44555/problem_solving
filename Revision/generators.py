def arr(fun):
    for i in range(fun):
        yield i
g=arr(4)
# print(next(g))
# print(next(g))
print(g.__next__())
print(g.__next__())
print(g.__next__())
# for j in g:
#     print(j)
    