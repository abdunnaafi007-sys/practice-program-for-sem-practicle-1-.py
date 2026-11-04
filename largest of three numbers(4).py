a = int(input("Enter a no:"))
b = int(input("Enter a no:"))
c = int(input("Enter a no:"))
if (a > b) & (a > c):
    print(a, "is largest")
elif (b > a) & (b > c):
    print(b, "is largest")
else:
    print(c, "is largest")
