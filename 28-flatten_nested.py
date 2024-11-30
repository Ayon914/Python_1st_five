def flatten_nested_list(nested_list):
    flatten_list = []
    for item in nested_list:
        if isinstance(item,list):
            flatten_list.extend(flatten_nested_list(item))
        else:
            flatten_list.append(item)
    return flatten_list

nested_list = [7, [2,3],4,[2,[3,4],5],6,[7,8]]
flattened = flatten_nested_list(nested_list)
print("Flattened list : ",flattened)