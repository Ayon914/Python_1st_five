My_Dict = { 'name': 'Ayon', 'age': '22'}
key_to_Check = input("enter the key you want to check: ")

if key_to_Check in My_Dict:
    print(f"The key '{key_to_Check}' Exists in the dictionary.")
else:
    print(f"The key '{key_to_Check}' does not exists in the dictionary.")