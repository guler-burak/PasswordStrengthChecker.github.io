special_characters = ["@", "$", "!", "*", "+", "&", "%"]
password = input("Enter Password: ")

if len(password) < 8:
    print("Password must be at least 8 characters long.")
    
if len(password) > 16:
    print("Password length must not exceed 16 characters.")
    
if not any(char.isnumeric() for char in password):
    print("Password must contain at least one digit.")
    
if not any(char.isalpha() for char in password):
    print("Password must contain letters.")
    
if not any(char in special_characters for char in password):
    print("Password must contain special characters.")
    
else:
    print("Password has been created.")