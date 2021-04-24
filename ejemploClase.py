
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
      pi = 3.14 # (Will hardcode pi in this example)
      circumferenceValue = pi * self.radius * 2
      return circumferenceValue

    def printCircumference(self):
      myCircumference = self.circumference()
      print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))


radius1 = 2
radius2 = 5
radius3 = 7

circle1 = Circle(radius1)
circle1.printCircumference()



circle2 = Circle(radius2)
circle2.printCircumference()



circle3 = Circle(radius3)
circle3.printCircumference()