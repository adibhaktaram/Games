import turtle
class Plant:
    '''
    Represents a plant

    Attributes: phylum - string; level of taxonomic rank

    Methods: __init__
             __str__
    '''
    def __init__(self, phylum):
        self.phylum = phylum

    def __str__(self):
        return 'This Plant is of the taxonomic class %s' %(self.phylum)

class Flower(Plant):
    '''
    Represents a Flower

    Attributes: smell - string; what the flower smells like
                petal_type - Petal Object; an instance of the class 'LShaped' or 'TearDrop'
                num_petals - integer; the number of petals the flower has
    '''
    def __init__(self, smell, petal_type, num_petals):
        self.smell = smell
        self.petal_type = petal_type
        self.num_petals = num_petals

    def __str__(self):
        return 'This flower smells %s. %s, and this flower has %d petals' %(self.smell, str(self.petal_type), self.num_petals)

    def draw(self, turtle, fill = False):
        '''
        Description: This method draws a flower using the draw method in LShaped or TearDrop

        Parameters: turtle - turtle: the turtle that draws the flower
                    fill - boolean value; True or False depending on whether you want it to fill the flower or not

        Return Values: None
        '''
        for i in range(self.num_petals):
                self.petal_type.draw(turtle)
                turtle.lt(360/self.num_petals)

class Petal:
    '''
    Represents a Petal

    Attributes: color - string; the color of the petal

    Methods: __init__
             __str__
    '''
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'This petal has a color of %s' %(self.color)

class LShaped(Petal):
    '''
    Represents an L-Shaped petal

    Attributes: color - string; the color of the petal
                radius - float; the radius of the arc of the petal
                fill - boolean value; True or False depending on whether you want the petal to be filled or not
                angle - float; the angle of the turn in the arc

    Methods: __init__
             __str__
             draw
    '''
    def __init__(self, color, radius, fill = False, angle = 120):
        super().__init__(color)
        self.angle = angle
        self.radius = radius
        self.fill = fill

    def __str__(self):
        return 'This is an l-shaped petal with angle %d and radius %d' %(self.angle, self.radius)

    def draw(self, turtle):
        '''
        Description: This method draws a single LShaped petal

        Parameters: turtle - turtle; the turtle that draws the petal

        Return Values: None
        '''
        turtle.ht()
        turtle.color(self.color)
        if self.fill == False:
            turtle.circle(self.radius, 120)
            turtle.lt(self.angle)
            turtle.circle(self.radius, 120)
        else:
            turtle.begin_fill()
            turtle.circle(self.radius, 120)
            turtle.lt(self.angle)
            turtle.circle(self.radius, 120)
            turtle.end_fill()

class TearDrop(Petal):
    '''
    Represents a Tear-drop petal

    Attributes: color - string; the color of the petal
                radius - float; the radius of the arc of the petal
                fill - boolean value; True or False depending on whether you want the petal to be filled or not
                angle - integer; the angle of the triangle in the TearDrop petal

    Methods: __init__
             __str__
             draw
    '''

    def __init__(self, color, radius, fill = False, angle = 60):
        super().__init__(color)
        self.angle = angle
        self.radius = radius
        self.fill = fill

    def __str__(self):
        return 'This is a tear-drop shaped petal with angle %d and radius %d' %(self.angle, self.radius)

    def draw(self, turtle):
        '''
        Description: This method draws a single TearDrop petal

        Parameters: turtle - turtle; the turtle that draws the petal

        Return Values: None
        '''
        diameter = self.radius * 2
        turtle.ht()
        if self.fill == False:
            turtle.color(self.color)
            turtle.fd(diameter)
            turtle.lt(self.angle/2)
            turtle.circle(self.radius, 180)
            turtle.lt(self.angle/2)
            turtle.fd(diameter)
        else:
            turtle.begin_fill()
            turtle.color(self.color)
            turtle.fd(diameter)
            turtle.lt(self.angle/2)
            turtle.circle(self.radius, 180)
            turtle.lt(self.angle/2)
            turtle.fd(diameter)
            turtle.end_fill()

if __name__ == '__main__':
    win = turtle.Screen()
    win.bgcolor("black")
    myLShaped = LShaped("white", 125)
    myTearDrop = TearDrop("white", 125)
    myFlower = Flower("good", myTearDrop, 45)
    t = turtle.Turtle()
    t.speed(0)
    myFlower.draw(t)
    turtle.mainloop()
