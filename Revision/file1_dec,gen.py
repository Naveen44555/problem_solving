# p1=open("myfile5.txt","w")
# # p1.write("hellowl m")
# print(p1.read())


# s=open("demo3.txt","w")
# s.write("hello")
# s.close()

# s=open("demo3.txt","r")
# print(s.read())


# s=open("demo3.txt","a")
# s.write("naveen \n")
# s.close()

# s=open("demo3.txt","r")
# print(s.read())

# ==-------------
# s=open("mine.txt",mode="x")
# s=open("mine.txt",mode="r")
# print(s.read())

# s=open("mine.txt","w")
# s.write("helo")

# s=open("mine.txt","r")
# print(s.read())

# s=open("mine.txt","w")
# s.write("naveen")
# s.close()

# s=open("mine.txt","r")
# print(s.read())

# s=open("mine.txt","a")
# s.write("hello\n")
# s.close()

# s=open("mine.txt","r")
# print(s.read())

# s=open("mine.txt","w+")
# s.write("morin")
# print(s.read())

# with open("mine.txt","r")as m:
#     print(m.read())

# with open("mine2.txt","w")as mm:
#     mm.write("evng")
#     print(mm.tell())


# def gen(a):
#     for i in range(a):
#         yield i
# g=gen(4)
# # print(next(g))
# for j in g:
#     print(j)


# def dec(fun):
#     def wrapper():
#         print("before")
#         fun()
#         print("after")
#     return wrapper
# @dec
# def say_hi():
#     print("hello")
# say_hi()




# def dec(fun):
#     def wrapper():
#         print('before')
#         fun()
#         print("after")
#     return wrapper
# @dec
# def say_helo():
#     print("hii")
# say_helo()

# def gen(a):
#     for i in range(a):
#         yield i
# g=gen(4)
# for j in g:
#     print(j)

# def dec(fun):
#     def wrapper():
#         print("before")
#         fun()
#         print("after")
#     return wrapper
# @dec
# def sample():
#     print("hii")
# sample()


# ---
# # method overloading
# class Test:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# t = Test()
# t.add(1,3,9)

# # method overriding
# class parent:
#     def speak(self):
#         print("speak")
# class dog(parent):
#     def speak(self):
#         print("dog sp")
# class cat(dog):
#     def speak(self):
#         print("cat sp")
# g=parent()
# dg=dog()
# dg.speak()


# class ml:
#     def summ(self,a,b):
#         print(a+b)
#     def summ(self,a,b,c):
#         print(a+b+c)
# m=ml()
# m.summ(3,4,5)

# class grandparent:
#     def speak(self):
#         print("gp speak")
# class parent(grandparent):
#     def speak(self):
#         print("parent sp")
# class child(parent):
#     def speak(self):
#         print("child sp")
# gp=grandparent()
# gp.speak()
# par=parent()
# par.speak()

