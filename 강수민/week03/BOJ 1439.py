# 먼저 전체를 뒤집는 거 안 하고 n번째 자리와 (n + 1)번쨰 자리의 수가 서로 다른 횟수를 구함
# 0001100 -> 서로 다른 횟수 : 2 -> 최소 횟수 : 1
# 0000001 -> 1 -> 1
# 11001100110011000001 -> 8 -> 4
# 11101101 -> 4 -> 2
# 규칙 -> 값을 +1하고 나서 2를 나눈 몫이다. (1 -> 1이 있기 때문)

s = input()
count = 0

for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        count += 1

print((count + 1) // 2)
