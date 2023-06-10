def common_elements(list1, list2):
    i = j = 0
    common = []

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            common.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    
    return common

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8, 10]
print(common_elements(list1, list2))