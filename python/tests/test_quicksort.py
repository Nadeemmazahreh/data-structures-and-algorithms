
def QuickSort(arr, left, right):
    if left < right:

        position = Partition(arr, left, right)

        QuickSort(arr, left, position - 1)

        QuickSort(arr, position + 1, right)

    return arr
def Partition(arr, left, right):

    pivot = arr[right]
    low = left - 1

    for i  in range(left,right):

        if arr[i] <= pivot :

            low += 1
            Swap(arr, i, low)

    Swap(arr, right, low + 1)

    return low + 1
def Swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
## importing the functions is not working

def test_random_sorted():
    arr=[8,4,23,42,16,15]
    QuickSort(arr,0,len(arr)-1)
    assert arr[0]==4
    assert arr[1]==8
    assert arr[-1]==42

def test_Reverse_sorted():
    arr=[20,18,12,8,5,-2]
    QuickSort(arr,0,len(arr)-1)
    assert arr[0]==-2
    assert arr[1]==5
    assert arr[-1]==20

def test_Few_uniques():
    arr=[5,12,7,5,5,7]
    QuickSort(arr,0,len(arr)-1)
    assert arr[0]==5
    assert arr[1]==5
    assert arr[-1]==12


