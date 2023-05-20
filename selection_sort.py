def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # swap the minimum element with the current element
        array[i], array[min_index] = array[min_index], array[i]

    return array


array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("The original array is:", array)

sorted_array = selection_sort(array)

print("The sorted array is:", sorted_array)
