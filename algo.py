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

def find_src_recursive(init, end, num):
    attempt = (init + end) / 2
    if end - init > 0.001:
        if attempt**2 > 25**2:
            end = attempt
        else:
            init = attempt
        attempt = find_src_recursive(init,end,num)
    return attempt


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[0]
    min = [elem for elem in arr if elem < pivo]
    max = [elem for elem in arr if elem > pivo]

    min = quick_sort(min)
    max = quick_sort(max)

    ordered = min + [pivo] + max
    return ordered

def binary_search(arr, target):
    init = arr[0]
    end = arr[len(arr) -1]

    attempt = (init + end ) // 2

    if arr[attempt] == target:
        return print(f"your index is {attempt}")
    else:
        if arr[attempt] > target:
            end = arr[attempt -1:]
        else:
            init = arr[attempt +1:]
    return attempt

arr = [4, 3, 9, 1, 8, 2, 5]
print(binary_search([1,2,3,4,5], 5))
print(f"The ordered arr is: \n-> {arr}")
