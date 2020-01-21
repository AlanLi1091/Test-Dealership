class vehicle:
    def __init__(self, year, make, model, trim, displacement, weight, carbon_emission, color, price):
        self.year = year
        self.make = make
        self.model = model
        self.trim = trim
        self.displacement = displacement
        self.weight = weight
        self.carbon_emission = carbon_emission
        self.color = color
        self.price = price
    def __repr__(self):
        return "{year} {make} {model} {trim}, {displacement}, {weight}, {carbon_emission}, {color}, {price}.".format(year=self.year, make=self.make, model=self.model, trim=self.trim, displacement=self.displacement, weight=self.weight, carbon_emission=self.carbon_emission, color=self.color, price=self.price)

class used_vehicle(vehicle):
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
        return "The warranty for {component} is {year} years or {mileage}, whichever comes earlier.".format(component=self.component, year=self.year, mileage=self.mileage)

class options:
    def __init__(self, name, vehicle_for_use, price):
        self.name = name
        self.vehicle_for_use = vehicle_for_use
        self.price = price
    def __repr__(self):
        return "{name} for {vehicle_for_use}, {price}.".format(name=self.name, vehicle_for_use=self.vehicle_for_use, price=self.price)

class tax(vehicle):
    def environment_tax(self):
        if vehicle.carbon_emission != "N/A":
            carbon_emission_value = vehicle.carbon_emission.strip("g/km")
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
        if vehicle.weight != "N/A":
            weight_value = vehicle.weight.strip("kg")
        if weight_value < 700:
            wt = vehicle.price * 0.005
        if ( weight_value >= 700 ) and ( weight_value < 1200 ):
            wt = vehicle.price * 0.007
        if ( weight_value >= 1200 ) and ( weight_value < 1600 ):
            wt = vehicle.price * 0.01
        if ( weight_value >= 1600 ) and ( weight_value < 2000 ):
            wt = vehicle.price * 0.015
        if ( weight_value >= 2000 ):
            wt = vehicle.price * 0.025
        return wt
    def displacement_tax(self):
        if vehicle.displacement < 0.7:
            dt = 18000
        if ( vehicle.displacement >= 0.7 ) and ( vehicle.displacement < 1.3 ):
            dt = 27500
        if ( vehicle.displacement >= 1.3 ) and ( vehicle.displacement < 2.0 ):
            dt = 44500
        if ( vehicle.displacement >= 2.0 ) and ( vehicle.displacement < 2.5 ):
            dt = 64000
        if ( vehicle.displacement >= 2.5 ) and ( vehicle.displacement < 3.0 ):
            dt = 90000
        if ( vehicle.displacement >= 3.0 ) and ( vehicle.displacement < 4.0 ):
            dt = 128000
        if ( vehicle.displacement >= 4.0 ):
            dt = 210000  
        return dt              

class insurance:
    def __init__(self, comprehensive_coverage, third_party_liability, collision, deductable, pedestrian_injury):
        self.comprehensive_coverage = comprehensive_coverage
        self.third_party_liability = third_party_liability
        self.collision = collision
        self.deductable = deductable
        self.pedestrian_injury = pedestrian_injury
        self.price = 0
    def policy_pricing(self):
        if self.comprehensive_coverage == True:
            self.price += 20000
        if self.third_party_liability == 100000000:
            self.price += 60000
        if self.third_party_liability == 200000000:
            self.price += 80000
        if self.collision == True:
            self.price += 50000
        if self.pedestrian_injury == True:
            self.price += 70000
        return self.price

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
    def __init__(self, name, make, address, phone_number, vehicle):
        super().__init__(name, make, address, phone_number)
        self.vehicle = vehicle
    def __repr__(self):
        return "%s." % (self.vehicle)

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
        for listing in self.listings_vehicle:
            print(listing)
        for listing in self.listings_used_vehicle:
            print(listing)

pre_delivery_inspection = 140000

class part:
    def __init__(self, component, vehicle_used, status, price):
        self.component = component
        self.vehicle_used = vehicle_used
        self.status = status
        self.price = price
    def __repr__(self):
        return "{component} for {vehicle_used}, {status}, {price}.".format(component=self.component, vehicle_used=self.vehicle_used, status=self.status, price=self.price)

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
        for part in self.stored_parts:
            print(part)

