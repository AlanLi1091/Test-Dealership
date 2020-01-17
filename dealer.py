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
    def __init__(self, year, make, model, trim, displacement, weight, carbon_emission, color, price, condition, mileage, owner):
        super().__init__(year, make, model, trim, displacement, weight, carbon_emission, color, price)
        self.condition = condition
        self.mileage = mileage
        self.owner = owner
    def __repr__(self):
        return "{year} {make} {model} {trim}, {displacement}, {weight}, {carbon_emission}, {color}, {price}, {condition}, {mileage}, {owner}.".format(year=self.year, make=self.make, model=self.model, trim=self.trim, displacement=self.displacement, weight=self.weight, carbon_emission=self.carbon_emission, color=self.color, price=self.price, condition=self.condition, mileage=self.mileage, owner=self.owner)

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

class dealership:
    def __init__(self, name, make, address, phone_number):
        self.name = name
        self.make = make
        self.address = address
        self.phone_number = phone_number
    def __repr__(self):
        return "{name}, your reliable {make} dealer located at {address}. Contact us at {phone_number} for more details about our latest deals.".format(name=self.name, make=self.make, address=self.address, phone_number=self.phone_number)

class listing(dealership):
    def __init__(self, name, make, address, phone_number, Vehicle):
        super().__init__(name, make, address, phone_number)
        self.Vehicle = Vehicle
    def __repr__(self):
        return "%s." % (self.Vehicle)

class listing_used_vehicle(dealership):
    def __init__(self, name, make, address, phone_number, used_vehicle):
        super().__init__(name, make, address, phone_number)
        self.used_vehicle = used_vehicle
    def __repr__(self):
        return "%s." % (self.used_vehicle)

class inventory(dealership):
    def __init__(self, name, make, address, phone_number):
        super().__init__(name, make, address, phone_number)
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

class part_listing(dealership):
    def __init__(self, name, make, address, phone_number, part):
        super().__init__(name, make, address, phone_number)
        self.part = part
    def __repr__(self):
        return "%s." % (self.part)

class warehouse(dealership):
    def __init__(self, name, make, address, phone_number):
        super().__init__(name, make, address, phone_number)
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
        price_to_pay = int(Vehicle.price.strip("¥,")) + int(options.price.strip("¥,")) + int(tax.environment_tax) + float(tax.weight_tax) + int(tax.displacement_tax) + int(Insurance.policy_pricing) + int(freight + pre_delivery_inspection)
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
        price_to_pay = int(Vehicle.price.strip("¥,")) + int(options.price.strip("¥,")) + int(tax.environment_tax) + float(tax.weight_tax) + int(tax.displacement_tax) + int(Insurance.policy_pricing) + int(freight + pre_delivery_inspection)
    def down_payment(self, price_to_pay):
        dp = self.down_payment_percentage * price_to_pay
        return dp
    def residual_value(self, price_to_pay):
        rv = self.residual_value_percentage * price_to_pay
        return rv
    def monthly_payment(self, apr, term, price_to_pay):
        mp = (price_to_pay * ((1 + apr) ** (term / 12)) - down_payment - residual_value) / term
        return mp

class promos:
    def __init__(self, discount, new_lease_apr, new_loan_apr, term, vehicle_applied, promotion_end_date):
        self.discount = discount
        self.new_lease_apr = new_lease_apr
        self.new_loan_apr = new_loan_apr
        self.term = term
        self.vehicle_applied = vehicle_applied
        self.promotion_end_date = promotion_end_date
    def __repr__(self):
        if discount > 0:
            return "Buying {vehicle_applied} by {promotion_end_date}, you will be getting a {discount} of discount.".format(vehicle_applied=self.vehicle_applied, promotion_end_date=self.promotion_end_date, discount=self.discount)
        if (new_lease_apr > 0) and (new_lease_apr < lease.apr):
            return "Buying {vehicle_applied} by {promotion_end_date}, you can lease your vehicle with a rate of {new_lease_apr} for {term} months.".format(vehicle_applied=self.vehicle_applied, promotion_end_date=self.promotion_end_date, new_lease_apr=self.new_lease_apr, installments=self.installments)
        if (new_loan_apr > 0) and (new_loan_apr < loan.apr):
            return "Buying {vehicle_applied} by {promotion_end_date}, you can finance your vehicle with a rate of {new_loan_apr} for {term} months.".format(vehicle_applied=self.vehicle_applied, promotion_end_date=self.promotion_end_date, new_loan_apr=self.new_loan_apr, installments=self.installments)
    def application(self, discount, new_lease_apr, new_loan_apr):
        if discount > 0:
            price_to_pay_promo = price_to_pay - discount
        if (new_lease_apr > 0) and (new_lease_apr < lease.apr):
            lease.apr = new_lease_apr
            lease.term = term
        if (new_loan_apr > 0) and (new_loan_apr < loan.apr):
            loan.apr = new_loan_apr
            loan.term = term
        
