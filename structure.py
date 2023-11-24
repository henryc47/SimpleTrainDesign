#stores the factor of safety for a project
class FactorOfSafety:
    def __init__(self,static,dynamic,passenger_dynamic):
        self.static = static #static factor of safety
        self.dynamic = dynamic #base dynamic factor of safety, will need to be multiplied by fatigue for load condition and material
        self.passenger_dynamic = passenger_dynamic #higher factor of safety for passenger related dynamic loads

#stores key material properties about a structural material
class Structural_Material:
    def __init__(self,density,yield_strength,elastic_modulus):
        self.density = density #material density in kg/m^3
        self.yield_strength = yield_strength #yield strength, MPa
        self.elastic_modulus = elastic_modulus #elastic_modulus, MPa

#stores fatigue related properties about a structural material
#we design for 50 year life, 7000 hr per year service = 350'000 hr service life
#hourly load = 350'000 cycles (snow loads, roof walk load), two minute load = 10'000'000 cycles (pax load/unload)
# 30 second load = 40'000'000 cycles (acceleration/decceleration, dynamic pressure), 30 hz load = 40'000'000'000 cycles (wheels+engine components) 
class Structural_Material_Fatigue_Limit:
    def __init(self,hourly_limit,two_minute_limit,thirty_second_limit,thirty_hz_limit):
        self.hourly_limit = hourly_limit #fatigue for 350'000 cycles
        self.two_minute_limit = two_minute_limit #fatigue for 10'000'000 cycles
        self.thirty_second_limit = thirty_second_limit #fatigue for 40'000'000 cycles
        self.thirty_hz_limit = thirty_hz_limit #fatigue for 40'000'000'000 cycles

#example of structural material fatigue limits
steel_fatigue_limits = Structural_Material_Fatigue_Limit(0.5,0.45,0.44,0.42)
aluminium_fatigue_limits = Structural_Material_Fatigue_Limit(0.5,0.42,0.4,0.3)


#roof skin - responsible for supporting static pressure, dynamic pressure, snow and person walker loads. 
#Also needs to support it's own weight under gravity, minor lifting + hillclimbing as well as longitudinal and latitudinal loads 

#roof frame - supports the roof skin

#triangle side skin - same as roof skin, but on the triangle.

#triangle side frame - supports the roof frame and triangle skin.

#intra-triangle components - components inside the triangle. This includes electrical, communication, computing and AC equipment.

#intra-triangle skin - internal, responsible for supporting static pressure, it's own weight and intra-triangle components.

#triangle base frame - supports the triangle side frame, triangle internal skin and intra-triangle components

#wall skin - responsible for supporting static and dynamic pressure loads, passenger lean loads. Also need to support it's own weight. 
#may also be prudent to design for heavy pax walker loads temporary in case of derailment.

#wall glass - as wall skin, but made of glass, for passengers to view the outside world through.

#wall frame - supports the wall skin and glass

#



