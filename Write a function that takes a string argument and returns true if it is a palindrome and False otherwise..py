def pelindrome(string_take):
    if(string_take==string_take[::-1]):
        print("Pelindrome")
    else:
        print("Not Pelindrome")
pelindrome(input("string="))