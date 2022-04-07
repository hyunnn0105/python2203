

n1 = 10
n2 = '34'

print(n1 + int(n2))
print(str(n1) + n2)


# 문자열 내부값이 순수한 정수가 아닌 경우 변환불가
s1 = 'hello'
# print(int(s1))

s2 = '3.14'
print(float(s2))

f1 = 5.7
print(int(f1))

# 반올림 round()
print(round(f1))

f2 = 3.14159265
print(round(f2, 2))