import random
import string 

def menu():
    while True:
        choice = input('''-- Password generator --
                    Choose option:
                    1: generate password
                    2: exit the program
                    Your choice: ''')
        if choice == '1':
            make_password()
        elif choice == '2':
            print('Bye!')
            break
        else:
            print('Please enter a correct value')

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits 
special = '!@#$%^&*()|_+'

def make_password():
    contains = list(string.ascii_lowercase)
    require = ''

    length = int(input('Provide password length: '))

    if input('Use uppercase letters? (y/n): ') == 'y':
        [contains.append(x) for x in upper]
        require + 'u'

    if input('Use digits? (y/n): ') == 'y':
        [contains.append(x) for x in digits]
        require + 'd'

    if input('Use special characters? (y/n): ') == 'y':
        [contains.append(x) for x in special]
        require + 's'

    str = ''
    print(contains)
    password = ''.join([str + x for x in random.choices(contains, k = length)])

    print(password)

    return password

menu()

# def check_requirements(password, require):
#     if 'u' in require:
#         if any(upper & password):
#             print('yayy')
#     print(password)

