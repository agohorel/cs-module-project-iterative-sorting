def selection_sort(arr):
    for i in range(len(arr)):
        lowest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j
        arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

# STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):
#     counts = [0 for x in range(maximum+1)]
#     result = [0 for x in range(maximum+1)]

    
#     for x in arr:
#         counts[x] += 1
#     print(counts)

#     for x in range(len(counts)):
#         counts[x] += counts[x-1]
#     print(counts)

# arr = [1,4,1,2,7,5,2]
# count_sort(arr, len(arr))