# 퀵 정렬
# 기준 데이터를 설정하고 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
# 병합정렬과 더불어 정렬 라이브러리의 근간이다.

a = [5,7,9,0,3,1,6,2,4,8]

# def quick_sort(array,start,end):
#     if start>=end:  # 원소가 1개인경우
#         return
#     pivot = start
#     left = start+1
#     right = end

#     while left<=right:
#         # 피벗보다 큰 데이터를 찾을때까지
#         while left<=end and array[left]<=array[pivot]:
#             left += 1
#         # 피벗보다 작은 데이터를 찾을때까지
#         while right>start and array[right]>=array[pivot]:
#             right -= 1
#         if left>right: #엇갈렸다면
#             array[right], array[pivot] = array[pivot], array[right]
#         else: #엇갈리지 않았다면
#             array[left], array[right] = array[right], array[left]
#     # 분할 이후 왼쪽과 오른쪽 에서 각각 정렬 수행
#     print(a)
#     quick_sort(array,start,right-1)
#     quick_sort(array,right+1,end)

# quick_sort(a,0,len(a)-1)

# 파이썬의 장점을 살린 방식(리스트인덱싱)

def quick_sort(array):
    if len(array)<=1: # 분할하다가 배열의크기가 1일때
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x<=pivot]
    right = [x for x in tail if x>pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(a))