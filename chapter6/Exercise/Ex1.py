numbers = []
for i in range(4):
    number = int(input(f"enter the number{i+1} : ")) 
    numbers.append(number)

ans = -1
for i in range(len(numbers)):
    if(numbers[i] > ans):
        ans = numbers[i]
    else:
        continue
print("Greates number is " , ans)