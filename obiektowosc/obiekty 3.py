class ElectricCar():
    def __init__(self,dist):
        self.dist = dist
        self.batt = dist

    def drive(self, range):
        # sposób 1
        # if range <= self.batt:
        #     self.batt -= range
        #     return range
        # else:
        #     act_batt = self.batt
        #     self.batt = 0
        #     return act_batt

        # sposób 2
        # act_batt = self.batt
        # self.batt = 0 if range > self.batt else self.batt - range
        # return range if act_batt >= range else act_batt

        # sposób 3
        act_range = min(self.batt, range)
        self.batt -= act_range
        return act_range

    def charge(self, val=None):
        if val is None or val + self.batt > self.dist:
            self.batt = self.dist
        else:
            self.batt += val


def test_ElectricCar_new():
    v = ElectricCar(100)
    assert v.dist == 100
    assert v.batt == 100

def test_ElectricCar_first_drive():
    v = ElectricCar(100)
    assert v.drive(70) == 70

def test_ElectricCar_too_long():
    v = ElectricCar(100)
    assert v.drive(120) == 100

def test_ElectricCar_two_rides():
    v = ElectricCar(100)
    assert v.drive(60) == 60
    assert v.drive(60) == 40

def test_ElectricCar_charge():
    v = ElectricCar(100)
    v.drive(60)
    v.charge()
    assert v.dist == 100
    assert v.batt == 100

def test_ElectricCar_charge2():
    v = ElectricCar(100)
    v.drive(90)
    v.charge(50)
    assert v.dist == 100
    assert v.batt == 60

def test_ElectricCar_charge3():
    v = ElectricCar(100)
    v.drive(90)
    v.charge(120)
    assert v.dist == 100
    assert v.batt == 100