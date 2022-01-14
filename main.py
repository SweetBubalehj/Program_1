import math
# Number 1
while True:
    print("Enter a: ")
    a = int(input())
    print("Enter b: ")
    b = int(input())
    print("Enter c: ")
    c = int(input())
    if a != 0 and b != 0 and c != 0:
        break

print("ax^2+bx+c=0")
print("%ix^2+%ix+%i=0" % (a, b, c))
d = b*b - 4*a*c
print("Delta =", d)

if d > 0:
    x1 = (-b + math.sqrt(d))/(a*a)
    x2 = (-b - math.sqrt(d))/(a*a)
    print("X1 =", x1, " X2 =", x2, "\n")
elif d == 0:
    x = -b/(a*a)
    print("X =", x, "\n")
else:
    print("ERROR, Delta < 0!\n")


# Number 2
for i in range(2, 9, 3):
    for j in range(2, 10):
        print(i, "*", j, "=", i*j, "  ", i+1, "*", j, "=", (i+1)*j, "  ", i+2, "*", j, "=", (i+2)*j)
    print('\n')

