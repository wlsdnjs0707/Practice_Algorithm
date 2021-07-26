# 선택 정렬
# 가장 작은데이터를 선택해 맨 앞의 데이터와 바꿈

a = [10,9,8,7,6,5,4,3,2,1]

min_index = 0

for i in range(len(a)):
    min_index = i
    for j in range(i+1,len(a)):
        if a[min_index]>a[j]:
            min_index=j
    
    temp = a[i]
    a[i] = a[min_index]
    a[min_index] = temp

    print(a)