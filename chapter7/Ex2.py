l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l :
    if(name.startswith('S')):
        print("Hello" , name)
        

i = 0
while i < len(l):
    if l[i].startswith("S"):
        print("Hello", l[i])
    i += 1

