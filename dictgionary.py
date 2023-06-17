d={901:"aarav",877:"hitesh",565:"vishal",233:"vihar",544:"gaurang"}

print(d)
print(d[565])
d[233]="parasar"
print(d)
for i in d:
    print(i," : ",d[i])
print(544 in d)
print(d.get(901))
print(d.items())
print(d.keys())
print(d.pop(544))
print(d)
print(d.popitem())
print(d)
d1={877:"dolly",323:"mahek",454:"jaya"}
d.update(d1)
print(d)
