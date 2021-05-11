class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(f'Name: {name}\n'
              f'Age: {age}\n'
              f'Gender: {gender}')

    def calculate_age(self, years):
        self.years = years
        print(f'Через {years} лет John исполнится {self.age + years}')


p = Person('John', 23, 'male')
p.calculate_age(10)
