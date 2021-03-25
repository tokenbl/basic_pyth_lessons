class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'зряплата': wage, 'премия': bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['зряплата'] + " " + self._income['премия']


staff_member = Position('Pupken', 'Vladimir', 'president', '9700000', 'top_secret')
print(staff_member.get_full_name(), staff_member.get_total_income())
staff_member = Position('Raushanov', 'Djamshut', 'janitor', '15000', '-7800')
print(staff_member.get_full_name(), staff_member.get_total_income())
