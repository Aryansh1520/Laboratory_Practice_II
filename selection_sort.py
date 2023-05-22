def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # swap the minimum element with the current element
        array[i], array[min_index] = array[min_index], array[i]

    return array


array = list(map(int,input("Enter Numbers seperated by space").split()))

print("The original array is:", array)

sorted_array = selection_sort(array)

print("The sorted array is:", sorted_array)
