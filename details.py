# pseudocode:
# ask the user to enter their name
# ask the user to enter their Age
# ask the user to enter their house number
# ask the user to enter their street name
# print concatinate the details into one sentence and print

name = input("Please enter your name: ")
age = input("Please enter your age in years (ONLY ENTER THE NUMBER): ")
house_number = input("""Please enter your house number
                      (ONLY ENTER THE NUMBER): """)
street_name = input("""Please enter your street name
                    (EXCLUDING THE WORD STREET): """)
print(f"""This is {name}. They are {age} years old and lives at house number
      {house_number}  on {street_name} street.""")
