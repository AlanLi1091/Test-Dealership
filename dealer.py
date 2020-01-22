#Due Saturday, Jan 25, 2020 at 0:00AM

freight = 30000
pre_delivery_inspection = 110000

class Vehicle:
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
        self.tax_amount = 0.0
    def environment_tax(self):
        if self.carbon_emission != "N/A":
            carbon_emission_value = int(self.carbon_emission.strip("g/km"))
        if carbon_emission_value < 100:
            self.et = 20000.0
        if (carbon_emission_value >= 100) and (carbon_emission_value < 150):
            self.et = 30000.0
        if (carbon_emission_value >= 150) and (carbon_emission_value < 200):
            self.et = 50000.0
        if (carbon_emission_value >= 200) and (carbon_emission_value < 250):
            self.et = 70000.0
        if (carbon_emission_value >= 250) and (carbon_emission_value < 300):
            self.et = 100000.0
        if (carbon_emission_value >= 300):
            self.et = 160000.0
        return self.et
    def weight_tax(self, price):
        if self.weight != "N/A":
            weight_value = int(self.weight.strip("kg"))
        if weight_value < 700:
            self.wt = float(self.price) * 0.005
        if (weight_value >= 700 ) and (weight_value < 1200):
            self.wt = float(self.price) * 0.007
        if (weight_value >= 1200) and (weight_value < 1600):
            self.wt = float(self.price) * 0.01
        if (weight_value >= 1600) and (weight_value < 2000):
            self.wt = float(self.price) * 0.015
        if (weight_value >= 2000):
            self.wt = float(self.price) * 0.025
        return self.wt
    def displacement_tax(self):
        if float(self.displacement) < 0.7:
            self.dt = 18000.0
        if (float(self.displacement) >= 0.7) and (float(self.displacement) < 1.3):
            self.dt = 27500.0
        if (float(self.displacement) >= 1.3) and (float(self.displacement) < 2.0 ):
            self.dt = 44500.0
        if (float(self.displacement) >= 2.0 ) and (float(self.displacement) < 2.5 ):
            self.dt = 64000.0
        if (float(self.displacement) >= 2.5 ) and (float(self.displacement) < 3.0 ):
            self.dt = 90000.0
        if (float(self.displacement) >= 3.0 ) and (float(self.displacement) < 4.0 ):
            self.dt = 128000.0
        if (float(self.displacement) >= 4.0 ):
            self.dt = 210000.0
        return self.dt
    def total_tax_amount(self):
        self.tax_amount = self.et + self.wt + self.dt
        return self.tax_amount
    def total_price(self):
        self.price_total = self.tax_amount + float(self.price) + float(freight) + float(pre_delivery_inspection)
        return self.price_total

class UsedVehicle(Vehicle):
    def __init__(self, year, make, model, trim, displacement, weight, carbon_emission, color, price, condition, mileage, owner):
        super().__init__(year, make, model, trim, displacement, weight, carbon_emission, color, price)
        self.condition = condition
        self.mileage = mileage
        self.owner = owner
    def __repr__(self):
        return "{year} {make} {model} {trim}, {displacement}, {weight}, {carbon_emission}, {color}, ¥{price}, {condition}, {mileage}, {owner}.".format(year=self.year, make=self.make, model=self.model, trim=self.trim, displacement=self.displacement, weight=self.weight, carbon_emission=self.carbon_emission, color=self.color, price=self.price, condition=self.condition, mileage=self.mileage, owner=self.owner)

class Options:
    def __init__(self, name, vehicle_for_use, price):
        self.name = name
        self.vehicle_for_use = vehicle_for_use
        self.price = price
    def __repr__(self):
        return "{name} for {vehicle_for_use}, ¥{price}.".format(name=self.name, vehicle_for_use=self.vehicle_for_use, price=self.price)          
    def get_price(self):
        return self.price

class Pricing:
    def price_addition(self):
        self.total_price_with_options = Options.get_price + Vehicle.total_price
        return self.total_price_with_options


