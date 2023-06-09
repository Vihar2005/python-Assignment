s=input("enter string : ")

alpha=0
digit=0
space=0
upper=0
lower=0

for i in s:
    if i.isalpha:
        alpha+=1
    elif i.isnumeric():
        digit+=1
    elif i.isspace():
        space+=1
    if i.isupper():
       upper+=1
    elif i.islower():
        lower+=1


print("total alphabets : ",alpha)
print("total isnumeric : ",digit)
print("total space : ",space)
print("total upper case : ",upper)
print("total lower case : ",lower)
