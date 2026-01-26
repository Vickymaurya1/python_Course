def convertor():
    c = float(input("Enter the temp in Celsius : "))
    f1 = c*(9/5)
    f2 = f1 + 32
    return f2

f = convertor()
print(f)