class Insurance:
    def __init__(self, comprehensive_coverage, third_party_liability, collision, deductable, pedestrian_injury):
        self.comprehensive_coverage = comprehensive_coverage
        self.third_party_liability = third_party_liability
        self.collision = collision
        self.deductable = deductable
        self.pedestrian_injury = pedestrian_injury
        self.price = 0
    def policy_pricing(self):
        if self.comprehensive_coverage == True:
            self.price += 20000.0
        if self.third_party_liability == "100000000":
            self.price += 60000.0
        if self.third_party_liability == "200000000":
            self.price += 80000.0
        if self.collision == True:
            self.price += 50000.0
        if self.pedestrian_injury == True:
            self.price += 70000.0
        return self.price

class Warranty:
    def __init__(self, component, year, mileage):
        self.component = component
        self.year = year
        self.mileage = mileage
    def __repr__(self):
        return "The warranty for {component} is {year} years or {mileage}, whichever comes earlier.".format(component=self.component, year=self.year, mileage=self.mileage)
    def get_warranty_year(self):
        return self.year
    def get_warranty_mileage(self):
        return self.mileage

#Both Finance and Promotion classes need to be fixed and simulate real car financing situations. Need more research.
#Might need to consider merging Finance class and Promotion class into a single class, or set up Promotion class as a sub class of Finance class.

class Finance:
    def __init__(self, is_lease, is_loan, lease_apr, loan_apr, lease_term, loan_term, lease_down_pay_rate, loan_down_pay_rate):
        self.is_lease = is_lease
        self.is_loan = is_loan
        self.lease_apr = lease_apr
        self.loan_apr = loan_apr
        self.lease_term = lease_term
        self.loan_term = loan_term
        self.lease_down_pay_rate = lease_down_pay_rate
        self.loan_down_pay_rate = loan_down_pay_rate
        if is_lease:
            self.lease_apr = lease_apr
        if is_loan:
            self.loan_apr = loan_apr
    def get_lease_apr(self):
        return self.lease_apr
    def get_loan_apr(self):
        return self.loan_apr
    def get_lease_term(self):
        return self.lease_term
    def get_loan_term(self):
        return self.loan_term
    def down_payment(self, total_price_with_options):
        if self.is_lease:
            self.dp = total_price_with_options * float(self.lease_down_pay_rate)
        if self.is_loan:
            self.dp = total_price_with_options * float(self.loan_down_pay_rate)
        return self.dp
    def monthly_installment(self, total_price_with_options):
        pass

class Promotions:
    def __init__(self, discount, new_lease_apr, new_loan_apr, new_lease_term, new_loan_term, vehicle_applied, promotion_end_date):
        self.discount = discount
        self.new_lease_apr = new_lease_apr
        self.new_loan_apr = new_loan_apr
        self.new_lease_term = new_lease_term
        self.new_loan_term = new_loan_term
        self.vehicle_applied = vehicle_applied
        self.promotion_end_date = promotion_end_date
    def __repr__(self):
        if self.discount > 0:
            return "Buying {vehicle_applied} by {promotion_end_date}, you will be getting a {discount} of discount.".format(vehicle_applied=self.vehicle_applied, promotion_end_date=self.promotion_end_date, discount=self.discount)
        if (self.new_lease_apr > 0) and (self.new_lease_apr < Finance.get_lease_apr):
            return "Buying {vehicle_applied} by {promotion_end_date}, you can lease your vehicle with a rate of {new_lease_apr} for {new_lease_term} months.".format(vehicle_applied=self.vehicle_applied, promotion_end_date=self.promotion_end_date, new_lease_apr=self.new_lease_apr, new_lease_term=self.new_lease_term)
        if (self.new_loan_apr > 0) and (self.new_loan_apr < Finance.get_loan_apr):
            return "Buying {vehicle_applied} by {promotion_end_date}, you can finance your vehicle with a rate of {new_loan_apr} for {new_loan_term} months.".format(vehicle_applied=self.vehicle_applied, promotion_end_date=self.promotion_end_date, new_loan_apr=self.new_loan_apr, new_loan_term=self.new_loan_term)
    def application(self, discount, new_lease_apr, new_loan_apr, price_to_pay_after_promo):
        if self.discount > 0:
            price_to_pay_after_promo = Pricing.price_addition - self.discount
        if (self.new_lease_apr > 0) and (self.new_lease_apr < Finance.get_lease_apr):
            Finance.get_lease_apr = self.new_lease_apr
            Finance.get_lease_term = self.new_lease_term
        if (self.new_loan_apr > 0) and (self.new_loan_apr < Finance.get_loan_apr):
            Finance.get_loan_apr = self.new_loan_apr
            Finance.get_loan_term = self.new_loan_term

