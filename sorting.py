def find_min(arr):
    min_i = 0
    min = arr[min_i]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_i = i
    return min_i

def selection_sort(arr):
    while arr:
        min_i = find_min(arr)
        el = arr.pop(min_i)
        order_arr.append(el)
    return order_arr

arr = [9,1,8,10,4,5,3,6,2,7]
print(arr[2:])
order_arr = []


print(ordenada)

def selection_sort_ruim(arr):
    for i in range(len(arr)):
        min_i = find_min(arr[i:]) + i
        aux = arr[i]
        arr[i] = arr[min_i]
        arr[min_i] = aux
    return

def bubble_sort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            aux = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = aux


