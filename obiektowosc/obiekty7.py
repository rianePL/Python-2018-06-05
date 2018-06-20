from obiektowosc import obiekty2


class PremiumEmployee(obiekty2.Employee):

    def __init__(self, bonus, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bonus = bonus

    def give_bonus(self, amount):
        self._bonus += amount

    def pay_salary(self):
        salary = super().pay_salary()
        salary += self._bonus
        self._bonus = 0
        return salary

albert = PremiumEmployee(fname='Albert',lname='the best',sal=200, bonus=300)
albert.register_time(5)
print(albert.pay_salary())

print(albert.lname)

