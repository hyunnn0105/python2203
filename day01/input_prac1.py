
# 상품의 이름
product_name = input('상품명을 입력하세요: ') 
# 상품의 가격
price = int(input('원가를 입력하세요: '))

# 할인가격
discount = int(price - price * 0.1)

# 메세지 출력
print(f'{product_name}의 할인가격은 {discount}원입니다.')