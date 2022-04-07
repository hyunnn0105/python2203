
hour, minute = map(int, input().split())

# 분이 45분 이상일 경우 분에서 45를 뺀다
if minute >= 45:
    print(hour, minute-45)

# 분이 44분 이하이면서 시가 1시보다 크다면
# 45분을 제거할 경우 시침이 1시간 줄어들어야 하므로
# 시간은 1을 빼주고 분은 15를 더한다.
elif minute <= 44 and hour >= 1:
    print(hour-1, minute+15)

# 남은 경우의 수는 시간이 0이면서 분이 44분 이하인 
# 경우로 이럴 때는 23시로 돌아가야한다.
else:
    print(23, minute+15)