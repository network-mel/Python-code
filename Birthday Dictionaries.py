# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
birthday_dict = {'Albert Einstein' : "14/03/1879", "Benjamin Franklin" : "01/17/1706", "Ada Lovelace" : "10/12/1815"}

print(">>> Welcome to the birthday dictionary. We know the birthdays of:")
for person in birthday_dict:
    print(person)
print(">>> Who's birthday do you want to look up?")
requested_name = input()
if requested_name in birthday_dict:
    print(f">>> {requested_name}'s birthday is {birthday_dict[requested_name]}")
else:
    print(f"Sorry, we don't have birthday of {requested_name}")
