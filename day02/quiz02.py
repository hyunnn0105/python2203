
print('2개의 정수값을 입력하세요.')
x = int(input('정수 x: '))
y = int(input('정수 y: '))

# 평균의 반전값
reverse = int(-((x + y) / 2))

print(f'평균값의 부호를 반전한 값은 {reverse}입니다.')