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


class DevOps(Employee):
    def __init__(self, first_name, last_name, salary, skills=[]):
        super().__init__(first_name, last_name, salary)
        self.skills = [skill.title() for skill in skills]

    def add_skill(self, skill):
        if skill.title() not in self.skills:
            self.skills.append(skill.title())

    def remove_skill(self, skill):
        try:
            self.skills.remove(skill.title())
        except ValueError as error:
            return error


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, subordinates=[]):
        super().__init__(first_name, last_name, salary)
        self.subordinates = subordinates

    def add_subordinate(self, subordinate):
        if subordinate not in self.subordinates:
            self.subordinates.append(subordinate)

    def remove_subordinate(self, subordinate):
        if isinstance(subordinate, str):
            for employee in self.subordinates:
                if employee.email == subordinate:
                    self.subordinates.remove(employee)
        else:
            try:
                self.subordinates.remove(subordinate)
            except ValueError as error:
                return error
