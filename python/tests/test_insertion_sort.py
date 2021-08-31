# from code_challenges.insertion_sort.insertion_sort import insertionSort

def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

    return arr


def test_insertionSort():
    arr = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    actual = insertionSort(arr)
    assert actual == expected

