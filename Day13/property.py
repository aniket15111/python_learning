class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):             # This is the getter
        return self._age

    @age.setter
    def age(self, value):      # This is the setter
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


p = Person(25)
print(p.age)     # ➤ Calls the getter → 25
p.age = 30       # ➤ Calls the setter → _age = 30
# p.age = "hi"     # ❌ TypeError

