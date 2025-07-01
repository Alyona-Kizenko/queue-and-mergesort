import time
import random
from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  
            break
    return arr

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def compare_sorting_algorithms():
    sizes = [10, 100, 1000, 10000]  
    
    print(f"{'Размер':<10} | {'MergeSort':<15} | {'BubbleSort':<15} | Ускорение")
    print("-" * 60)
    
    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]

        start = time.perf_counter()
        merge_sort(data.copy())
        merge_time = time.perf_counter() - start

        start = time.perf_counter()
        bubble_sort(data.copy())
        bubble_time = time.perf_counter() - start
        
        speedup = bubble_time / merge_time if merge_time != 0 else 0
        
        print(f"{size:<10} | {merge_time:.6f} сек | {bubble_time:.6f} сек | {speedup:.1f}x")

if __name__ == "__main__":
    compare_sorting_algorithms()