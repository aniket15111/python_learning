from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound():
        return


# class Dog(Animal):                                    this one will not work because the abstract method is not present
#     def __init__(self):                                     
#         pass


class Dog(Animal):                                   
    def __init__(self):                                     
        pass
    def sound(self):
        print("Bark")

a1=Dog()
a1.sound()
