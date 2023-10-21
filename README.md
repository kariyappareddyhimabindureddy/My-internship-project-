# My-internship-project-
import string
import random

print('------------Welcome to Password Generator------------')
print()
length = int(input('Enter length of the password: '))
nos = int(input('How many password you want to generate: '))

all_letters = string.ascii_letters + string.digits + '_@#$/?'

pw = []
temp_pass = ''
for i in range(nos):
    for j in range(length):
        temp_pass += random.choice(all_letters)
    pw.append(temp_pass)
    temp_pass = ''
print()
print(f'----------Here is your passwords----------')
print()
for i in pw:
    print(i)
