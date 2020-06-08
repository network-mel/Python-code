# https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
import json


if __name__ == "__main__":
    with open("birthdays.json", "r+") as f:
        birthday_dict = json.load(f)
        print(">>> Welcome to the birthday dictionary. We know the birthdays of:")
        for person in birthday_dict:
            print(person)
        print(">>> Who's birthday do you want to look up?")
        requested_name = input()
        if requested_name in birthday_dict:
            print(f">>> {requested_name}'s birthday is {birthday_dict[requested_name]}")
        else:
            print(f"Sorry, we don't have birthday of {requested_name}")
    choice = input("Do you want to add a new birthday? (YES\\NO): ")
    if choice == "YES" or choice == "y":
        with open("birthdays.json", "w") as f:
            new_name = input("Please input a person's name: ")
            new_birthday = input("please input a birthday: ")
            birthday_dict[new_name] = new_birthday
            json.dump(birthday_dict, f, indent=4, sort_keys=True)
            print("Birthday added!")