class loan:
    def __init__(self, apr, term, down_payment_percentage):
        self.apr = apr
        self.term = term
        self.down_payment_percentage = down_payment_percentage
        price_to_pay = int(vehicle.price.strip("¥")) + int(options.price.strip("¥")) + int(tax.environment_tax) + float(tax.weight_tax) + int(tax.displacement_tax) + int(insurance.policy_pricing) + int(freight + pre_delivery_inspection)
    def down_payment(self, price_to_pay):
        dp = self.down_payment_percentage * price_to_pay 
        return dp
    def monthly_installments(self, apr, term, price_to_pay):
        mi = (price_to_pay * ((1 + apr) ** (term / 12)) - self.dp) / term
        return mi

class lease:
    def __init__(self, apr, term, down_payment_percentage, residual_value_percentage):
        self.apr = apr
        self.term = term
        self.down_payment_percentage = down_payment_percentage
        self.residual_value_percentage = residual_value_percentage
        price_to_pay = int(vehicle.price.strip("¥")) + int(options.price.strip("¥")) + int(tax.environment_tax) + float(tax.weight_tax) + int(tax.displacement_tax) + int(insurance.policy_pricing) + int(freight + pre_delivery_inspection)
    def down_payment(self, price_to_pay):
        dp = self.down_payment_percentage * price_to_pay
        return dp
    def residual_value(self, price_to_pay):
        rv = self.residual_value_percentage * price_to_pay
        return rv
    def monthly_payment(self, apr, term, price_to_pay):
        mp = (price_to_pay * ((1 + apr) ** (term / 12)) - dp - rv) / term
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
        if self.discount > 0:
            return "Buying {vehicle_applied} by {promotion_end_date}, you will be getting a {discount} of discount.".format(vehicle_applied=self.vehicle_applied, promotion_end_date=self.promotion_end_date, discount=self.discount)
        if (self.new_lease_apr > 0) and (self.new_lease_apr < lease.apr):
            return "Buying {vehicle_applied} by {promotion_end_date}, you can lease your vehicle with a rate of {new_lease_apr} for {term} months.".format(vehicle_applied=self.vehicle_applied, promotion_end_date=self.promotion_end_date, new_lease_apr=self.new_lease_apr, installments=self.installments)
        if (self.new_loan_apr > 0) and (self.new_loan_apr < loan.apr):
            return "Buying {vehicle_applied} by {promotion_end_date}, you can finance your vehicle with a rate of {new_loan_apr} for {term} months.".format(vehicle_applied=self.vehicle_applied, promotion_end_date=self.promotion_end_date, new_loan_apr=self.new_loan_apr, installments=self.installments)
    def application(self, discount, new_lease_apr, new_loan_apr):
        if self.discount > 0:
            price_to_pay_promo = price_to_pay - self.discount
        if (new_lease_apr > 0) and (new_lease_apr < lease.apr):
            lease.apr = new_lease_apr
            lease.term = self.term
        if (new_loan_apr > 0) and (new_loan_apr < loan.apr):
            loan.apr = new_loan_apr
            loan.term = self.term

class customer:
    def __init__(self, name, request_at_the_desk):
        self.name = name
        self.request_at_the_desk = request_at_the_desk
    def __repr__(self):
        return "{name}, {request_at_the_desk}.".format(name=self.name, request_at_the_desk=self.request_at_the_desk)

class buy_and_sell(customer):
    def __init__(self, name, request_at_the_desk, make_inquiry, model_inquiry, budget):
        super().__init__(name, request_at_the_desk)
        self.make_inquiry = make_inquiry
        self.model_inquiry = model_inquiry
        self.budget = budget
    def buy_car(self, listing, model_inquiry, budget):
        for listing in inventory.listings_vehicle:
            print(listing)
        if self.model_inquiry not in inventory.listings_vehicle.vehicle.model:
            print("I'm afraid we cannot process your request. Please pick a model.")
        elif self.budget.strip("¥") < inventory.listings_vehicle.vehicle.price.strip("¥"):
            listings_vehicle_under_budget = [listing for listing in listings_vehicle if budget.strip("¥") < inventory.listings_vehicle.vehicle.price.strip("¥")]
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
        elif budget.strip("¥") < inventory.listings_used_vehicle.used_vehicle.price.strip("¥"):
            listings_used_vehicle_under_budget = [listing for listing in listings_used_vehicle if budget.strip("¥") < inventory.listings_used_vehicle.used_vehicle.price.strip("¥")]
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

