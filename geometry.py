#functions relating to the fundamental geometry of a carriage



#a passenger on the train
class Passenger:
    def __init__(self,mean_weight,design_weight,design_density):
        self.mean_weight = mean_weight #mean weight of a passenger during simulation, kg
        self.design_weight = design_weight #mean weight of a passenger for design (worst-case) purposes, kg
        self.design_density = design_density #design density of passengers per square metre

#a seat on the train
class Seat:
    def __init__(self,length,width,weight,reversible,direction):
        self.length = length #length between the seats including legroom, m
        self.width = width #width of the seats, m
        self.weight = weight #weight of the seat, kg
        self.reversible = reversible #is the seat reversible, True or False
        self.direction = direction #direction of the seat, horizontal or vertical

#gangway between carriages
class Gangway:
    def __init__(self,length,width,height):
        self.length = length #length of the gangway between carriages (0.25m), this is in addition to the carriage length
        self.width = width #width of the gangways
        self.height = height #height of the gangways

#compartment at front/rear of train for the driver    
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

#area of the vehicle near the doors where passengers board/alight
#on all our trains there are two, one at each end
class Vestible:
    def __init__(self,doorway_width,extra_width):
        self.doorway_width = doorway_width
        self.extra_width = extra_width
        self.length = self.doorway_width + self.extra_width

#area of the vehicle near the doors where seating is horizontal
class Saloon:
    def __init__(self,length):
        self.length = length

#stores info about the outer geometry of the carriage
class CarriageOuterGeometry:
    def __init__(self,length,width,roof_height,triangle_height,triangle_width):
        self.length = length #length of the carriage, metres
        self.width = width  #width of the carriage, metres
        self.roof_height = roof_height  #height of the roof above the rail, metres
        self.triangle_height = triangle_height #height where the width starts to reduce, metres above the rail
        self.triangle_width = triangle_width #minimum width of the roof, metres

#stores info about the interior geometry of the carriage(at entry level only for double decker trains)
class CarriageInnerGeometry:
    def __init__(self,floor_height,ceiling_height):
        self.floor_height = floor_height #height of the floor above the rail, metres
        self.ceiling_height = ceiling_height #height of the ceiling above the floor, metres

#for double decker trains, stores info about the split level section
class DoubleDeckGeometry:
    def __init__(self,lower_floor_height,lower_ceiling_height,interstage_height,upper_ceiling_height,stair_grade,stair_width,stair_seats_lost):
        self.lower_floor_height = lower_floor_height #lower section height above the rails, metres
        self.lower_ceiling_height = lower_ceiling_height #height of the lower ceiling, metres
        self.interstage_height = interstage_height #height between the lower ceiling and the upper floor, metres
        self.upper_ceiling_height = upper_ceiling_height #height between the upper floor and upper ceiling, metres
        self.stair_grade = stair_grade #how much does the stair rise/fall for every metre it goes forward
        self.stair_width = stair_width #width of the stairwell, metres
        self.stair_seats_lost = stair_seats_lost #how many seats in the deck are lost due to the stairwell, per stairwell
        self.upper_floor_height = self.lower_floor_height + self.lower_ceiling_height + self.interstage_height #higher section height above the rails, metres


#train carriage
class Carriage:
    def __init__(self,carriage_outer,carriage_inner,gangway,num_gangways,driver_compartment,vestible,num_vestibles,num_saloons,saloon):
        self.carriage_outer = carriage_outer
        self.carriage_inner = carriage_inner
        self.gangway = gangway #info about the gangways
        self.num_gangways = num_gangways #number of gangways attached to the carriage, 1 for driving carriage, 2 for other carriages
        if driver_compartment==0: #if no driver compartment, provide zero
            self.is_driver_compartment = False
            self.passenger_section_length = self.carriage_outer.length #length of the passenger section is equal to length of carriage
        else:
            self.is_driver_compartment = True
            self.driver_compartment = driver_compartment
            self.driver_compartment.provide_carriage_specs(self.carriage_outer.width,self.carriage_inner.floor_height,self.carriage_outer.roof_height,self.carriage_outer.triangle_height,self.carriage_outer.triangle_width)
            self.passenger_section_length = self.carriage_outer.length-self.driver_compartment.length #length of the passenger section is equal to length of carriage excluding length of driver compartment
        self.num_vestibles = num_vestibles #number of vestibles on this carriage, will be two for all the vehicles we have
        self.vestible = vestible #type of vestible found in this carriage
        self.num_saloons = num_saloons #number of saloons on this carriage, will be two for normal carriages, one for driving carriages
        self.saloon = saloon #type of saloon found 
        #determine the total length of vestible sections
        if self.num_vestibles>0:
            self.length_vestibles = self.vestible.length*self.num_vestibles
        else:
            self.length_vestibles = 0
        #determine the total length of saloon sections
        if self.num_saloons>0:
            self.length_saloons = self.saloon.length*self.num_saloons
        else:
            self.length_saloons = 0
        self.remaining_length = self.passenger_section_length-self.length_vestibles-self.length_saloons #remaining length for seating/decks