class Dealership:
    def __init__(self, name, make, address, phone_number):
        self.name = name
        self.make = make
        self.address = address
        self.phone_number = phone_number
        self.listings_vehicle = []
        self.listings_used_vehicle = []
    def __repr__(self):
        return "{name}, your reliable {make} dealer located at {address}. Contact us at {phone_number} for more details about our latest deals.".format(name=self.name, make=self.make, address=self.address, phone_number=self.phone_number)
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
    def show_used_listings(self):
        for listing in self.listings_used_vehicle:
            print(listing)


class NewVehicleListing:
    def __init__(self, vehicle, price, seller):
        self.vehicle = vehicle
        self.price = price
        self.seller = seller
    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s." % (self.vehicle.year, self.vehicle.make, self.vehicle.model, self.vehicle.trim, self.vehicle.color, self.price)

class UsedVehicleListing:
    def __init__(self, used_vehicle, price, seller):
        self.used_vehicle = used_vehicle
        self.price = price
        self.seller = seller
    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s." % (self.used_vehicle.year, self.used_vehicle.make, self.used_vehicle.model, self.used_vehicle.trim, self.used_vehicle.color, self.used_vehicle.condition, self.used_vehicle.mileage, self.used_vehicle.price)

class Part:
    def __init__(self, component, vehicle_used, status, price):
        self.component = component
        self.vehicle_used = vehicle_used
        self.status = status
        self.price = price
    def __repr__(self):
        return "{component} for {vehicle_used}, {status}, {price}.".format(component=self.component, vehicle_used=self.vehicle_used, status=self.status, price=self.price)
    def get_part_price(self):
        return self.price

class PartListing:
    def __init__(self, part, price):
        self.part = part
        self.price = price
    def __repr__(self):
        return "%s, %s, %s, %s." % (self.part.component, self.part.vehicle_used, self.part.status, self.part.price)

class Warehouse(Dealership):
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
    def get_stored_parts(self):
        return self.stored_parts

class CustomerBuyOrSell:
    def __init__(self, name, make_inquiry, model_inquiry, budget):
        self.name = name
        self.make_inquiry = make_inquiry
        self.model_inquiry = model_inquiry
        self.budget = budget
    def __repr__(self):
        return "{name}, buy or sell.".format(name=self.name)
    def buy_car(self, vehicle):
        pass
    def buy_used_car(self, listing, make_inquiry, model_inquiry, budget):
        pass
    def sell_car(self, used_vehicle, price):
        if used_vehicle.owner == self:
            pass

class CustomerService:
    def __init__(self, name, mileage, serviced_before, previous_services, request):
        self.name = name
        self.mileage = mileage
        self.serviced_before = serviced_before
        self.previous_services = previous_services
        self.request = request
        if serviced_before == False:
            previous_services = None
            print("This is the customer's first service")
    def __repr__(self):
        return "{name}, looking for service, {request}.".format(name=self.name, request=self.request)

