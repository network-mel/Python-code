# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
string = input("Input palindrome: ")
string2 = string[::-1]
if string == string2:
    print("YES")
else:
    print("NO")