# 삽입 정렬
# 처리되지 않은 데이터를 적절한 위치에 삽입한다.

a = [5,4,3,2,1]

for i in range(1,len(a)):
    for j in range(i,0,-1):
        if a[j]<a[j-1]:
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp
        else:
            break
        print(a)