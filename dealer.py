class Vehicle:
    def __init__(self, year, make, model, trim, displacement, weight, carbon_emission, color, price):
        self.year = year
        self.make = make
        self.model = model
        self.displacement = displacement
        self.trim = trim
        self.weight = weight
        self.carbon_emission = carbon_emission
        self.color = color
        self.price = price
    def __repr__(self):
        return "{year} {make} {model} {trim}, {displacement}, {weight}, {carbon_emission}, {color}, {price}.".format(year=self.year, make=self.make, model=self.model, trim=self.trim, displacement=self.displacement, weight=self.weight, carbon_emission=self.carbon_emission, color=self.color, price=self.price)

class used_vehicle(Vehicle):
    def __init__(self, year, make, model, trim, displacement, weight, carbon_emission, color, price, condition, mileage):
        super().__init__(year, make, model, trim, displacement, weight, carbon_emission, color, price)
        self.condition = condition
        self.mileage = mileage
    def __repr__(self):
        return "{year} {make} {model} {trim}, {displacement}, {weight}, {carbon_emission}, {color}, {price}, {condition}, {mileage}.".format(year=self.year, make=self.make, model=self.model, trim=self.trim, displacement=self.displacement, weight=self.weight, carbon_emission=self.carbon_emission, color=self.color, price=self.price, condition=self.condition, mileage=self.mileage)

class warranty:
    def __init__(self, component, year, mileage):
        self.component = component
        self.year = year
        self.mileage = mileage
    def __repr__(self):
        return "For {Vehicle.make} {Vehicle.model}, the warranty for {component} is {year} or {mileage}.".format(Vehicle.make, Vehicle.model, component=self.component, year=self.year, mileage=self.mileage)

class options:
    def __init__(self, name, vehicle_for_use, price):
        self.name = name
        self.vehicle_for_use = vehicle_for_use
        self.price = price
    def __repr__(self):
        return "{name} for {vehicle_for_use}, {price}.".format(name=self.name, vehicle_for_use=self.vehicle_for_use, price=self.price)

class tax:
    def __init__(self, price):
        self.price = Vehicle.price.strip("¥,")
    def environment_tax(self):
        if Vehicle.carbon_emission != "N/A":
            carbon_emission_value = Vehicle.carbon_emission.split("g/km")
        if carbon_emission_value < 100:
            et = 20000
        if ( carbon_emission_value >= 100 ) and ( carbon_emission_value < 150 ):
            et = 30000
        if ( carbon_emission_value >= 150 ) and ( carbon_emission_value < 200 ):
            et = 50000
        if ( carbon_emission_value >= 200 ) and ( carbon_emission_value < 250 ):
            et = 70000
        if ( carbon_emission_value >= 250 ) and ( carbon_emission_value < 300 ):
            et = 100000
        if ( carbon_emission_value >= 300 ):
            et = 160000
        return et
    def weight_tax(self, price):
        if Vehicle.weight != "N/A":
            weight_value = Vehicle.weight.split("kg")
        if weight_value < 700:
            wt = price * 0.005
        if ( weight_value >= 700 ) and ( weight_value < 1200 ):
            wt = price * 0.007
        if ( weight_value >= 1200 ) and ( weight_value < 1600 ):
            wt = price * 0.01
        if ( weight_value >= 1600 ) and ( weight_value < 2000 ):
            wt = price * 0.015
        if ( weight_value >= 2000 ):
            wt = price * 0.025
        return wt
    def displacement_tax(self):
        if Vehicle.displacement < 0.7:
            dt = 18000
        if ( Vehicle.displacement >= 0.7 ) and ( Vehicle.displacement < 1.3 ):
            dt = 27500
        if ( Vehicle.displacement >= 1.3 ) and ( Vehicle.displacement < 2.0 ):
            dt = 44500
        if ( Vehicle.displacement >= 2.0 ) and ( Vehicle.displacement < 2.5 ):
            dt = 64000
        if ( Vehicle.displacement >= 2.5 ) and ( Vehicle.displacement < 3.0 ):
            dt = 90000
        if ( Vehicle.displacement >= 3.0 ) and ( Vehicle.displacement < 4.0 ):
            dt = 128000
        if ( Vehicle.displacement >= 4.0 ):
            dt = 210000  
        return dt              

class Insurance:
    def __init__(self, comprehensive_coverage, third_party_liability, collision, deductable, pedestrian_injury):
        self.comprehensive_coverage = comprehensive_coverage
        self.third_party_liability = third_party_liability
        self.collision = collision
        self.deductable = deductable
        self.pedestrian_injury = injury
        self.price = 0
    def policy_pricing(self):
        if comprehensive_coverage == True:
            price += 20000
        if third_party_liability == 100000000:
            price += 60000
        if third_party_liability == 200000000:
            price += 80000
        if collision == True:
            price += 50000
        if pedestrian_injury == True:
            price += 70000
        return price


