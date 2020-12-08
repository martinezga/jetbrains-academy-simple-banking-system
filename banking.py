import random
import sqlite3


menu_options = {
        '1': '1. Create an account',
        '2': '2. Log into account',
        '0': '0. Exit'
}


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


class DbManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        self.CREATE_CARD_TABLE = """
        CREATE TABLE card (
            id INTEGER PRIMARY KEY,
            number TEXT UNIQUE,
            pin TEXT,
            balance INTEGER DEFAULT 0);"""
        self.INSERT_CARD = "INSERT INTO card (number, pin) VALUES (?, ?);"
        self.GET_ALL_CARDS = "SELECT * FROM card;"
        self.GET_PIN_BY_NUMBER = "SELECT pin FROM card WHERE number = ?;"
        self.GET_BALANCE = "SELECT balance FROM card WHERE number = ?;"

    def close_cursor(self):
        self.conn.close()

    def create_table(self):
        try:
            self.cur.execute(self.CREATE_CARD_TABLE)
        except:
            pass

    def insert_card(self, number, pin):
        self.cur.execute(self.INSERT_CARD, (number, pin))
        self.conn.commit()

    def get_pin_by_number(self, number):
        pin = self.cur.execute(self.GET_PIN_BY_NUMBER, (number, )).fetchone()
        if pin is None:
            return 'error'
        else:
            return pin[0]

    def get_balance(self, number):
        balance = self.cur.execute(self.GET_BALANCE, (number, )).fetchone()
        if balance is None:
            return 0
        else:
            return balance[0]

    def get_all_cards(self):
        return self.cur.execute(self.GET_ALL_CARDS).fetchall()

    # def drop_table(self):
        # self.cur.execute("DROP TABLE card;")


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
            db.close_cursor()
            continue_balance = False
            return 0
        elif user_option == '1':
            balance = db.get_balance(card_num)
            print(f'\nBalance: {balance}\n')
        elif user_option == '2':
            print('\nYou have successfully logged out!\n')
            continue_balance = False
            return 1
        else:
            print('Error')


db = DbManager('card.s3db')
# db.drop_table()
db.create_table()
main()
