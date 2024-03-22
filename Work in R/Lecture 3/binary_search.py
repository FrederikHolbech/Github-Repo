# modified binary_search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def common_values(arr1,arr2):
    values_list = []
    for i in arr1:
        if i in arr2:
            values_list.append(i)
    return values_list

print(common_values([8],[11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,24,24,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,10,1,67,68,69,6,67,8898758,7685578678,678586785,6786785678,67857865,87685688,657858678,678586785,8678586,87685,685,8678,58,5678,6785,88,6578,8,6578,5678,578,6578,78,568,78,8567,867,85,8678,5678,58,678,58,7856,8]))

