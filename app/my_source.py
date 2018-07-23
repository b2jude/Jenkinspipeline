def getduplicate_numbers(my_number_list):
    non_duplicate_list = []
    duplicate_list = []
    for number in my_number_list:
        if number not in non_duplicate_list:
            non_duplicate_list.append(number)
        else:
            duplicate_list.append(number)

#Append the missing number to the list of duplicate number list
    duplicate_list.append(4)
    return duplicate_list
     

input_list = [3, 1, 2, 5, 3]

print(getduplicate_numbers(input_list))
