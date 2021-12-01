secret_number = 777

print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)
your_number = int(input('Enter your number :'))
while your_number != 0:
    if your_number == secret_number:
        print('Well done, muggle ! you are free now')
    else:
        print('Haha you are stuck in my loop')
        second_attempt =int(input('Enter your number again: '))
