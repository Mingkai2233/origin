class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def nameSet(self, name):
        self.name = name

    def ageSet(self, age):
        self.age = age

    def genderSet(self, gender):
        self.gender = gender

    def showName(self):
        print("name:", self.name)

    def showAge(self):
        print("age:", self.age)

    def showClassName(self):
        print("className:", type(self))


class Student(People):
    def __init__(self, name, age, gender, studentNumber, grade):
        super(Student, self).__init__(name, age, gender)
        self.studentNumber = studentNumber
        self.grade = grade

    def add(self):
        return int(self.studentNumber[1:])+int(self.grade)

    def showInfo(self):
        self.showName()
        self.showAge()
        print("gender:", self.gender)
        print("studentNumber:", self.studentNumber)
        print("grade:", self.grade)


if __name__ == "__main__":
    me = Student("张明凯", 21, "男", "E01914293", 2019)
    me.showInfo()
    print(me.add())
