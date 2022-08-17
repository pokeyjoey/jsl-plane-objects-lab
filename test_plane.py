from plane import Plane, twa, boeing
def test_boeing_initialized():
    assert type(boeing) == Plane

def test_twa_initialized():
    assert type(twa) == Plane

def test_boeing_seats_per_row():
    assert boeing.seats_per_row == 10

def test_boeing_number_rows():
    assert boeing.number_of_rows == 30

def test_twa_seats_per_row():
    assert twa.seats_per_row == 6

def test_twa_number_rows():
    assert twa.number_of_rows == 25

def test_init_with_seats_per_row():
    boeing_2020 = Plane(year = 2020, seats_per_row = 10)
    assert boeing_2020.seats_per_row == 10

def test_init_with_year():
    boeing_2020 = Plane(year = 2020, seats_per_row = 10)
    assert boeing_2020.year == 2020

def test_default_init_number_of_rows():
    boeing_2020 = Plane(year = 2020, seats_per_row = 10)
    assert boeing_2020.number_of_rows == 20

def test_init_year():
    boeing_2020 = Plane(year = 2020, seats_per_row = 10)
    assert boeing_2020.year == 2020

def test_total_seats():
    boeing_2020 = Plane(year = 2020, seats_per_row = 10, number_of_rows = 10)
    assert boeing_2020.total_seats() == 100

def test_age():
    boeing_2020 = Plane(year = 2018, seats_per_row = 10, number_of_rows = 10)
    assert boeing_2020.age() == 2