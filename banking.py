import random
import sqlite3


menu_options = {
        '1': '1. Create an account',
        '2': '2. Log into account',
        '0': '0. Exit'
}

BALANCE_PROMPT = """1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
"""


class DbManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        self.CREATE_CARD_TABLE = """
        CREATE TABLE if not exists card (
            id INTEGER PRIMARY KEY,
            number TEXT UNIQUE,
            pin TEXT,
            balance INTEGER DEFAULT 0);"""
        self.INSERT_CARD = "INSERT INTO card (number, pin) VALUES (?, ?);"
        self.GET_PIN_BY_NUMBER = "SELECT pin FROM card WHERE number = ?;"
        self.GET_BALANCE = "SELECT balance FROM card WHERE number = ?;"
        self.UPDATE_BALANCE = "UPDATE card SET balance = ? WHERE number = ?;"
        self.DELETE_ACCOUNT = "DELETE FROM card WHERE number = ?;"

    def close_cursor(self):
        self.conn.close()

    def create_table(self):
        self.cur.execute(self.CREATE_CARD_TABLE)

    def insert_card(self, number, pin):
        self.cur.execute(self.INSERT_CARD, (number, pin))
        self.conn.commit()

    def get_pin_by_number(self, number):
        pin = self.cur.execute(self.GET_PIN_BY_NUMBER, (number, )).fetchone()
        if pin is None:
            return -1
        else:
            return pin[0]

    def get_balance(self, number):
        balance = self.cur.execute(self.GET_BALANCE, (number, )).fetchone()
        if balance is None:
            return -1
        else:
            return balance[0]

    def update_balance(self, card_num, new_balance):
        self.cur.execute(self.UPDATE_BALANCE, (new_balance, card_num))
        self.conn.commit()

    def delete_account(self, card_num):
        self.cur.execute(self.DELETE_ACCOUNT, (card_num, ))
        self.conn.commit()

    # def drop_table(self):
        # self.cur.execute("DROP TABLE card;")


class Transactions:
    def __init__(self, balance):
        self.balance = balance

    def add_income(self, money):
        if money > 0:
            self.balance = self.balance + money
            return self.balance
        else:
            return -1

    def do_transfer(self, money):
        if money < 0 or money > self.balance:
            return -1
        else:
            self.balance = self.balance - money
            return self.balance


def create_account():
    inn = '400000'
    customer_num = get_random(900000000, 999999999)
    checksum = luhn_algorithm(inn + str(customer_num))
    card_num = inn + str(customer_num) + str(checksum)
    card_pin = str(get_random(9000, 9999))
    return [card_num, card_pin]


def get_random(start, end):
    rand_num = random.randrange(start, end)
    return rand_num


def luhn_algorithm(card_str):
    card_num = []
    list_sum = 0
    checksum = 0
    for element in card_str:
        card_num.append(int(element))
    for i in range(len(card_num)):
        if i % 2 == 0:
            card_num[i] *= 2
    for i in range(len(card_num)):
        if card_num[i] > 9:
            card_num[i] -= 9
    for i in card_num:
        list_sum += i
    for i in range(1, 10):
        if (list_sum + i) % 10 == 0:
            checksum = i
    return checksum


def balance_menu(card_num):
    continue_balance = True
    while continue_balance:
        user_option = input(BALANCE_PROMPT)
        if user_option == '0':
            db.close_cursor()
            return 0
        elif user_option == '1':
            balance = db.get_balance(card_num)
            print(f'\nBalance: {balance}\n')
        elif user_option == '2':
            do_transaction(card_num, user_option, 0)
        elif user_option == '3':
            print('Transfer')
            card_to_transfer = input('Enter card number:\n')
            if valid_transfer_card(card_num, card_to_transfer):
                do_transaction(card_num, user_option, card_to_transfer)
        elif user_option == '4':
            db.delete_account(card_num)
            print('\nThe account has been closed!\n')
            return 1
        elif user_option == '5':
            print('\nYou have successfully logged out!\n')
            return 1
        else:
            print('Error')


def do_transaction(card_num, user_option, card_to_transfer):
    user_balance = db.get_balance(card_num)
    user = Transactions(user_balance)
    receiver_balance = db.get_balance(card_to_transfer)
    receiver = Transactions(receiver_balance)
    if user_option == '2':
        money = int(input('Enter income:\n'))
        new_balance = user.add_income(money)
        if new_balance != -1:
            db.update_balance(card_num, new_balance)
            print('Income was added!\n')
        else:
            print('Error')
    elif user_option == '3':
        money = int(input('Enter how much money you want to transfer:\n'))
        user_new_balance = user.do_transfer(money)
        receiver_new_balance = receiver.add_income(money)
        if user_new_balance != -1:
            db.update_balance(card_num, user_new_balance)
            db.update_balance(card_to_transfer, receiver_new_balance)
            print('\nSuccess!\n')
        else:
            print('Not enough money!\n')


def valid_transfer_card(user_card, card_to_transfer):
    flag = 1
    if user_card == card_to_transfer:
        print("You can't transfer money to the same account!")
        flag = flag - 1
    elif str(luhn_algorithm(card_to_transfer[:15])) != card_to_transfer[15]:
        print('Probably you made a mistake in the card number. Please try again!\n')
        flag = flag - 1
    elif db.get_balance(card_to_transfer) == -1:
        print('Such a card does not exist.\n')
        flag = flag - 1
    if flag == 1:
        return 1
    else:
        return 0


def main():
    user_continue = True
    while user_continue:
        for option in menu_options:
            print(menu_options[option])
        user_option = input()
        if user_option == '0':
            db.close_cursor()
            user_continue = False
            print('\nBye!')
        elif user_option == '1':
            card = create_account()
            db.insert_card(card[0], card[1])
            print('\nYour card has been created')
            print(f'Your card number:\n{card[0]}')
            print(f'Your card PIN:\n{card[1]}\n')
        elif user_option == '2':
            print('\nEnter your card number:')
            user_card = input()
            print('Enter your PIN:')
            user_pin = input()
            if db.get_pin_by_number(user_card) != user_pin:
                print('\nWrong card number or PIN!\n')
            else:
                print('\nYou have successfully logged in!\n')
                user_continue = balance_menu(user_card)
        else:
            print('Error')


db = DbManager('card.s3db')
# db.drop_table()
db.create_table()
main()
