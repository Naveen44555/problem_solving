# s=open("demo.txt",mode="r")
# print(s.read())

# s=open("demo.txt",mode="a")
# s.write("/n bye good ni8")

# s=open("demo.txt", mode="r+")
# print(s.read())
# s.write("nice")

s=open("demo.txt",mode="w+")
s.write("where")
print(s.read())
s.close()