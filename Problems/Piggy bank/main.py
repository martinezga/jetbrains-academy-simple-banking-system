class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        cents = (self.cents + deposit_cents) % 100
        sum_cents = self.cents + deposit_cents
        total_dollars = self.dollars + deposit_dollars + sum_cents // 100
        self.dollars = total_dollars
        self.cents = cents
        return f' {self.dollars} {self.cents}'


# gab_bank = PiggyBank(1, 1)
# print(gab_bank.add_money(500, 500))
