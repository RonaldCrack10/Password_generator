import string
import random

#

def password_gen(length= 12,letter = 8 , number: int = 2, ascii = 2):

    if letter + number + ascii != length:
        raise ValueError('Gib entsprechende Zahlen ein')


    

    letters = [random.choice(string.ascii_letters) for letters in range(letter)]
    digits = [random.choice(string.digits) for digits in range(number)]
    zeichen = [random.choice(string.punctuation) for ascii in range(ascii)]

    characters = letters + digits + zeichen
        
    for password in range(length):
        password = ''.join(characters)


   
    return password

password = password_gen(length= 16,letter= 8, number=4, ascii=4)
print(password)

with open('Password Speicher.txt', 'a') as file: #'w' überschreibt einfach während 'a' append
    ziel_app = input("Fuer welche App brauchst du das Passwort: ")
    file.write(f'\nThe password for {ziel_app} is : {password}')



    

