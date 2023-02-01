num = list(map(int, input()))
numlen = len(num) / 2
numlen = int(numlen)
rightnumsum = 0
leftnumsum = 0

for i in range(numlen):
    rightnumsum += num[i + numlen]
    leftnumsum += num[i]
    
if rightnumsum == leftnumsum:
    print("LUCKY")
else:
    print("READY")
