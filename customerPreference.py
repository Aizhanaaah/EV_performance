class mechanicalPerformance:
    def __init__(self, engine_size, transmission, drive_type):
        self.engine_size = engine_size
        self.transmission = transmission
        self.drive_type = drive_type

class fuel_efficiency:
    def __init__(self, mpg_l, ev_range, fuel_type):
        self.mpg_l = mpg_l
        self.ev_range = ev_range
        self.fuel_type = fuel_type

class maintenance:
    def __init__(self, repair_cost, spareParts_availability, service_history):
        self.repair_cost = repair_cost
        self.spareParts_availability = spareParts_availability
        self.service_history = service_history

class interior:
    def __init__(self, seat_quality_vs_adjustablility, infotainment_system, climate_control):
        self.seat_quality_vs_adjustablity = seat_quality_vs_adjustablility
        self.infotainment_system = infotainment_system
        self.climate_control = climate_control

class costVSvalue:
    def __init__(self, price, insurance_cost, taxes, resale_value):
        self.price = price
        self.insurance_cost = insurance_cost
        self.taxes = taxes
        self.resale_value = resale_value

class environmentalImpact:
    def __init__(self, CO2emissions, EVincentives):
        self.CO2emissions = CO2emissions
        self.EVincentives = EVincentives
        self.CO2emissions_total = self.CO2emissions * self.EVincentives
