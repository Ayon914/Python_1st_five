def check_empty_list(my_list):
    if not my_list:
        return ("This List is Empty")
    else:
        return "This list is not Empty"


list1 = []
print(check_empty_list(list1))

list2 = [1,2,3]
print(check_empty_list(list2))