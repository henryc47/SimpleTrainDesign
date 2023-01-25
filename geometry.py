#functions relating to the fundamental geometry of a carriage


#single_deck = SingleDeckCarriage(length=20,width=3,floor_height=1.3,roof_height=3.7,triangle_height=3.3,triangle_width=2,ceiling_height=2.1)

class Carriage:
    def __init__(self,length,width,floor_height,roof_height,triangle_height,triangle_width):
        self.length = length #length of the carriage, metres
        self.width = width  #width of the carriage, metres
        self.floor_height = floor_height #height of the floor above the rail, metres
        self.roof_height = roof_height  #height of the roof above the rail, metres
        self.triangle_height = triangle_height #height where the width starts to reduce, metres above the rail
        self.triangle_width = triangle_width #minimum width of the roof, metres

class SingleDeckCarriage(Carriage):
    def __init__(self,length,width,floor_height,roof_height,triangle_height,triangle_width,ceiling_height):
        Carriage.__init__(self,length,width,floor_height,roof_height,triangle_height,triangle_width) #setup base class
        self.ceiling_height = ceiling_height #height of ceiling above the floor, metres

    

