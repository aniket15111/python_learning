class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        avg=sum(self.marks)/len(self.marks)
        return avg
    def display(self):
        print(f"AAverage of {self.name} is {student1.average()}")

student1=Student("Aniket",[70,80,90,95,88])
student1.display()

