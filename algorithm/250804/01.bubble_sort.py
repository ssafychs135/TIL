# 정방향
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 역방향
def bubble_sort_invert(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr), i, -1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)


numbers = [64, 13, 9, 62, 3]
inverted_sorted_numbers = bubble_sort_invert(numbers)
print("정렬 후:", inverted_sorted_numbers)