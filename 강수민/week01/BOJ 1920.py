# n을 정수로 받음
n = int(input())
# n개의 정수를 리스트로 받음 (시간 초과 떠서 list -> set으로 바꿈)
nlist = set(map(int, input().split()))

# 중간중간 확인 위함
print(nlist)

# m을 정수로 받음
m = int(input())
# m개의 정수를 리스트로 받음
mlist = list(map(int, input().split()))

print(mlist)

# M개의 수가 nlist안에 존재하면 1을, 존재하지 않으면 0을 출력
for i in mlist:
    if i in nlist:
        print(1)
    else:
        print(0)
            
