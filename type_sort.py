def bubble_sort(lists):
    size_list = len(lists)
    swaps = 0
    comparisons = 0
    for a in range(size_list):
        for b in range(0, size_list-a-1):
            comparisons += 1
            if lists[b] > lists[b+1]:
                lists[b], lists[b+1] = lists[b+1], lists[b]
                swaps += 1
    print("Lista posortowana metodą bąbelkową\n"
        f"Liczba porównań: {comparisons}\n"
        f"Liczba zamian: {swaps}")
    return lists

def place_sort(lists):
    compariso = 0
    swap = 0
    size = len(lists)
    for a in range(1, size):
        key = lists[a]
        b = a - 1
        while(b >= 0 and lists[b] > key):
            lists[b+1] = lists[b]
            b -= 1
        compariso += 1
        lists[b + 1] = key
        swap += 1
    print("Lista posortowana metodą przez wstawianie\n"
          f"Liczba porównań: {compariso}\n"
          f"LIczba zamian: {swap}")
    return lists

def selection_sort(lists):
    compa = 0
    swa = 0
    size = len(lists)
    for a in range(size):
        min_a = a
        for b in range(a+1, size):
            if lists[b] < lists[min_a]:
                min_a = b
            compa += 1
        lists[a], lists[min_a] = lists[min_a], lists[a]
        swa += 1
    print("Lista posortowana metodą przez wstawianie\n"
          f"Liczba porównań: {compa}\n"
          f"LIczba zamian: {swa}")
    return lists

list_to_sort = [4, 2, 3, 1, 6, 5, 9, 7, 8, 0]
print(f"Lista do sortowania: {list_to_sort}\n")

print(f"{bubble_sort(list_to_sort)}\n")

print(f"{place_sort(list_to_sort)}\n")

print(f"{selection_sort(list_to_sort)}\n")