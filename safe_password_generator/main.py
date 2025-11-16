# Challenge: 

# Pedro is developing a registration system and needs to generate secure passwords for users. He wants a program that creates random passwords with uppercase letters, lowercase letters, numbers, and special characters.

# Create a program that generates a random 12-character password containing at least one uppercase letter, one lowercase letter, one number, and one special character. Display the generated password.

# Expected output:

# Generated password: A1b@C3d$E5f&


# import pyperclip

from safe_password_generator import pass_generator as pg

pg.initial_screen()
password = pg.create_pass()
print(f'Password generated: {password}')
# pyperclip.copy(password)
