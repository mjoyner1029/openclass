# task 1
#Questions one: What is car company created the M series? Answer: BMW 
#Question two: what super car company is owned by fiat? Answer: Ferrari 
#Question three: what car is famous for their 911 car? Answer: Porsche

questions = [
    'What is car company created the M series? ',
'What super car company is owned by fiat? ',
'What car is famous for their 911 car? ' 
]

answers = ['BMW, Ferrari, Porsche']

for i in range(len(questions)):
    user_answer = input(questions[i] + " ")
    try:
        if user_answer == 'BMW':
            print('Bayerische Motoren Werke(BMW) is correct')
            score += 1
        else:
            print('That is incorrect')

        if user_answer == 'Ferrari':
            print('Ferrari is correct, they are known for game-changing performance and unparalleled elegance')
            score += 1
        else:
            print('That is incorrect')
        if user_answer == 'porsche':
            print('Porsche is known for their 911. Many believe it is the greatest sports car ever to be made.')
            score += 1
        else:
            print('That is incorrect')
    except ValueError:
        print('invalidinput')

print(f'your final score is {score}/{len(questions)}.')