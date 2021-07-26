# 그리디 알고리즘
# 현재 상황에서 가장 좋은 값만 선택
# 최적의 해를 보장하는지 꼭 확인해야 한다.

# 거스름돈
n = int(input())
count=0

coin = [500,100,50,10]

for i in coin:
    count = count + n//i
    n = n%i

print(count)