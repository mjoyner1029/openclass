# task 1
first_name = input('Please input your first name. ')
last_name = input('Please input your last name. ')

if 3 <= len(first_name and last_name):
    print('Thank you')
else:
    print('name is invalid')


# task 2
def password():

    print ('enter password')
    print ()
    print ()
    print ('the password must be at least 6, and no more than 12 characters long')
    print ()

    password = input('type your password    ....')


    weak = 'weak'
    med = 'medium'
    strong = 'strong'

    if len(password) >12:
        print ('password is too long It must be between 6 and 12 characters')

    elif len(password) <6:
        print ('password is too short It must be between 6 and 12 characters')


    elif len(password)    >=6 and len(password) <= 12:
        print ('password ok')

        if password.lower()== password or password.upper()==password or password.isalnum()==password:
            print ('password is', weak)

        elif password.lower()== password and password.upper()==password or password.isalnum()==password:
            print ('password is', med)

        else:
            password.lower()== password and password.upper()==password and password.isalnum()==password
            print ('password is', strong)


# task 3
email = input('What is your email?: ')

def check(email):
 
    if(re.fullmatch(regex, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")