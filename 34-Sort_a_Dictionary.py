my_dict = {
    'apple': 3,
    'banana': 1,
    'cherry': 2,
    'date': 5,
    'elderberry': 4
}
sorted_dictionary = dict(sorted(my_dict.items(),key=lambda item: item[1]))

print("Dictionary sorted by values: ",sorted_dictionary)