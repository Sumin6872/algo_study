# 1. 문제가 이해가 되지 않아 먼저 -1을 출력하는 경우(제대로 된 녹음이 아닌 경우)부터 정리
# - 문자열을 모두 방문 X
# - 오리가 0마리
# - 문자열의 길이 % 5 != 0일 때
# 2. quack하고 quack해야 한 마리 (quaquackck하면 2마리) - 한 사이클이 끝나는 거에 중점


duck = input()
countlist = [False] * len(duck)
quack = ['q', 'u', 'a', 'c', 'k']

count = 0
# quack index를 저장하는 변수
idx = 0

# 제대로 된 녹음이 안 된 경우 먼저 거름 (5의 배수 아닐 때)
if len(duck) % 5 != 0:
    print(-1)
    
else :
    for i in range(len(duck)):
        # 조건 충족하면 q 시작 (countlist에 가지 x, q임)
        if duck[i] == 'q' and not countlist[i]:
            first = True
            for j in range(len(duck)):
                if quack[idx] == duck[j] and not countlist[j]:
                    countlist[j] = True
                    if duck[j] == 'k':
                        if first:
                            count += 1
                            # 한 사이클 끝나고 초기화
                            first = False 
                        # 한 사이클 끝나고 초기화
                        idx = 0
                        continue
                    idx += 1

if count == 0 or not all(countlist):
    print(-1)
else:
    print(count)
