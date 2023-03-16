# 1. 삼각형의 크기 입력 받음 -> 이걸 변수로 받는다
# 2. 각각 층의 수들을 입력 받음 -> 이걸 리스트로 받는다
# 3. 각 수들을 기억할 dp 생성 -> 이것도 리스트
# 4. 밑에서 위로 올라간다 -> 위에서 밑은 어려웡....
# 5. 밑에서 위로 올라갈 때 겹치는 부분은 가장 큰 수로 입력 받는다
# ex) 5 -> 7을 가고 2 -> 7을 가기 떄문에 가장 큰 합인 12로 입력받는다.
# 6. 계속 위로 올라가고 나서 가장 위에 있는 수를 출력한다. -> 다 더한 것이니깐

# 정수 삼각형 크기 입력
n = int(input())  

# 각 층마다 삼각형 값 입력받을 리스트
triangle = [] 

# 값을 층마다 입력시킴
for i in range(n):
    row = list(map(int, input().split()))
    triangle.append(row)

# 이건 서림 언니한테 배운 리스트 생성 (for문 사용함)
dp = [[0 for _ in range(n)] for _ in range(n)]  

# 마지막 층 수부터 올라가기 위해 dp 안에 넣어주기
for i in range(n):
    dp[n-1][i] = triangle[n-1][i]

# 밑 -> 위, 겹치는 부분은 가장 큰 수로 입력
for i in range(n-2, -1, -1):
    for j in range(i+1):
        dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])

# 가장 위의 값 출력 (다 더한 것이니깐)
print(dp[0][0])
