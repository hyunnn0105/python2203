

T = True
F = False

print(T and T)
print(T and F)
print(F and T)
print(F and F)

print('=====================')

print(T or T)
print(T or F)
print(F or T)
print(F or F)

print('=======================')

a = 5

if (a > 1) and (a < 10):
    print('a는 1과 10 사이의 정수입니다!')
else:
    print('a는 범위 안의 정수가 아닙니다.')


print('=====================')

b = 4
if (b == 2) or (b == 4):
    print('b는 2 또는 4입니다.')
else:
    print('b는 2 또는 4가 아닙니다.')