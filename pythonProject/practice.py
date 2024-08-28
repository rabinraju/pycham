# def check_palindrome(text):
#     if text == text[::-1]:
#         print("It's Palindrome")
#     else:
#         print("Not Palindrome")
#
#
# text = "MALAYAALAM"
# check_palindrome(text)
# num = 12
# if num > 1:
#     for i in range(2, (num//2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://web.whatsapp.com")
# current_url = driver.current_url
# print("the current url is :",current_url)
# driver.quit()
# import pandas as pd
# df = pd.dataframe(mydata)
# filtered_df = df[df['value']]>100

# import pandas as pd
#
# # Assuming 'mydata' is a dictionary or a list of dictionaries that you want to convert to a DataFrame
# mydata = {'value': [50, 150, 200, 80, 120]}  # Example data
#
# df = pd.DataFrame(mydata)
# filtered_df = df[df['value'] > 100]
#
# print(filtered_df)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
nums = [2, 7, 11, 15]
target = 3
print(two_sum(nums, target))
