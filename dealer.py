# Overdue

# The problems to be solved:
# 1. Figure out a mechanism to replace an older value with a new value (ex. replace non-promo rate with promo rate).
# 2. Work on a list of maintenance.
import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

# time_diff = datetime.datetime(2019, 7, 14) - datetime.datetime(2016, 7, 14)
# difference_in_years = relativedelta(datetime.datetime(2016, 7, 14), datetime.datetime(2019, 7, 14)).years
# print(difference_in_years)
# print(datetime.date.today())


freight = 30000.0
pre_delivery_inspection = 110000.0

class Dealer:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.listings = []
        self.used_listings = []

    def __repr__(self):
        return "%s, %s, %s." % (self.name, self.address, self.phone_number)

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, sold_listing):
        self.listings.remove(sold_listing)

    def add_used_listing(self, new_used_listing):
        self.used_listings.append(new_used_listing)

    def remove_used_listing(self, sold_used_listing):
        self.used_listings.remove(sold_used_listing)
        
dealer_1 = Dealer("Toyota Mobility Chiyoda", "2-1-4 Uchi-Kanda, Chiyoda District, Tokyo, Tokyo, Japan 101-0047", "+81-3-3256-5351")

class Client:
    def __init__(self, name, is_buyer, is_seller, drivers_license_date, drivers_license_color, incident_record):
        self.name = name
        self.is_buyer = is_buyer
        self.is_seller = is_seller
        self.drivers_license_date = drivers_license_date
        self.drivers_license_color = drivers_license_color
        self.incident_record = incident_record
        
    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s." % (self.name, self.is_buyer, self.is_seller, self.drivers_license_date, self.drivers_license_color, self.incident_record)
    
    def get_driver_license_date(self):
        return self.drivers_license_date
    
    def get_driver_license_color(self):
        return self.drivers_license_color
    
    def get_incident_record(self):
        return self.incident_record
    
    def driving_age(self):
        self.da = relativedelta(self.drivers_license_date, datetime.date.today()).years
        return self.da
    
    def sell_car(self, used_vehicle):
        if self.is_seller == True:
            if used_vehicle.owner == self:
                new_used_listing = UsedVehicleListing(used_vehicle, self)
                dealer_1.add_used_listing(new_used_listing)
        else:
            dealer_1.add_used_listing(new_used_listing)
    
    def buy_car(self, vehicle):
        if self.is_buyer == True:
           dealer_listing = None
           for listing in dealer_1.listings:
                if listing.vehicle == vehicle:
                    dealer_listing = listing
                    break
                if dealer_listing != None:
                    dealer_listing.vehicle.owner = self
                    dealer_1.remove_listing(dealer_listing)
    
    def buy_used_car(self, used_vehicle):
        if self.is_buyer == True:
            dealer_used_listing = None
            for listing in dealer_1.used_listings:
                if listing.used_vehicle == used_vehicle:
                    dealer_used_listing = listing
                break
            if dealer_used_listing != None:
                dealer_used_listing.used_vehicle.owner = self
                dealer_1.remove_listing(dealer_used_listing)

sato = Client("Sato", False, True, datetime.datetime(1997, 3, 29), "Gold", False)
matsumoto = Client("Matsumoto", False, True, datetime.datetime(2010, 7, 13), "Blue", True)
takahashi = Client("Takahashi", True, False, datetime.datetime(2019, 1, 24), "Green", False)

