from Module import Person, Wizard, HealthPotion

def test_Person():
    person = Person("Bob")
    expected_Person_name = "Bob"
    assert person.name == expected_Person_name
    assert person.life_points == 100

def test_hit_Person():
    person = Person("Bob")
    person.hit(person)
    expected_life = 90
    assert person.life_points == expected_life

def test_is_dead():
    person = Person("Bob")
    assert person.is_dead() == False
    for _ in range(10):
        person.hit(person)
    assert person.is_dead() == True

def test_gained_life_points():
    person = Person("Bob")
    person.gained_life_points(10)
    expected_life_point = 110
    assert person.get_life_points() == expected_life_point

def test_get_life_points():
    person = Person("Bob")
    assert person.get_life_points() == 100

def test_Wizard():
    wizard = Wizard("Gandalf")
    expected_Wizard_name = "Gandalf"
    assert wizard.name == expected_Wizard_name