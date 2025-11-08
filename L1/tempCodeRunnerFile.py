for i in range (1,100):
 if i>1:
    for j in range(2,i):
        if i%j==0:
            print(i,"not prime")
            break
    else:
        print(i,"prime")
else:
    print("not prime")