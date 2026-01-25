a ={
    "key" : "value",
    "harry" : "code", 
    "marks" : "100" , 
    "list" : [1,2,0],
    "from" : "india"
}
# print(a["key"])

# print(a["list"])
# print(a["marks"])
# print(a["harry"])

# print(a , type(a))

# print(a.items())
# print(a.keys())
# print(a.values())

# a.update({"marks" : "99"})
# print(a.values())

print(a.get("harry")) #but is this same as print(a["harry"])
#ANS yes but if we enter invalid key than get method show none
# but normal method show error





