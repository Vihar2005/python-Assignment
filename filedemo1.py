file=open("tops1.txt","w")
file.write("this is file input//output demo using python.")
file.close()
print("file written successfully")

print('*'*50)

file=open("tops1.txt",'r')
print(file.read())
file.close()

print('*'*50)

file=open('tops1.txt','a')
file.write("\nNow This file is appended.")
file.close()

print('*'*50)

file=open("tops1.txt",'r')
print(file.read())
file.close()

print('*'*50)

file=open("tops2.txt","w+")
file.write("this is read/write operation using w+ mode.")
print("current file position : ",file.tell())
file.seek(20)
print(file.read())
file.close()

print('*'*50)
