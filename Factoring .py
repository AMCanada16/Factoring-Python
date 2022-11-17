print("Factoring starting")
x = input()
z = []
try:
    y = int(x)
except:
    print("needs to be an integer")
for i in range(1,y):
    var1 = y % i
    if var1 == 0:
        z.append(i)
    print(f"{y} for {i}  {var1}")
print(f"List of factors{z}")