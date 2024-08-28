def check_palindrome(text):
    if text == text[::-1]: #start:stop:step
        print("its palindrome")
    else:
        print("its not palindrome")


text = "MALAYALAM"
check_palindrome(text)