#carriage with one levels (single-deck)
class SingleDeckCarriage(Carriage):
    def __init__(self,carriage_outer,carriage_inner,gangway,num_gangways,driver_compartment,vestible,num_vestibles,num_saloons,saloon):
        Carriage.__init__(self,carriage_outer,carriage_inner,gangway,num_gangways,driver_compartment,vestible,num_vestibles,num_saloons,saloon)
        

#carriage with two levels (double-deck)    
class DoubleDeckCarriage(Carriage):
    def __init__(self,carriage_outer,carriage_inner,gangway,num_gangways,driver_compartment,vestible,num_vestibles,num_saloons,saloon,double_deck):
        Carriage.__init__(self,carriage_outer,carriage_inner,gangway,num_gangways,driver_compartment,vestible,num_vestibles,num_saloons,saloon)
        #note in double deck formation, floor and ceiling height is the height of the centre section
        self.double_deck = double_deck #geometry of the double deck section
        self.levels_and_stairs() #calculate parameters of the upper and lower decks and the stairs leading up to them

    #calculate parameters of stairs and levels
    def levels_and_stairs(self):
        self.lower_stairs_height = self.carriage_inner.floor_height-self.double_deck.lower_floor_height #how much do the stairs to the lower deck descend 
        self.upper_stairs_height = self.double_deck.upper_floor_height-self.carriage_inner.floor_height #how much do the stairs to the upper deck rise
        self.lower_stairs_length = self.lower_stairs_height * (1/self.double_deck.stair_grade) #length of the stairs to the lower deck
        self.upper_stairs_length = self.upper_stairs_height * (1/self.double_deck.stair_grade) #length of the stairs to the upper deck
        self.upper_deck_length = self.remaining_length-self.upper_stairs_length*2 #length of the upper deck, metres
        self.lower_deck_length = self.remaining_length-self.lower_stairs_length*2 #length of the lower deck, metres

#example components
driver_compartment = DriverCompartment(length=3,triangle_grade=0.5,ceiling_height=2.1)
passenger = Passenger(mean_weight=80,design_weight=100,design_density=6)
#http://www.gbspecialprojects.co.uk/bus-coach-seats.php, guide for seat weights  
city_seat_fixed = Seat(length=0.8,width=0.5,weight=11,reversible=False,direction='forward')
city_seat = Seat(length=0.8,width=0.5,weight=14,reversible=True,direction='forward')
city_side_seat = Seat(length=0.7,width=0.5,weight=11,reversible=False,direction='side')
country_seat_fixed = Seat(length=0.9,width=0.6,weight=21,reversible=False,direction='forward')
country_seat_reversible = Seat(length=0.9,width=0.6,weight=25,reversible=True,direction='forward')
gangway = Gangway(length=0.25,width=1.4,height=2.1)
vestible = Vestible(doorway_width=2.4,extra_width=0.4)
saloon = Saloon(length=2)
carriage_exterior_single = CarriageOuterGeometry(length=20,width=3,roof_height=3.7,triangle_height=3.3,triangle_width=1.5) 
carriage_exterior_double = CarriageOuterGeometry(length=20,width=3,roof_height=4.4,triangle_height=4,triangle_width=1.5) 
carriage_interior = CarriageInnerGeometry(floor_height=1.3,ceiling_height=2.1)
double_deck = DoubleDeckGeometry(lower_floor_height=0.5,lower_ceiling_height=1.8,interstage_height=0.1,upper_ceiling_height=1.8,stair_grade=1,stair_width=1,stair_seats_lost=1)
single_deck_centre = SingleDeckCarriage(carriage_exterior_single,carriage_interior,gangway=gangway,num_gangways=2,driver_compartment=0,num_vestibles=2,vestible=vestible,num_saloons=2,saloon=saloon)
double_deck_centre = DoubleDeckCarriage(carriage_exterior_double,carriage_interior,gangway=gangway,num_gangways=2,driver_compartment=0,num_vestibles=2,vestible=vestible,num_saloons=2,saloon=saloon,double_deck=double_deck)
single_deck_driving = SingleDeckCarriage(carriage_exterior_single,carriage_interior,gangway=gangway,num_gangways=1,driver_compartment=driver_compartment,num_vestibles=2,vestible=vestible,num_saloons=1,saloon=saloon)
double_deck_driving = DoubleDeckCarriage(carriage_exterior_double,carriage_interior,gangway=gangway,num_gangways=1,driver_compartment=driver_compartment,num_vestibles=2,vestible=vestible,num_saloons=1,saloon=saloon,double_deck=double_deck)