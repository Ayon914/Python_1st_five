

def remove_duplicates(input_list):
    unique_list = []

    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)

    return unique_list



user_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = remove_duplicates(user_list)


print("List after removing duplicates : ",result)


