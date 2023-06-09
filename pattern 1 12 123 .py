'''
  1
 1 2
1 2 3
'''
for i in range(1,10):
    print(" "*(9-i),end="")
    for j in range(1,i):
        print(" "+str(j),end="")
    print()
