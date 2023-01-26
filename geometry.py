#functions relating to the fundamental geometry of a carriage

#driver_compartment = g.DriverCompartment(length=3,triangle_grade=0.5,ceiling_height=2.1)
#gangway = g.Gangway(length=0.25,width=1.4,height=2.1)
#single_deck_centre = g.SingleDeckCarriage(length=20,width=3,floor_height=1.3,roof_height=3.7,ceiling_height=2.1,triangle_height=3.3,triangle_width=1.5,gangway=gangway,num_gangways=2,driver_compartment=0)
#double_deck_centre = g.DoubleDeckCarriage(length=20,width=3,floor_height=1.3,roof_height=4.4,ceiling_height=2.1,triangle_height=4,triangle_width=1.5,gangway=gangway,num_gangways=2,driver_compartment=0,lower_floor_height=0.5,lower_ceiling_height=1.8,interstage_height=0.1,upper_ceiling_height=1.8,stair_grade=1)
#single_deck_driving = g.SingleDeckCarriage(length=20,width=3,floor_height=1.3,roof_height=3.7,ceiling_height=2.1,triangle_height=3.3,triangle_width=1.5,gangway=gangway,num_gangways=1,driver_compartment=driver_compartment)
#double_deck_driving = g.DoubleDeckCarriage(length=20,width=3,floor_height=1.3,roof_height=4.4,ceiling_height=2.1,triangle_height=4,triangle_width=1.5,gangway=gangway,num_gangways=1,driver_compartment=driver_compartment,lower_floor_height=0.5,lower_ceiling_height=1.8,interstage_height=0.1,upper_ceiling_height=1.8,stair_grade=1)
#gangway between carriages
class Gangway:
    def __init__(self,length,width,height):
        self.length = length #length of the gangway between carriages (0.25m), this is in addition to the carriage length
        self.width = width #width of the gangways
        self.height = height #height of the gangways
    
class DriverCompartment:
    def __init__(self,length,triangle_grade,ceiling_height):
        self.length = length #length of the drivers compartment
        self.triangle_grade = triangle_grade #metres the front goes forward for each meter it rises/falls
        self.ceiling_height = ceiling_height
    
    #import info about the carriage as a whole
    def provide_carriage_specs(self,width,floor_height,roof_height,triangle_height,triangle_width):
        self.width = width
        self.floor_height = floor_height
        self.roof_height = roof_height
        self.triangle_height = triangle_height
        self.triangle_width = triangle_width



#carriage
class Carriage:
    def __init__(self,length,width,floor_height,ceiling_height,roof_height,triangle_height,triangle_width,gangway,num_gangways,driver_compartment):
        self.length = length #length of the carriage, metres
        self.width = width  #width of the carriage, metres
        self.floor_height = floor_height #height of the floor above the rail, metres
        self.ceiling_height = ceiling_height #height of the ceiling above the floor, metres
        self.roof_height = roof_height  #height of the roof above the rail, metres
        self.triangle_height = triangle_height #height where the width starts to reduce, metres above the rail
        self.triangle_width = triangle_width #minimum width of the roof, metres
        self.gangway = gangway #info about the gangways
        self.num_gangways = num_gangways #number of gangways attached to the carriage, 1 for driving carriage, 2 for other carriages
        if driver_compartment==0: #if no driver compartment, provide zero
            self.is_driver_compartment = False
            self.passenger_section_length = self.length #length of the passenger section is equal to length of carriage
        else:
            self.is_driver_compartment = True
            self.driver_compartment = driver_compartment
            self.driver_compartment.provide_carriage_specs(self.width,self.floor_height,self.roof_height,self.triangle_height,self.triangle_width)
            self.passenger_section_length = self.length-self.driver_compartment.length #length of the passenger section is equal to length of carriage excluding length of driver compartment

class SingleDeckCarriage(Carriage):
    def __init__(self,length,width,floor_height,ceiling_height,roof_height,triangle_height,triangle_width,gangway,num_gangways,driver_compartment):
        Carriage.__init__(self,length,width,floor_height,ceiling_height,roof_height,triangle_height,triangle_width,gangway,num_gangways,driver_compartment)
        

    
class DoubleDeckCarriage(Carriage):
    def __init__(self,length,width,floor_height,ceiling_height,roof_height,triangle_height,triangle_width,stair_grade,gangway,driver_compartment,num_gangways,lower_floor_height,lower_ceiling_height,interstage_height,upper_ceiling_height):
        Carriage.__init__(self,length,width,floor_height,ceiling_height,roof_height,triangle_height,triangle_width,gangway,num_gangways,driver_compartment)
        #note in double deck formation, floor and ceiling height is the height of the centre section
        self.lower_floor_height = lower_floor_height #lower section height above the rails
        self.lower_ceiling_height = lower_ceiling_height #height of the lower ceiling
        self.interstage_height = interstage_height #height between the lower ceiling and the upper floor
        self.upper_ceiling_height = upper_ceiling_height #height between the upper floor and upper ceiling
        self.stair_grade = stair_grade

    #def calculate_stair