class service(customer):
    def __init__(self, name, request_at_the_desk, mileage, serviced_before, previous_services, request):
        super().__init__(name, request_at_the_desk)
        self.mileage = mileage
        self.serviced_before = serviced_before
        self.previous_services = previous_services
        self.request = request
        if serviced_before == False:
            previous_services = None
            print("This is the customer's first service")
    def __repr__(self):
        return "{name}, {request}.".format(name=self.name, request=self.request)

class repair(service, customer):
    def __init__(self, name, request_at_the_desk, mileage, serviced_before, previous_services, request, component_to_fix, purchase_date, repair_date):
        super().__init__(name, request_at_the_desk, mileage, serviced_before, previous_services, request)
        self.component_to_fix = component_to_fix
        self.purchase_date = purchase_date
        self.repair_date = repair_date
        self.human_hours = 0
        self.price = 0
    def body(self, part):
        if (self.component_to_fix in warehouse.stored_parts == True):
            if ("front bumper" in self.request == True) or ("rear bumper" in self.request == True):
                self.human_hours += 5.0
            if "door panel" in self.request == True:
                self.human_hours += 6.0
            if "windshield" in self.request == True:
                self.human_hours += 4.0
            if ("left window" in self.request == True) or ("right window" in self.request == True):
                self.human_hours += 6.0
            if ("wheel" in self.request == True):
                self.human_hours += 3.0
            if ("need to be scrapped" in self.request == True):
                print("Sorry, we are unable to fix a totalled vehicle.")
        else:
            print("We need to preorder the part in order to fix your vehicle.")
    def transmission(self, part):
        if (self.component_to_fix in warehouse.stored_parts == True):
            if ("gearbox" in self.request == True):
                self.human_hours += 8.0
            elif ("clutch" in self.request == True):
                self.human_hours += 6.0
            elif ("differential" in self.request == True):
                self.human_hours += 6.0
            elif ("transmission fluid replacement" in self.request == True):
                self.human_hours += 1.5
            elif ("synchronizers" in self.request == True):
                self.human_hours += 6.0
            else:
                if (self.repair_date - self.purchase_date <= warranty.year) or (self.mileage <= warranty.mileage):
                    part.price = 0
                self.human_hours += 12.0
                print("We need to swap a new transmission for you.")          
        else:
            print("We need to preorder the part in order to fix your vehicle.")
    def engine(self, part):
        if (self.component_to_fix in warehouse.stored_parts == True):
            if ("spark plug" in self.request == True):
                self.human_hours += 1.0
            if ("timing belt" in self.request == True):
                self.human_hours += 1.5
            if ("alternator" in self.request == True):
                self.human_hours += 1.0
            if ("air filter" in self.request == True):
                self.human_hours += 1.0
            if ("oil filter" in self.request == True):
                self.human_hours += 1.0
            if ("exhaust pipe" in self.request == True):
                self.human_hours += 4.0
            if ("muffler" in self.request == True):
                self.human_hours += 3.0
            if ("catalytic converter" in self.request == True):
                self.human_hours += 3.0
            else:
                if (self.repair_date - self.purchase_date <= warranty.year) and (self.mileage <= warranty.mileage):
                    part.price = 0
                self.human_hours += 12.0
                print("A engine swap is needed.")
        else:
            print("We need to preorder the part in order to fix your vehicle.")
    def chassis(self, part):
        if (self.component_to_fix in warehouse.stored_parts == True):
            if ("brakes" in self.request == True):
                self.human_hours += 4
            if ("calipers" in self.request == True):
                self.human_hours += 3
            if ("suspension" in self.request == True):
                self.human_hours += 6
            if ("springs" in self.request == True):
                self.human_hours += 3
            if ("shock absorbers" in self.request == True):
                self.human_hours += 4.5
            if ("struts" in self.request == True):
                self.human_hours += 5
            if ("control arms" in self.request == True):
                self.human_hours += 4
            if ("sway bars" in self.request == True):
                self.human_hours += 4
        else:
            print("We need to preorder the part in order to fix your vehicle.")
    def interior(self, part):
        if (self.component_to_fix in warehouse.stored_parts == True):
            if ("seats" in self.request == True):
                self.human_hours += 3
            if ("dashboard" in self.request == True):
                self.human_hours += 3
            if ("infotainment system" in self.request == True):
                self.human_hours += 5
            if ("tpms" in request == True):
                self.human_hours += 1.5
            if ("air conditioning" in self.request == True):
                self.human_hours += 3
            if ("steering wheel" in self.request == True):
                self.human_hours += 2
            if ("sunroof" in self.request == True):
                self.human_hours += 1.5
        else:
            print("We need to preorder the part in order to fix your vehicle.")
        return self.human_hours
    def final_pricing(self, part, human_hours):
        price = part.price + 5500 * human_hours

