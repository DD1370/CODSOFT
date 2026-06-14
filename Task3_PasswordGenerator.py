import string
import random

def generate_password(min_length,numbers=True,special_char=True):
    if min_length<1:
        print("\nError:Invalid length for a password!\n")
        return
    req_len=1
    if numbers:
        req_len+=1
    if special_char:
        req_len+=1
    if min_length<req_len:
        options=[]
        if numbers:
            options.append("numbers")
        if special_char:
            options.append("special characters")
        joined_options=" and ".join(options)
        print(f"\nError:The minimum length of the password should be atleast {req_len} to have {joined_options}!\n")
        return
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters=letters

    if numbers:
        characters+=digits
    
    if special_char:
        characters+=special
    
    pwd=""
    meets_criteria=False
    has_numbers=False
    has_special=False

    while not meets_criteria or len(pwd)<min_length:
        new_char= random.choice(characters)
        pwd+=new_char

        if new_char in digits:
            has_numbers=True
        if new_char in special:
            has_special=True
        
        meets_criteria=True
        if numbers:
            meets_criteria= meets_criteria and has_numbers
        if special_char:
            meets_criteria= meets_criteria and has_special
    return pwd
while True:
    try:
        min_length=int(input("Enter minimum length for the password: "))
        break
    except ValueError:
        print("Invalid input! Please enter a whole number (e.g., 8, 12).")

numbers= input("Should the password contain numbers?(y/n): ").lower() =="y"
special_char=input("Should the password contain special charaters?(y/n): ").lower() =="y"
password=generate_password(min_length,numbers,special_char)
if password is not None:
    print(f"\nGenerated password:{password}")

            
