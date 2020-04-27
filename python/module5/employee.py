class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary
        self.email = f'{first_name.lower()}_{last_name.lower()}@example.com'
        self.full_name

    @property
    def full_name(self):
        return f'{self.first_name}, {self.last_name}'

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(", ")
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    @classmethod
    def from_str(cls, emp_str):
        first_name, last_name, salary = emp_str.split(",")
        return cls(first_name, last_name, int(salary))
