# Insertion Sort
    Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

# Pseudocode
    InsertionSort(int[] arr)

        FOR i = 1 to arr.length

        int j <-- i - 1
        int temp <-- arr[i]

        WHILE j >= 0 AND temp < arr[j]
            arr[j + 1] <-- arr[j]
            j <-- j - 1

        arr[j + 1] <-- temp

# Trace
### pass 1
![image](assets/in1.PNG)

### pass 2
![image](assets/n2.PNG)

### pass 3
![image](assets/n3.PNG)

### pass 4
![image](assets/n4.PNG)

### pass 5
![image](assets/n5.PNG)


# Efficency
    Time: O(1)
    Space: O(1)
