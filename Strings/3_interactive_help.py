# task 1

commands = ("help", "issue", "contact support")

user_command = input('How can i help you today? ')

if user_command == 'help':
    print('How may I help you today?')
elif user_command == 'issue':
    print('What issue are you currectly dealing with?')
elif user_command == 'contact support':
    print('Transfering you to one of our support members now')
else:
    print("I'm sorry many there is something else i can help with?")

# task 2

issues = ("login", "performance", "error")

#print('User is dealing with user login issues.')
#print('User is having proformance issues.')
#print('User is recieving error message.')