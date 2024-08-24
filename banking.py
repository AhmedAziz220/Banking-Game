def showbalance():
    print('your balance is $',balance)


def deposit():
    amount = float(input('Enter an amount: '))
    if amount < 0:
        print('Invalid amount. Please enter a positive value.')
        return 0
    else:
        return amount


def withdraw():
    amount = float(input('Enter an amount: '))
    if amount < 0:
        print('Invalid amount. Please enter a positive value.')
        return 0
    elif amount > balance:
        print('Insufficient funds. Please try again.')
        return 0
    else:
        return amount


balance = 0
is_running = True

while is_running:
    print('Banking Program')
    print('1. Show Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        showbalance()
    elif choice == 2:
        balance += deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        is_running = False
    else:
        print('Invalid choice. Please try again.')


print('Thank you have a nice day')