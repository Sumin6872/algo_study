# 1. 카드 개수 입력 받음
# 2. P 리스트 생성 <- 카드 장수에 따른 카드 금액 입력 받기
# 3. DP 리스트 생성 <- 장 수에 따라 가장 큰 카드 금액을 입력 받기 
# 4. for 문 돌림 <- 카드를 차례대로 더해주려면 필요할 것 같다...
# 5. max 사용 <- 가장 큰 금액을 출력하려면 사용
# 6. 편하게 하기 위해 DP랑 P 리스트의 index 0번째에 0이라는 값 추가
# => 시간 초과가 나길래 인터넷을 참고하니 index 0번째에 0이라는 값 추가했더라....

N = int(input())
P = [0] + list(map(int, input().split()))
DP = [0] * (N+1)

for i in range(1, N+1):
    for j in range(1, i+1):
        DP[i] = max(DP[i], P[j] + DP[i-j])

print(DP[N])