class maintenance(service, customer):
    def __init__(self, name, request_at_the_desk, mileage, serviced_before, previous_services, request, mileage_before_service):
        super().__init__(name, request_at_the_desk, mileage, serviced_before, previous_services, request)
        self.mileage_before_service = mileage_before_service
        self.price = 0
        self.human_hours = 0
    def oil_change(self, mileage_before_service):
        if (int(mileage_before_service) / 6000 >= 1) and (int(mileage_before_service) % 6000 >= 0) and (int(mileage_before_service) % 6000 <= 5999):
            self.price += part.price()
            self.human_hours += 1
    def brake_fluid_change(self, mileage_before_service):        
        if (int(mileage_before_service) / 20000 >= 1) and (int(mileage_before_service) % 20000 >= 0) and (int(mileage_before_service) % 20000 <= 19999):
            self.price += part.price()
            self.human_hours += 1
    def air_filter_change(self, mileage_before_service):
        if (int(mileage_before_service) / 12000 >= 1) and (int(mileage_before_service) & 12000 >= 0) and (int(mileage_before_service) % 12000 <= 11999):
            self.price += part.price()
            self.human_hours += 0.5
    def wheel_alignment(self, mileage_before_service):
        if (int(mileage_before_service) / 70000 >= 1) and (int(mileage_before_service) % 70000 >= 0) and (int(mileage_before_service) % 70000 <= 69999):
            self.price += part.price()
            self.human_hours += 3
    def brake_replacement(self, mileage_before_service):
        if (int(mileage_before_service) / 60000 >= 1) and (int(mileage_before_service) % 60000 >= 0) and (int(mileage_before_service) % 60000 <= 59999):
            self.price += part.price()
            self.human_hours += 3
    def engine_replacement(self, mileage_before_service):
        if (int(mileage_before_service) / 200000 >= 1) and (int(mileage_before_service) % 200000 >= 0) and (int(mileage_before_service) % 200000 <= 199999):
            self.price += part.price()
            self.human_hours += 12
    def transmission_replacement(self, mileage_before_service):
        if (int(mileage_before_service) / 120000 >= 1) and (int(mileage_before_service) % 120000 >= 0) and (int(mileage_before_service) % 120000 <= 119999):
            self.price += part.price()
            self.human_hours += 8

#gr_supra_rz = vehicle("2020", "Toyota", "GR Supra", "RZ", str(3.0), "1540kg", "170g/km", "Red", "¥7027778")
#print(gr_supra_rz)
#tm_chiyoda = dealership("Toyota Mobility Chiyoda", "Toyota", "2-1-4 Uchi-Kanda, Chiyoda, Tokyo, Tokyo 101-0047", "+81-3-3256-5351")
#print(tm_chiyoda)
#supra_jza80 = used_vehicle("1997", "Toyota", "Supra", "RZ", str(3.0), "1570kg", "N/A", "Silver", "¥4005000", "mint", "120000km", tm_chiyoda.name)
#print(supra_jza80)
#engine_warranty = warranty("engine", str(5), "100000km")
#print(engine_warranty)
#trunk_spoiler = options("GR Trunk Spoiler", "GR Supra", "¥220000")
#print(trunk_spoiler)
#forged_al_wheel = part("GR 19-in forged aluminium wheel", "GR Supra", "Stock", "¥704000")
#print(forged_al_wheel)
#kazu = customer("Kazuya", "buying a car")
#print(kazu)