class Vehicle:
    def __init__(self, year, make, model, trim, displacement, weight, carbon_emission, color, price, discount, end_date):
        self.year = year
        self.make = make
        self.model = model
        self.trim = trim
        self.displacement = displacement
        self.weight = weight
        self.carbon_emission = carbon_emission
        self.color = color
        self.price = price
        self.discount = discount
        self.end_date = end_date
        self.tax_amount = 0.0
    
    def __repr__(self):
        if self.discount > 0.0:
            return "This vehicle has a ¥%s discount by the end of %s." % (self.discount, self.end_date.date)
        return "{year} {make} {model} {trim}, {displacement}, {weight}, {carbon_emission}, {color}, ¥{price}."
    
    def environment_tax(self):
        if self.carbon_emission != "N/A":
            carbon_emission_value = int(self.carbon_emission.strip("g/km"))
            if carbon_emission_value < 100:
                self.et = 20000.0
            elif (carbon_emission_value >= 100) and (carbon_emission_value < 150):
                self.et = 30000.0
            elif (carbon_emission_value >= 150) and (carbon_emission_value < 200):
                self.et = 50000.0
            elif (carbon_emission_value >= 200) and (carbon_emission_value < 250):
                self.et = 70000.0
            elif (carbon_emission_value >= 250) and (carbon_emission_value < 300):
                self.et = 100000.0
            else:
                self.et = 160000.0
        else:
            self.et = 0.0
        return self.et
    
    def weight_tax(self, price):
        if self.weight != "N/A":
            weight_value = int(self.weight.strip("kg"))
            if weight_value < 700:
                self.wt = float(self.price) * 0.005
            elif (weight_value >= 700 ) and (weight_value < 1200):
                self.wt = float(self.price) * 0.007
            elif (weight_value >= 1200) and (weight_value < 1600):
                self.wt = float(self.price) * 0.01
            elif (weight_value >= 1600) and (weight_value < 2000):
                self.wt = float(self.price) * 0.015
            else:
                self.wt = float(self.price) * 0.025
        return self.wt
    
    def displacement_tax(self):
        if float(self.displacement) < 0.7:
            self.dt = 18000.0
        elif (float(self.displacement) >= 0.7) and (float(self.displacement) < 1.3):
            self.dt = 27500.0
        elif (float(self.displacement) >= 1.3) and (float(self.displacement) < 2.0 ):
            self.dt = 44500.0
        elif (float(self.displacement) >= 2.0 ) and (float(self.displacement) < 2.5 ):
            self.dt = 64000.0
        elif (float(self.displacement) >= 2.5 ) and (float(self.displacement) < 3.0 ):
            self.dt = 90000.0
        elif (float(self.displacement) >= 3.0 ) and (float(self.displacement) < 4.0 ):
            self.dt = 128000.0
        else:
            self.dt = 210000.0
        return self.dt
   
    def apply_discount(self):
        if self.discount > 0.0:
            self.price = self.price - self.discount
            return self.price
    
    def total_tax_amount(self):
        self.tax_amount = self.environment_tax() + self.weight_tax(self.price) + self.displacement_tax()
        return self.tax_amount
    
    def total_price(self):
        self.price_total = self.total_tax_amount() + float(self.price) + float(freight) + float(pre_delivery_inspection)
        return self.price_total

gr_supra_rz = Vehicle("2020", "Toyota", "GR Supra", "RZ", "3.0", "1540kg", "170g/km", "Red", "7027778", None, None)
corolla_sport1 = Vehicle("2020", "Toyota", "Corolla Sport", "HYBRID G", "1.8", "1370kg", "83g/km", "White", "2659800", None, None)
alphard_hybrid_sr_c_pack = Vehicle("2020", "Toyota", "Alphard", "HYBRID SR C Package 7-seater", "2.5", "2190kg", "N/A", "White", "5654000", None, None)

class NewVehicleListing:
    def __init__(self, vehicle, seller=Dealer):
        self.vehicle = vehicle
        self.seller = seller
    
    def __repr__(self):
        return "%s %s %s %s, %s." % (self.vehicle.year, self.vehicle.make, self.vehicle.model, self.vehicle.trim, self.seller)

dealer_1_inventory = NewVehicleListing(gr_supra_rz, dealer_1)
print(dealer_1_inventory)

class UsedVehicle(Vehicle):
    def __init__(self, year, make, model, trim, displacement, weight, carbon_emission, color, price, discount, end_date, condition, mileage, owner):
        super().__init__(year, make, model, trim, displacement, weight, carbon_emission, color, price, discount, end_date)
        self.condition = condition
        self.mileage = mileage
        self.owner = owner
    
    def __repr__(self):
        return "{year} {make} {model} {trim}, {displacement}, {weight}, {carbon_emission}, {color}, \
            ¥{price}, {condition}, {mileage}, {owner}.".format(year=self.year, make=self.make, \
                model=self.model, trim=self.trim, displacement=self.displacement, weight=self.weight, \
                    carbon_emission=self.carbon_emission, color=self.color, price=self.price, condition=self.condition, \
                        mileage=self.mileage, owner=self.owner)