class customer:
    def __init__(self, name, driving_period, is_buyer, is_seller, make_inquiry, model_inquiry, budget):
        self.name = name
        self.driving_period = driving_period
        self.make_inquiry = make_inquiry
        self.model_inquiry = model_inquiry
        self.budget = budget
        self.is_buyer = is_buyer
        self.is_seller = is_seller
        if is_buyer:
            pass
        elif is_seller:
            pass
        else:
            print("Visitor.")
            print("Ask us if you need help.")
    def buy_car(self, listing, model_inquiry, budget):
        for listing in inventory.listings_vehicle:
            print(listing)
        if model_inquiry not in inventory.listings_vehicle.Vehicle.model:
            print("I'm afraid we cannot process your request. Please pick a model.")
        elif budget.strip("¥,") < inventory.listings_vehicle.Vehicle.price.strip("¥,"):
            listings_vehicle_under_budget = [listing for listing in listings_vehicle if budget.strip("¥,") < inventory.listings_vehicle.Vehicle.price.strip("¥,")]
            for listing in listings_vehicle_under_budget:
                print(listing)
        else:
            inventory.remove_listings()
    def buy_used_car(self, listing, make_inquiry, model_inquiry, budget):
        for listing in inventory.listings_used_vehicle:
            print(listing)
        if make_inquiry not in inventory.listings_used_vehicle.used_vehicle.make:
            print("We do not have the brand requested in stock. Please make another choice or check back later.")
        elif model_inquiry not in inventory.listings_used_vehicle.used_vehicle.model:
            print("We do not have the model requested in stock. Please make another choice or check back later.")
        elif budget.strip("¥,") < inventory.listings_used_vehicle.used_vehicle.price.strip("¥,"):
            listings_used_vehicle_under_budget = [listing for listing in listings_used_vehicle if budget.strip("¥,") < inventory.listings_used_vehicle.used_vehicle.price.strip("¥,")]
            for listing in listings_used_vehicle_under_budget:
                print(listing)
        elif dealership.name not in inventory.listing_used_vehicle.used_vehicle.owner:
            print("We do not have this model in stock. Please go to another dealership or check back later.")
        else:
            inventory.remove_used_listings()
    def sell_car(self, used_vehicle, price):
        if used_vehicle.owner == self:
            new_used_listing = listing_used_vehicle(used_vehicle)
            inventory.add_used_listings(new_used_listing)

class service:


gr_supra_rz = Vehicle(2020, "Toyota", "GR Supra", "RZ", "3.0", "1540kg", "170g/km", "Red", "¥7,027,778")
gr_yaris = Vehicle(2021, "Toyota", "GR Yaris", "GR-FOUR", "1.6", "1280kg", "N/A", "White", "¥3,690,000")
corolla_sport_hybrid_g = Vehicle(2020, "Toyota", "Corolla Sport", "Hybrid G", "1.8", "1400kg", "83g/km", "White", "¥2,659,800")
sngwngtd = dealership("Toyota Mobility Tokyo Shinagawa Nishi Gotanda", "Toyota", "8-11-18 Nishi-Gotanda, Shinagawa, Tokyo, Tokyo, Japan 141-0031", "+81-3-3491-0141")
print(sngwngtd)
print(gr_supra_rz)
print(gr_yaris)
print(corolla_sport_hybrid_g)
supra_rz_jza80 = used_vehicle(1997, "Toyota", "Supra", "RZ", "3.0", "1570kg", "N/A", "Gray", "¥4,000,500", "mint", "140,500km", "Toyota Mobility Tokyo Shinagawa Nishi Gotanda")
print(supra_rz_jza80)