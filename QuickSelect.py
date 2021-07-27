# QuickSelect

def quick_select(arr,k):
    pivot = arr[((len(arr)+1)//2)-1] # 중간값
    left,mid,right = [],[],[]

    for i in range(len(arr)):
        if arr[i]<pivot:
            left.append(arr[i]) # 피봇보다 작으면 왼쪽
        elif arr[i]>pivot:
            right.append(arr[i]) # 피봇보다 크면 오른쪽
        else:
            mid.append(arr[i]) # 피봇이면 중간

    if k<len(left):
        return quick_select(left,k)
    elif k<len(left)+len(mid):
        return mid[0]
    else:
        return quick_select(right,k-len(left)-len(mid))

arr=[3,5,1,2,9,6,4,7,5]
print(quick_select(arr,4))