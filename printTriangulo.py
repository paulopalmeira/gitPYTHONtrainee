x = float(input())
y = float(input())
z = float(input())
if x == y and y == z:
    print("Triângulo equilátero")
else:
    if x != y and y != z:
        print("Triãngulo escaleno")
    else:
        print("Triângulo isósceles")
