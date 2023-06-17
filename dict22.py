d={919:"a",212:"b",232:"c",252:"d",525:"e",565:"f",545:"g"}

print(d)
print(d[212])
d[232]="h"
print(d)
for i in d:
    print(i," : ",d[i])
print(545 in d)
#print(d.clear())
#print(d)
print(d.copy())
print(d)
print(d.get(545))
print(d.items())
print(d.keys())
print(d.pop(545))
print(d)
print(d.popitem())
print(d)
d1={212:"z",858:"x",878:"n",686:"f"}
d.update(d1)
print(d)

