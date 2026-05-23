def palindrome(n):
    original = str(n)
    reverse = original[::-1]

    if reverse == original:
        print("The provided string is a Palindrome")
    else :
        print("The provided string is not a Palindrome")

string = input("Enter the string: ")

palindrome(string)
        

