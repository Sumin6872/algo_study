# 1. n만큼 for문이 돌아가게 하기
# 2. 번호, 위치 변수 정의하기
# 3. list를 생성해 안에 입력한 번호의 위치 유무 확인
# 4. 없으면 입력한 번호를 list의 index로 해서 list에 위치 삽입
# 5. 있는데 위치가 다르면 count해서 총 이동한 횟수 구하기

n = int(input())
cowlist = [2] * 11
count = 0

for _ in range(n):
    num, loc = map(int, input().split(' '))
    
    if cowlist[num] == 2:
        cowlist[num] = loc
        
    else:
        if cowlist[num] != loc:
            count += 1
            cowlist[num] = loc
                
print(count)
