#Basic class Parent and Child

class Parent():
    def __init__(self, lastName, eyeColor):
        print("Parent constructor called.")
        self.lastName = lastName
        self.eyeColor = eyeColor

    def showInfo(self):
        print("Last name: " + self.lastName)
        print("Eye color: " + self.eyeColor)

class Child(Parent):
    def __init__(self, lastName,eyeColor, numSongs):
        print("Child constructor called.")
        Parent.__init__(self,lastName,eyeColor)
        self.numSongs = numSongs

    def showInfo(self):
        print("Last name: " + self.lastName)
        print("Eye color: " + self.eyeColor)
        print("Number of songs: " + str(self.numSongs))

hansLarsson = Parent("Larsson","black")
hansLarsson.showInfo()

zaraLarsson = Child("Larsson","black",150)
zaraLarsson.showInfo()
