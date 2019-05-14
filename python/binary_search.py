def binary_search(a, x, low = 0, high = None):
    if high is None:
        high = len(a)
    while low < high:
        middle = (low + high)//2
        middle_value = a[middle]
        if middle_value < x:
            low = middle + 1
        elif middle_value > x: 
            high = middle
        else:
            return middle
    return -1

# 이진탐색

# 이진 탐색은 순서대로 찾는 것이 아니라, 중간부터 찾아 나서는 방법입니다.
# 만약 아래와 같은 배열에서 7을 찾아야 한다면, 

# 첫 번째로 중간 위치의 요소를 비교하고(7<14)
# 찾아야할 값보다 크면 왼쪽의 중간에서 다시 비교합니다.

# 다시 한 번 크기를 비교해서 오른쪽의 중간으로 갈지, 
# 왼쪽의 중간으로 갈지 결정하여 다시 찾아나서는 것을 이진 탐색법이라고 합니다.