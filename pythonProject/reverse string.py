def reversestring(string):
    return string[::-1]


string = "RABINRAJU"
reversed_string = reversestring(string)
print(reversed_string)

# reverse in list
mylist = [10,20,30,40,50]
print("mylist before reverse :",mylist)
mylist2 = mylist[::-1]
print("mylist after reverse :",mylist2)

#another way to reverse
rev_str = "RABIN RAJU"
print(rev_str[::-1])