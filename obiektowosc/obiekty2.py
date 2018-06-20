class Employee():
    def __init__(self, fname, lname, sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal
        self.wallet = 0

    def pay_salary(self):
        salary = self.wallet
        self.wallet = 0
        return salary

    def register_time(self, hours):
        # self.wallet += hours * self.sal
        # if hours > 8:
        #     self.wallet += (hours - 8) * self.sal

        self.wallet += self.sal * (hours if hours <= 8 else 2 * hours - 8)


def test_Employee_tworzenie():
    prac = Employee('Jan', 'Kowalski', 100.0)
    assert prac.fname == 'Jan'
    assert prac.lname == 'Kowalski'
    assert prac.sal == 100.0


def test_Employee_payday():
    prac = Employee('Jan', 'Kowalski', 100.0)
    prac.register_time(5)
    assert prac.pay_salary() == 500.0


def test_Employee_payday2():
    prac = Employee('Jan', 'Kowalski', 100.0)
    prac.register_time(5)
    assert prac.pay_salary() == 500.0
    assert prac.pay_salary() == 0.0


def test_Employee_overtime():
    prac = Employee('Jan', 'Kowalski', 100.0)
    prac.register_time(10)
    assert prac.pay_salary() == 1200.0


def test_Employee_two_days():
    prac = Employee('Jan', 'Kowalski', 100.0)
    prac.register_time(10)
    prac.register_time(5)
    assert prac.pay_salary() == 1700.0
