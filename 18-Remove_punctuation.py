import string
def remove_punctuatuions(s):
    translator = s.maketrans('','',string.punctuation)
    return s.translate(translator)

user_input = input("Enter a string: ")
cleaned_string = remove_punctuatuions(user_input)

print(f"String without punctuation: {cleaned_string}")