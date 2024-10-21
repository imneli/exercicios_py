def find_min(arr):
    min_i = 0
    min = arr[min_i]
    for i in range(len(arr)):
        if arr[i] < min:
            min_i = i
            min = arr[i]
    return min_i

ordered = []

def selection_sort(arr):
    while arr:
        min_i = find_min(arr)
        el = arr.pop(min_i)
        ordered.append(el)
    return ordered

def better_selection_sort(arr):
    for i in range(len(arr)):
        min_i = find_min(arr[i:]) + i
        aux = arr[i]
        arr[i] = arr[min_i]
        arr[min_i] = aux
    return

def bubble_sort(arr):
    for i in range(len(arr)):
        changes = 0
        for j in range(len(arr) -1 -i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                changes += 1
                print(f"changes \n->{changes}")
        if changes == 0:
            print("Não teve mudanças")
            return

def find_src(num):
    init = 0
    end = num
    while end - init > 0.001:
        attempt = (init + end) / 2
        if attempt**2 > 25**2:
            end = attempt
        else:
            init = attempt
    return attempt

def verify_num_recursive(msg):
    num = input(msg)
    if not num.isnumeric():
        num = verify_num_recursive(msg)
    return int(num)

arr = [4, 3, 9, 1, 8, 2]
bubble_sort(arr)

print(f"The ordered arr is: \n-> {arr}")
