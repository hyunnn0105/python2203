
A = int(input())
B = int(input())

C = A * (B // 10 ** 0 % 10)
print(C)

D = A * (B // 10 ** 1 % 10)
print(D)

E = A * (B // 10 ** 2 % 10)
print(E)

F = (C * 10 ** 0) + (D * 10 ** 1) + (E * 10 ** 2)
print(F)