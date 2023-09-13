def sort_list(input_list):
    print(input_list)
    for i in range(len(input_list)):
        for j in range(len(input_list) - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                #Fix on the previous line. The item 'input_list[j]' was being swapped by itself again, meaning no changes. Changed for [j + 1]
    print(input_list)
    return input_list

#List to be used for testing the sorting method.
test_list = [4, 2, 9, 1, 5, 3, 98, 3, 1, 0]


sort_list(test_list)