supra_jza80 = UsedVehicle("1997", "Toyota", "Supra", "RZ", "3.0", "1570kg", "N/A", "Silver", "4005000", None, None, "mint", "140000km", dealer_1)
matsumotos_car = UsedVehicle("2007", "Toyota", "Prius", "S 10th Anniversary Edition", "1.5", "1317kg", "N/A",\
     "Silver", "444000", None, None, "mint", "58000km", matsumoto)


class UsedVehicleListing:
    def __init__(self, used_vehicle, client):
        self.used_vehicle = used_vehicle
        self.client = client
    
    def __repr__(self):
        return "%s %s %s %s, %s." % (self.used_vehicle.year, self.used_vehicle.make, self.used_vehicle.model, \
            self.used_vehicle.trim, self.used_vehicle.owner)

dealer_1_used_inventory = UsedVehicleListing(supra_jza80, dealer_1)
matsumoto.sell_car(matsumotos_car)

class Part:
    def __init__(self, name, vehicle_for_use, status, use, price, labour_hours):
        self.name = name
        self.vehicle_for_use = vehicle_for_use
        self.status = status
        self.use = use
        self.price = price
        self.labour_hours = labour_hours
   
    def __repr__(self):
        return "%s for %s, %s, %s, ¥%s, %s." % (self.name, self.vehicle_for_use, self.status, self.use, self.price, self.labour_hours)          
    
    def get_price(self):
        return float(self.price)
    
    def get_labour_hours(self):
        return self.labour_hours

gr_al_wheel = Part("GR 19-inch forged aluminum wheel", gr_supra_rz, "In stock", "Manufacturer Option", "704000", None)
alphard_bumper = Part("Front Bumper", alphard_hybrid_sr_c_pack, "In Stock", "Stock", "136900", 3.0)
 
class Insurance:

    def __init__(self, comprehensive_coverage, third_party_liability, collision, deductable, pedestrian_injury, client):
        self.comprehensive_coverage = comprehensive_coverage
        self.third_party_liability = third_party_liability
        self.collision = collision
        self.deductable = deductable
        self.pedestrian_injury = pedestrian_injury
        self.client = client
        self.price = 0.0

    def policy_premium_pricing(self):
        if self.comprehensive_coverage == True:
            self.price += 20000.0
        if self.third_party_liability == "100000000":
            self.price += 60000.0
        if self.third_party_liability == "200000000":
            self.price += 80000.0
        if self.collision == True:
            self.price += 50000.0
        if self.deductable == "45000":
            self.price += 30000.0
        if self.deductable == "75000":
            self.price += 40000.0
        if self.pedestrian_injury == True:
            self.price += 40000.0
        if self.client.get_driver_license_color() == "Green":
            if (self.client.driving_age() < 0) and (self.client.driving_age() > -3):
                self.price = self.price * (1.12 + float(self.client.driving_age()) * 0.01)
        if self.client.get_driver_license_color() == "Blue":
            if (self.client.driving_age() <= -3) and (self.client.driving_age() > -25):
                self.price = self.price * (0.98 + float(self.client.driving_age()) * 0.015)
        if self.client.get_driver_license_color() == "Gold":
            if (self.client.driving_age() <= -6) and (self.client.driving_age() > -25):
                self.price = self.price * (0.80 + float(self.client.driving_age()) * 0.018)
        if self.client.get_incident_record() == True:
            self.price = self.price * 1.28
        return self.price

ins_option_1 = Insurance(True, "100000000", True, "45000", True, takahashi)
ins_option_1_price = ins_option_1.policy_premium_pricing()
print(ins_option_1_price)

class Warranty:

    def __init__(self, component, year, mileage):
        self.component = component
        self.year = year
        self.mileage = mileage

    def __repr__(self):
        return "The warranty for {component} is {year} years or {mileage}km, whichever comes earlier.". \
            format(component=self.component, year=self.year, mileage=self.mileage)
    
    def get_year(self):
        return self.year
   
    def get_mileage(self):
        return self.mileage

engine_warranty = Warranty("engine", "5", "100000")
whole_car_warranty = Warranty("whole_vehicle", "3", "60000")

class WarrantyList:
    def __init__(self, warranty):
        self.warranty = warranty
    
    def __repr__(self):
        return "%s, %s or %s." % (self.warranty.component, self.warranty.year, self.warranty.mileage)

warranty_list1 = WarrantyList(whole_car_warranty)

