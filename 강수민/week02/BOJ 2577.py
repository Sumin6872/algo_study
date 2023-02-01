# 1. 먼저 각각 저장할 변수 생성
# 2. 수가 반복한 횟수가 들어갈 리스트 생성
# 3. a, b, c를 곱한 값을 넣을 변수 생성
# 4. 각 수에 맞는 리스트의 인덱스의 값을 변경 (+1)

# 입력값을 숫자로 변환해 a, b, c에 각각 저장
a = int(input())
b = int(input())
c = int(input())

# 리스트 생성
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# a, b, c의 값을 곱할 변수 생성
mul = list(str(a * b * c))

# 리스트의 i 값과 같은 인덱스의 값에 +1
for i in mul:
    num[int(i)] += 1

# 답 출력    
for i in num:
    print(i)