class Repair(CustomerService):
    def __init__(self, name, mileage, serviced_before, previous_services, request, component_to_fix, purchase_date, repair_date):
        super().__init__(name, mileage, serviced_before, previous_services, request)
        self.component_to_fix = component_to_fix
        self.purchase_date = purchase_date
        self.repair_date = repair_date
        self.human_hours = 0
        self.price = 0
    def body(self, part):
        if (self.component_to_fix in Warehouse.get_stored_parts == True):
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
        if (self.component_to_fix in Warehouse.get_stored_parts == True):
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
                if (self.repair_date - self.purchase_date <= Warranty.get_warranty_year) or (self.mileage <= Warranty.get_warranty_mileage):
                    part.price = 0.0
                self.human_hours += 12.0
                print("We need to swap a new transmission for you.")          
        else:
            print("We need to preorder the part in order to fix your vehicle.")
    def engine(self, part):
        if (self.component_to_fix in Warehouse.get_stored_parts == True):
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
                if (self.repair_date - self.purchase_date <= Warranty.get_warranty_year) and (self.mileage <= Warranty.get_warranty_mileage):
                    part.price = 0.0
                self.human_hours += 12.0
                print("A engine swap is needed.")
        else:
            print("We need to preorder the part in order to fix your vehicle.")
    def chassis(self, part):
        if (self.component_to_fix in Warehouse.get_stored_parts == True):
            if ("brakes" in self.request == True):
                self.human_hours += 4.0
            if ("calipers" in self.request == True):
                self.human_hours += 3.0
            if ("suspension" in self.request == True):
                self.human_hours += 6.0
            if ("springs" in self.request == True):
                self.human_hours += 3.0
            if ("shock absorbers" in self.request == True):
                self.human_hours += 4.5
            if ("struts" in self.request == True):
                self.human_hours += 5.0
            if ("control arms" in self.request == True):
                self.human_hours += 4.0
            if ("sway bars" in self.request == True):
                self.human_hours += 4.0
        else:
            print("We need to preorder the part in order to fix your vehicle.")
    def interior(self, part):
        if (self.component_to_fix in Warehouse.get_stored_parts == True):
            if ("seats" in self.request == True):
                self.human_hours += 3.0
            if ("dashboard" in self.request == True):
                self.human_hours += 3.0
            if ("infotainment system" in self.request == True):
                self.human_hours += 5.0
            if ("tpms" in self.request == True):
                self.human_hours += 1.5
            if ("air conditioning" in self.request == True):
                self.human_hours += 3.0
            if ("steering wheel" in self.request == True):
                self.human_hours += 2.0
            if ("sunroof" in self.request == True):
                self.human_hours += 1.5
        else:
            print("We need to preorder the part in order to fix your vehicle.")
        return self.human_hours
    def final_pricing(self, part, human_hours):
        self.price = part.price + 5500.0 * human_hours
        return self.price

class Maintenance(CustomerService):
    def __init__(self, name, mileage, serviced_before, previous_services, request, mileage_before_service):
        super().__init__(name, mileage, serviced_before, previous_services, request)
        self.mileage_before_service = mileage_before_service
        self.price = 0.0
        self.human_hours = 0.0
    def oil_change(self, mileage_before_service):
        if (int(mileage_before_service) / 6000 >= 1) and (int(mileage_before_service) % 6000 >= 0) and (int(mileage_before_service) % 6000 <= 5999):
            self.price += Part.get_part_price
            self.human_hours += 1.0
    def brake_fluid_change(self, mileage_before_service):        
        if (int(mileage_before_service) / 20000 >= 1) and (int(mileage_before_service) % 20000 >= 0) and (int(mileage_before_service) % 20000 <= 19999):
            self.price += Part.get_part_price
            self.human_hours += 1.0
    def air_filter_change(self, mileage_before_service):
        if (int(mileage_before_service) / 12000 >= 1) and (int(mileage_before_service) & 12000 >= 0) and (int(mileage_before_service) % 12000 <= 11999):
            self.price += Part.get_part_price
            self.human_hours += 0.5    
    def wheel_alignment(self, mileage_before_service):
        if (int(mileage_before_service) / 70000 >= 1) and (int(mileage_before_service) % 70000 >= 0) and (int(mileage_before_service) % 70000 <= 69999):
            self.price += Part.get_part_price
            self.human_hours += 3.0
    def brake_replacement(self, mileage_before_service):
        if (int(mileage_before_service) / 60000 >= 1) and (int(mileage_before_service) % 60000 >= 0) and (int(mileage_before_service) % 60000 <= 59999):
            self.price += Part.get_part_price
            self.human_hours += 3.0
    def engine_replacement(self, mileage_before_service):
        if (int(mileage_before_service) / 200000 >= 1) and (int(mileage_before_service) % 200000 >= 0) and (int(mileage_before_service) % 200000 <= 199999):
            self.price += Part.get_part_price
            self.human_hours += 12.0
    def transmission_replacement(self, mileage_before_service):
        if (int(mileage_before_service) / 120000 >= 1) and (int(mileage_before_service) % 120000 >= 0) and (int(mileage_before_service) % 120000 <= 119999):
            self.price += Part.get_part_price
            self.human_hours += 8.0