class Finance:
    def __init__(self, loan_apr, loan_term, loan_down_pay_rate, price, bonus, end_date):
        self.loan_apr = loan_apr
        self.loan_term = loan_term
        self.loan_down_pay_rate = loan_down_pay_rate
        self.price = price
        self.bonus = bonus
        self.end_date = end_date
   
    def __repr__(self):
        if self.end_date != None:
            return "This finance option will end at %s." % (self.end_date)
    
    def get_loan_apr(self):
        return self.loan_apr
    
    def get_loan_term(self):
        return self.loan_term
    
    def apply_bonus(self):
        if self.bonus > 0.0:
            self.price = self.price - self.bonus
        return self.price
   
    def get_loan_down_pay_rate(self):
        return self.loan_down_pay_rate
   
    def down_payment(self, price, loan_down_pay_rate):
        self.dp = self.price * self.loan_down_pay_rate
        return self.dp
    
    def monthly_installment(self, price):
        self.mi = (self.price - self.dp) * ((self.loan_apr / 1200.0) * (1.0 + self.loan_apr / 1200.0) ** \
            self.loan_term) / (((1.0 + self.loan_apr / 1200.0) ** self.loan_term) - 1.0)
        return self.mi
    

finance_op1 = Finance(4.8, 60.0, 0.30, gr_supra_rz.total_price(), None, None)
finance_op2 = Finance(1.99, 60.0, 0.0, corolla_sport1.total_price(), 150000.0, datetime.datetime(2020, 3, 31, 23, 59))
print(gr_supra_rz.total_price())
dp1 = finance_op1.down_payment(gr_supra_rz.total_price(), 0.30)
mi1 = finance_op1.monthly_installment(gr_supra_rz.total_price())
print(dp1)
print(mi1)

class Lease:
    def __init__(self, lease_apr, lease_term, lease_down_pay_rate, lease_residual_value_ratio, price, annual_mileage_allowance, bonus, end_date):
        self.lease_apr = lease_apr
        self.lease_term = lease_term
        self.lease_down_pay_rate = lease_down_pay_rate
        self.lease_residual_value_ratio = lease_residual_value_ratio
        self.price = price
        self.annual_mileage_allowance = annual_mileage_allowance
        self.bonus = bonus
        self.end_date = end_date
    
    def __repr__(self):
        if self.end_date != None:
            return "This lease option will end at %s." % (self.end_date)
    
    def get_lease_apr(self):
        return self.lease_apr
    
    def get_lease_term(self):
        return self.lease_term
    
    def get_lease_down_pay_rate(self):
        return self.lease_down_pay_rate
    
    def get_lease_residual_value_ratio(self):
        return self.lease_residual_value_ratio
    
    def apply_bonus(self):
        if self.bonus > 0.0:
            self.price = self.price - self.bonus
        return self.price
    
    def down_payment(self, price, lease_down_pay_rate):
        self.lease_dp = float(self.price) * self.lease_down_pay_rate
        return self.lease_dp
    
    def capitalized_cost(self, price):
        self.cc = self.price - self.lease_dp
        return self.cc
    
    def residual_value(self, price, lease_residual_value_ratio, annual_mileage_allowance):
        self.lease_rv = self.price * self.lease_residual_value_ratio
        if self.annual_mileage_allowance >= 24000.0:
            self.lease_rv = self.price * self.lease_residual_value_ratio - (self.annual_mileage_allowance - 24000.0) * 15.0
        return self.lease_rv
    
    def money_factor(self, lease_apr):
        self.mf = self.lease_apr / 2400.0
        return self.mf
    
    def monthly_depreciation_payment(self, cc, lease_rv, lease_term):
        self.mdp = (self.cc - self.lease_rv) / self.lease_term
        return self.mdp
    
    def monthly_financial_charges(self, cc, lease_rv, mf):
        self.mfc = (self.cc + self.lease_rv) * self.mf
        return self.mfc
    
    def monthly_payment(self):
        self.mp = self.mdp + self.mfc
        return self.mp

