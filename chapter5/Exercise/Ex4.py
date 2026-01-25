favLan = {}

for i in range(4):
    name = input(f"Enter the name of friend {i+1}: ")
    language= input(f"Enter {name}'s favourite language: ")
    favLan[name] = language
    
print("\nFavourite language of friends : ")
print(favLan)