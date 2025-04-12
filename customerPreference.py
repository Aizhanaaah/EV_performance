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