lease_op1 = Lease(4.8, 60.0, 0.25, 0.34, gr_supra_rz.total_price(), 24025.0, None, None)
lease_op2 = Lease(1.99, 72.0, 0.0, 0.409, corolla_sport1.total_price(), 20000.0, 75000.0, datetime.datetime(2020, 3, 31, 23, 59))
gr_dp_lease = lease_op1.down_payment(gr_supra_rz.total_price(), 0.25)
gr_rv = lease_op1.residual_value(gr_supra_rz.total_price(), 0.34, 24025.0)
gr_mf = lease_op1.money_factor(4.8)
gr_mdp = lease_op1.monthly_depreciation_payment(lease_op1.capitalized_cost(gr_supra_rz.total_price()), gr_rv, 60.0)
gr_mfc = lease_op1.monthly_financial_charges(lease_op1.capitalized_cost(gr_supra_rz.total_price()), gr_rv, gr_mf)
gr_mp = lease_op1.monthly_payment()
print(gr_dp_lease)
print(gr_rv)
print(gr_mf)
print(gr_mp)

class Maintenance:
    def __init__(self, name, price, labour_hours, first_service_mileage, subsequent_service_mileage):
        self.name = name
        self.price = price
        self.labour_hours = labour_hours
        self.first_service_mileage = first_service_mileage
        self.subsequent_service_mileage = subsequent_service_mileage
   
    def __repr__(self):
        return """{name}, ¥{price}, {labour_hours} human hours needed for maintenance.
        First service at {first_service_mileage}kms and subsequent service for every {subsequent_service_mileage}kms.""". \
            format(name=self.name, price=self.price, labour_hours=self.labour_hours, first_service_mileage=self.first_service_mileage, \
                subsequent_service_mileage=self.subsequent_service_mileage)
    
    def get_labour_hours(self):
        return self.labour_hours
    
    def get_first_service_mileage(self):
        return self.first_service_mileage
   
    def get_subsequent_service_mileage(self):
        return self.subsequent_service_mileage
    
    def get_pricing(self):
        return self.price
    

service1 = Maintenance("Service 1", str(int(50455.0)), str(3.0), str(int(8000.0)), str(int(16000.0)))
service2 = Maintenance("Service 2", str(int(63799.0)), str(4.0), str(int(16000.0)), str(int(32000.0)))
service3 = Maintenance("Service 3", str(int(82288.0)), str(5.0), str(int(32000.0)), str(int(32000.0)))
brake_fluid_replacement = Maintenance("Brake Fluid Replacement", str(int(23920.0)), str(1.5), str(int(48000.0)), str(int(48000.0)))
engine_coolant_replacement = Maintenance("Engine Coolant Replacement", str(int(47673.0)), str(2.0), str(int(160000.0)), str(int(160000.0)))
spark_plug_replacement = Maintenance("Spark Plug Replacement", str(int(38772.0)), str(int(2.0)), str(int(200000.0)), str(int(200000.0)))
list_of_regular_service = [service1, service2, service3] 
list_of_regular_replacement = [brake_fluid_replacement, engine_coolant_replacement, spark_plug_replacement]
print(list_of_regular_service[1+1])


class Repair:
    def __init__(self, customer_look_for_service, mileage, part, warranty, date_of_purchase, date_of_repair):
        self.customer_look_for_service = customer_look_for_service
        self.mileage = mileage
        self.part = part
        self.warranty = warranty
        self.date_of_purchase = date_of_purchase
        self.date_of_repair = date_of_repair
        self.labour_hours = 0.0
        self.price = 0.0
    
    def making_repair(self, customer_look_for_service):
        if self.part.status == "Out of stock":
            print("Part out of stock.")
        self.labour_hours += float(self.part.labour_hours)
        if self.part.status == "In Stock":
            if (float(self.mileage) < float(self.warranty.get_mileage())) and (self.date_of_purchase > \
                (self.date_of_repair + relativedelta(year=-int(self.warranty.get_year())))):
                self.part.price = 0.0
                self.price += float(self.part.labour_hours) * 10454.0
            else:
                if (float(self.part.get_labour_hours()) != None) and (float(Part.get_labour_hours) > 0.0):
                    self.price += float(self.part.price) + float(self.part.labour_hours) * 10454.0
        return self.labour_hours, self.price

makoto_repair = Repair("Makoto", "58000", alphard_bumper, whole_car_warranty, datetime.date(2017, 12, 18), datetime.date.today())
delta1 = makoto_repair.date_of_repair+relativedelta(years=-3)
print(delta1)

