class Dog:
    Created = 0

    def __init__(self, name, birth_year, sound="Woff woff"):
        self.name = name
        self.birth = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.sound)
        return


dog1 = Dog("Rockey", 2011)
dog2 = Dog("Hero", 2009)

dog1.bark(5)
dog2.bark(3)
