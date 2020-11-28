import random


menu_options = {
        '1': '1. Create an account',
        '2': '2. Log into account',
        '0': '0. Exit'
}
bank_accounts = {}


def main():
    user_continue = True
    while user_continue:
        for option in menu_options:
            print(menu_options[option])
        user_option = input()
        if user_option == '0':
            user_continue = False
            print('\nBye!')
        elif user_option == '1':
            card = create_account()
            bank_accounts[card[0]] = card[1]
            print('\nYour card has been created')
            print(f'Your card number:\n{card[0]}')
            print(f'Your card PIN:\n{card[1]}\n')
        elif user_option == '2':
            print('\nEnter your card number:')
            user_card = input()
            print('Enter your PIN:')
            user_pin = input()
            if check_user(user_card, user_pin):
                print('\nYou have successfully logged in!\n')
                user_continue = balance_menu()
            else:
                print('\nWrong card number or PIN!\n')
        else:
            print('Error')


def create_account():
    inn = '400000'
    customer_num = get_random(999999999)
    checksum = '3'
    card_num = inn + str(customer_num) + checksum
    card_pin = str(get_random(9999))
    return [card_num, card_pin]


def get_random(num):
    rand_num = random.randrange(0, num)
    return rand_num


def check_user(card_num, card_pin):
    for accounts in bank_accounts:
        if accounts == card_num and bank_accounts[accounts] == card_pin:
            return 1
        else:
            return 0


def balance_menu():
    continue_balance = True
    menu = {
        '1': '1. Balance',
        '2': '2. Log out',
        '3': '0. Exit'
    }
    while continue_balance:
        for option in menu:
            print(menu[option])
        user_option = input()
        if user_option == '0':
            continue_balance = False
            return 0
        elif user_option == '1':
            # get_balance()
            print(f'\nBalance: 0\n')
        elif user_option == '2':
            print('\nYou have successfully logged out!\n')
            continue_balance = False
            return 1
        else:
            print('Error')


main()
