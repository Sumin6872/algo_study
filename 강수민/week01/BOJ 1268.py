# 입력값을 숫자로 변환해 n에 저장
n = int(input())
# 리스트에 0을 n 갯수만큼 저장 (비교하여 값을 넣기 위함)
issame = [0] * n
# 학생 정보 저장
stulist = []
# 가장 많은 학생들과 같은 반이 된 학생 출력하기 위한 리스트
nummax = []

# 학생 정보 저장 (정수로 변환하여 저장)
for i in range(n):
    stulist.append(list(map(int, input().split())))
    issame[i] = [0] * n

# i학년의 j와 k가 같음을 확인하기 위한 반복문 
for i in range(5):
    for j in range(n):
        for k in range(j + 1, n):
            if stulist[j][i] == stulist[k][i]:
                # 같으면 같은 반인 친구 위치에 1 저장
                issame[k][j] = 1
                issame[j][k] = 1

# 각각 같은 반이었던 학생 명수 저장
for l in issame:
    nummax.append(l.count(1))

# 가장 많은 학생과 같은 반이 된 학생 출력
print(nummax.index(max(nummax)) + 1)
