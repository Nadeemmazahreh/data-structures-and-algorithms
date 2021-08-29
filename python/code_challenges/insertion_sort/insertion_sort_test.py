from insertion_sort import insertionSort

def test_insertionSort():
    arr = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    actual = insertionSort(arr)
    assert actual == expected