freight = 80000

class Listing:
    def __init__(self, Vehicle):
        self.Vehicle = Vehicle
    def __repr__(self):
        return "%s." % (self.Vehicle)

class Listing_used_vehicle:
    def __init__(self, used_vehicle):
        self.used_vehicle = used_vehicle
    def __repr__(self):
        return "%s." % (self.used_vehicle)

class inventory:
    def __init__(self):
        self.listings_vehicle = []
        self.listings_used_vehicle = []
    def add_listings(self, new_listing):
        self.listings_vehicle.append(new_listing)
    def remove_listings(self, sold_listing):
        self.listings_vehicle.remove(sold_listing)
    def add_used_listings(self, new_used_listing):
        self.listings_used_vehicle.append(new_used_listing)
    def remove_used_listings(self, sold_used_listing):
        self.listings_used_vehicle.remove(sold_used_listing)
    def show_listings(self):
        for listing in listings_vehicle:
            print(listing)
        for listing in listings_used_vehicle:
            print(listing)

pre_delivery_inspection = 140000

class part:
    def __init__(self, component, vehicle_for_use, status, price):
        self.component = component
        self.vehicle_used = vehicle_for_use
        self.status = status
        self.price = price
    def __repr__(self):
        return "{component} for {vehicle_for_use}, {status}, {price}.".format(component=self.component, vehicle_for_use=self.vehicle_for_use, status=self.status, price=self.price)

class part_listing:
    def __init__(self, part):
        self.part = part
    def __repr__(self):
        return "%s." % (self.part)

class warehouse:
    def __init__(self):
        self.stored_parts = []
    def store_parts(self, new_part):
        self.stored_parts.append(new_part)
    def remove_parts(self, sold_part):
        self.stored_parts.remove(sold_part)
    def show_warehose(self):
        for part in stored_parts:
            print(part)

class loan:
    def __init__(self, apr, term, down_payment_percentage):
        self.apr = apr
        self.term = term
        self.down_payment_percentage = down_payment_percentage
        price_to_pay = Vehicle.price.strip("¥,") + options.price.strip("¥,") + tax.environment_tax + tax.weight_tax + tax.displacement_tax + Insurance.policy_pricing + freight + pre_delivery_inspection
    def down_payment(self, price_to_pay):
        dp = self.down_payment_percentage * price_to_pay 
        return dp
    def monthly_installments(self, apr, term, price_to_pay):
        mi = (price_to_pay * ((1 + apr) ** (term / 12)) - down_payment) / term
        return mi

class lease:
    def __init__(self, apr, term, down_payment_percentage, residual_value_percentage):
        self.apr = apr
        self.term = term
        self.down_payment_percentage = down_payment_percentage
        self.residual_value_percentage = residual_value_percentage
        price_to_pay = Vehicle.price.strip("¥,") + options.price.strip("¥,") + tax.environment_tax + tax.weight_tax + tax.displacement_tax + Insurance.policy_pricing + freight + pre_delivery_inspection
    def down_payment(self, price_to_pay):
        dp = self.down_payment_percentage * price_to_pay
        return dp
    def residual_value(self, price_to_pay):
        rv = self.residual_value_percentage * price_to_pay
        return rv
    def monthly_payment(self, apr, term, price_to_pay):
        mp = (price_to_pay * ((1 + apr) ** (term / 12)) - down_payment - residual_value) / term
        return mp

class dealership:
    def __init__(self, name, make, address, phone_number):
        self.name = name
        self.make = make
        self.address = address
        self.phone_number = phone_number
    def __repr__(self):
        return "{name}, your reliable {make} dealer located at {address}. Contact us at {phone_number} for more details about our latest deals.".format(name=self.name, make=self.make, address=self.address, phone_number=self.phone_number)

class customer:
    def __init__(self, name, location, driving_period, is_buyer):
        self.name = name
        self.driving_period = driving_period
        self.location = location
    def buy_car(self, vehicle):
        pass
        
gr_supra_rz = Vehicle(2020, "Toyota", "GR Supra", "RZ", "3.0", "1540kg", "170g/km", "Red", "¥7,027,778")
gr_yaris = Vehicle(2021, "Toyota", "GR Yaris", "GR-FOUR", "1.6", "1280kg", "N/A", "white", "¥3,690,000")
print(gr_supra_rz)
print(gr_yaris)
supra_rz_jza80 = used_vehicle(1997, "Toyota", "Supra", "RZ", "3.0", "1570kg", "N/A", "Gray", "¥4,000,500", "mint", "140,500km")
print(supra_rz_jza80)