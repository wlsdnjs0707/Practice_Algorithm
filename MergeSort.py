# 병합 정렬
# 반씩 쪼개서 분할 정복

a = [10,9,8,7,6,5,4,3,2,1]

def merge_sort(arr):

    def sort(low,high):
        if high-low<2:     # 배열의 길이가 1일때
            return
        
        mid = (low+high)//2   # 중간값
        sort(low,mid)         # 왼쪽 배열
        sort(mid,high)        # 오른쪽 배열
        merge(low,mid,high)   # 배열 합치기

    def merge(low,mid,high):
        temp=[]
        l = low
        h = mid

        while l<mid and h<high:  # 배열의 모든값
            if arr[l]<arr[h]:    # 배열에 작은값 넣기
                temp.append(arr[l])
                l+=1
            else:
                temp.append(arr[h])
                h+=1

        while l<mid:
            temp.append(arr[l])
            l+=1
        
        while h<high:
            temp.append(arr[h])
            h+=1

        for i in range(low,high):
            arr[i]=temp[i-low]

        print(arr)

    return sort(0,len(arr))

merge_sort(a)

print(a)