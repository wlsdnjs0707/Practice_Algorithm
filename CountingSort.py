# 카운팅 정렬 (계수 정렬)
# 데이터 크기를 기준으로 개수를 세서 인덱스에 맞춰 정렬한다.
# 특정한 범위 조건이 있는 경우 매우 빠르다. O(n)

a = [5,5,5,5,5,4,4,4,4,3,3,3,2,2,1]

index = [0]*5

for i in a:
    index[i-1]+=1

for i in range(len(index)):
    for j in range(index[i]):
        print("{0}".format(i+1),end='')