class VehicleMaintenance:
    def __init__(self, customer, current_mileage, serviced_before, parts_replaced_before, last_service_mileage, last_reg_part_replacement):
        self.customer = customer
        self.current_mileage = current_mileage
        self.serviced_before = serviced_before
        self.parts_replaced_before = parts_replaced_before
        self.last_service_mileage = last_service_mileage 
        self.last_reg_part_replacement = last_reg_part_replacement
        self.price = 0.0
        self.labour_hours = 0.0
        self.content_of_last_replacement = []
        self.recommended_maintenance = []
    
    def get_mileage_between_service(self):
        if self.serviced_before == True:
            self.mileage_between_service = self.current_mileage - self.last_service_mileage
        return self.mileage_between_service
    
    def get_last_reg_part_replacement(self):
        if self.parts_replaced_before == True:
            self.mileage_between_reg_part_replacement = self.current_mileage - self.last_reg_part_replacement
        return self.mileage_between_reg_part_replacement
    
    def get_content_of_last_replacement(self):
        for i in range(0, len(list_of_regular_replacement)):
            for j in range(0, 999):
                if (float(self.last_service_mileage) > j * float(list_of_regular_replacement[i].subsequent_service_mileage())) \
                    and (float(self.last_service_mileage) < (j + 1) * float(list_of_regular_replacement[i].subsequent_service_mileage())):
                    self.content_of_last_replacement.append(list_of_regular_replacement[i])
                    break
        return self.content_of_last_replacement
    
    def determine_service_content(self):
        if self.serviced_before == False:
            for i in range(0, len(list_of_regular_service)):
                if (float(self.current_mileage) - float(list_of_regular_service[i].get_first_service_mileage()) > 0.0) and \
                    (float(self.current_mileage) - float(list_of_regular_service[i+1].get_first_service_mileage()) < 0.0):
                    self.recommended_maintenance.append(list_of_regular_service[i])
                else:
                    self.recommended_maintenance.append(list_of_regular_service[2])
                    break

        if (self.serviced_before == True) and (float(self.current_mileage) >= 8000.0):
            if float(self.mileage_between_service) >= 8000.0:
                for i in range(0, len(list_of_regular_service)):
                    for j in range(0, 99):
                        if (((float(self.current_mileage) - float(list_of_regular_service[i].get_first_service_mileage())) // \
                            j * float(list_of_regular_service[i].get_subsequent_service_mileage())) == 1) \
                            and ((float(self.current_mileage) - float(list_of_regular_service[i].get_first_service_mileage()) // \
                            (j + 1) * float(list_of_regular_service[i].get_subsequent_service_mileage())) == 0):
                            if (float(self.current_mileage) - (float(list_of_regular_service[i].get_first_service_mileage()) + \
                                j * float(list_of_regular_service[i].get_subsequent_service_mileage())) > 0.0) and \
                                (float(self.current_mileage) - (float(list_of_regular_service[i].get_first_service_mileage()) + \
                                j * float(list_of_regular_service[i].get_subsequent_service_mileage())) < 8000.0):    
                                self.recommended_maintenance.append(list_of_regular_service[i])
                                break

        if (self.parts_replaced_before == False):
            for i in range(0, len(list_of_regular_replacement)):
                if (float(self.current_mileage) > float(list_of_regular_replacement[i].get_first_service_mileage())):
                    self.recommended_maintenance.append(list_of_regular_replacement[i])
                    break

        if self.parts_replaced_before == True:
            for i in range(0, len(list_of_regular_replacement)):
                if (float(self.current_mileage) > float(list_of_regular_replacement[i].get_first_service_mileage())) \
                    and (list_of_regular_replacement[i] not in self.content_of_last_replacement):
                    for j in range(0, 99):
                        if ((float(self.current_mileage) // j * float(list_of_regular_replacement[i].get_subsequent_service_mileage())) == 1) and \
                            ((float(self.current_mileage) // (j + 1) * float(list_of_regular_replacement[i].get_subsequent_service_mileage())) == 0):
                            self.recommended_maintenance.append(list_of_regular_replacement[i])
                            break

        return self.recommended_maintenance
   
    def total_labour_hours(self):
        for i in range(0, len(self.recommended_maintenance)):
            self.labour_hours += float(self.recommended_maintenance[i].get_labour_hours())
            break
        return self.labour_hours
    
    def total_price(self):
        for i in range(0, len(self.recommended_maintenance)):
            self.price += float(self.recommended_maintenance[i].get_pricing())
            self.total_pricing = self.labour_hours * 10454.0 + self.price
            break
        return self.price, self.total_pricing
jack_service = VehicleMaintenance("Jack", 93443.0, True, True, 84262.0, 52019.0)            