class PalindromeChecker:
    def __init__(self, input_str):
        self.input_str = input_str

    def is_palindrome(self):
        clean_str = ''.join(self.input_str.split()).lower()
        
        return clean_str == clean_str[::-1]
user_input = input("Enter a string to check if it's a palindrome: ")
palindrome_checker = PalindromeChecker(user_input)
if palindrome_checker.is_palindrome():
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
