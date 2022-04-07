kor = int(input('국어: '))
eng = int(input('영어: '))
math = int(input('수학: '))

# 총점 계산
tot = kor + eng + math
# 평균 계산 (2자리까지 반올림)
avg = round(tot / 3, 2)

print(f'당신의 평균점수: {avg}점')
if avg >= 60:
    print('이번 시험에 통과하셨습니다.')
else :
    print('재수강 대상자입니다.')     
print('열공하세요!')















