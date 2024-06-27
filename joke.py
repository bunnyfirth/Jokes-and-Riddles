playAgain = True
while playAgain:
    print('why did the chicken cross the road?')
    text = input('')
    if text=='To get to the other side!':
        print('you got it corect!')
    else:
        print('you got it wrong!')
        print('the correct answer was :To get to the other side!')
    text = input('')

    answered = False
    while not answered:
        print('if you want to play again, type play again!')
        text = input('')

        if text == 'play again':
            playAgain = True
            answered = True
        elif text == 'no thanks':
            playAgain = False
            answered = True
            print('ok.')
        elif text == 'Potato!':
            print('YES!!!!!')
            playAgain = True
            answered = True
            potato = True
        elif text == 'No':
            print("ABA")
            playAgain = True
            answered = True
        else:
            print('type no thanks or python joke.py!')