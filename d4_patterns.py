# # # 1.	Solid Square Pattern
# n=int(input("enter a number"))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

# 2.	Solid Rectangle Pattern
# n=4
# for i in range(n-1):
#     for j in range(n+1):
#           print("* ",end=" ")
#     print()

# # 3.	Right-Angled Triangle (Left-Aligned)
# p=5
# for i in range(p):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

p=5
for i in range(p):
    for j in range(p-i):
          print(" ",end=" ")
    for k in range(i):
         print("*",end=" ")
    print()

# p=5
# for i in range(p):
#     s=""
#     for j in range(p):
#         if j==p-1 or i==p-1 or j==p-j:
#           s+="*"+" "
#         else:
#            s+=" "+" "
#     print(s)



# # # # # -------------N letter
# n = 9
# for i in range(n):
#     s="  "
#     for j in range(n):
#         if j == 0 or j == n - 1 or i == j:
#             s += "\033[91mN\033[0m "
#         else:
#             s += "  "
#     print(s)

# print("             ")
# print("             ")


# for e in range(n):
#     s=" "
#     for f in range(n):
#        if e==0 or f==0 or f==n-1 or e==n//2:
#           s+="\033[92mA\033[0m "
#        else:
#           s+=" "+" "
#     print(s)

# print("             ")
# print("             ")

# # # -----------V letter
# n1 = 15
# for j in range(n1 // 2 + 1):  # only top half
#     s = ""
#     for k in range(n1):
#         if (j == k or j == n1 - k - 1):
#             s += "\033[93mV\033[0m"
#         else:
#             s += " "
#     print(s.rstrip())

# print("             ")
# print("             ")

# n1 = 15



# # ------------E letter
# for l in range(n):
#     s=" "
#     for m in range(n):
#         if m==0 or l==0 or l==n-1 or l==n//2:
#            s+="\033[95mE\033[0m "
#         else:
#             s+=" "+" "
#     print(s)

# print("             ")
# print("             ")

# # ------------E letter
# for l in range(n):
#     s=" "
#     for m in range(n):
#         if m==0 or l==0 or l==n-1 or l==n//2:
#            s+="\033[96mE\033[0m "
#         else:
#             s+=" "+" "
#     print(s)

# print("             ")
# print("             ")


# for i in range(n):
#     s="  "
#     for j in range(n):
#         if j == 0 or j == n - 1 or i == j:
#             s += "\033[97mN\033[0m "
#         else:
#             s += "  "
#     print(s)


# # -------sqaure
# n=6
# for a in range(n):
#     s=" "
#     for b in range(n):
#         if a==0 or b==0 or b==n-1 or a==n-1:
#             s+="\033[94mA\033[0m "
#         else:
#             s+=" "+" "
#     print(s)


# # # ------rectacgle
# # for c in range(n):
# #     s=" "
# #     for d in range(n):
# #         if c==0 or d==0 or c==n-1 or d==n-1:
# #             s+="* "+" "
# #         else:
# #             s+=" "+"  "
# #     print(s)

# n=5
# for i in range(n):
#     s=" "
#     for j in range(1,i+1):
#         if j==0 or j==n-1 :
#            s+="*"
#         else:
            

#     print(s)


# def fun(n):
#     if n==0:    #base condition
#         return
#     else:
#         print(n)   
#         fun(n-1)  
# fun(5)
