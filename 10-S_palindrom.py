"""
def is_palindrome(s):

    s = s.replace(" ", "").lower()

    return s == s[::-1]


Given = input("Enter a string = ")

if is_palindrome(Given):
    print(f"{Given} is a Palindrome")

else:
    print(f"{Given} is not a Palindrome")





###N_palindrome
    """


def is_palindrome(s):
    s = str(s)

    return s == s[::-1]


Given = input("Enter a valid number = ")

if is_palindrome(Given):
    print(f"{Given} is a Palindrome")

else:
    print(f"{Given} is not a Palindrome")
