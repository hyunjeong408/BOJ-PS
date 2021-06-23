list1 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

selection_list = list1[:]
insertion_list = list1[:]
quick_list = list1[:]
count_list = list1[:]
#selection sort
for i in range(len(selection_list)):
    min_idx = i
    for j in range(i+1, len(selection_list)):
        if selection_list[min_idx] > selection_list[j]:
            min_idx = j
    selection_list[i], selection_list[min_idx] = selection_list[min_idx], selection_list[i]

print(selection_list)

#insertion_sort
for i in range(1, len(insertion_list)):
    for j in range(i, 0, -1):
        if insertion_list[j] < insertion_list[j-1]:
            insertion_list[j], insertion_list[j-1] = insertion_list[j-1], insertion_list[j]
        else:
            break
print(insertion_list)

#quick_sort
def quick_sort(arr):
    if len(arr)<=1 :
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x<=pivot]
    right = [x for x in tail if x>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)

print(quick_sort(quick_list))

#count_sort
count_list.append(9)
count_list.append(7)
count_arr = [0]*(max(count_list)+1)

for i in range(len(count_list)):
    count_arr[count_list[i]] += 1

for i in range(len(count_arr)):
    for j in range(count_arr[i]):
        print(i, end=' ')