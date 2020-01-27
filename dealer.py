# Overdue

# The problems to be solved:
# 1. Figure out the formula for lease and finance.
# 2. Make code simpler and more accurate.

freight = 30000.0
pre_delivery_inspection = 110000.0

class Dealer:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
    def __repr__(self):
        return "%s, %s, %s." % (self.name, self.address, self.phone_number)

dealer_1 = Dealer("Toyota Mobility Chiyoda", "2-1-4 Uchi-Kanda, Chiyoda District, Tokyo, Tokyo, Japan 101-0047", "+81-3-3256-5351"
)

class Client:
    def __init__(self, name, is_buyer, is_seller):
        self.name = name
        self.is_buyer = is_buyer
        self.is_seller = is_seller
    def __repr__(self):
        return "%s, %s, %s." % (self.name, self.is_buyer, self.is_seller)

sato = Client("Sato", False, True)
matsumoto = Client("Matsumoto", False, True)

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
    def __repr__(self):
        return "{year} {make} {model} {trim}, {displacement}, {weight}, {carbon_emission}, {color}, ¥{price}, ."
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
    def total_tax_amount(self):
        self.tax_amount = self.environment_tax() + self.weight_tax(self.price) + self.displacement_tax()
        return self.tax_amount
    def total_price(self):
        self.price_total = self.total_tax_amount() + float(self.price) + float(freight) + float(pre_delivery_inspection)
        return self.price_total

gr_supra_rz = Vehicle("2020", "Toyota", "GR Supra", "RZ", "3.0", "1540kg", "170g/km", "Red", "7027778")


class NewVehicleListing:
    def __init__(self, vehicle, seller=Dealer):
        self.vehicle = vehicle
        self.seller = seller
    def __repr__(self):
        return "%s %s %s %s, %s." % (self.vehicle.year, self.vehicle.make, self.vehicle.model, self.vehicle.trim, self.seller)
dealer_1_list = NewVehicleListing(gr_supra_rz, dealer_1)
print(dealer_1_list)

class UsedVehicle(Vehicle):
    def __init__(self, year, make, model, trim, displacement, weight, carbon_emission, color, price, condition, mileage, owner):
        super().__init__(year, make, model, trim, displacement, weight, carbon_emission, color, price)
        self.condition = condition
        self.mileage = mileage
        self.owner = owner
    def __repr__(self):
        return "{year} {make} {model} {trim}, {displacement}, {weight}, {carbon_emission}, {color}, ¥{price}, {condition}, {mileage}, {owner}.".format(year=self.year, make=self.make, model=self.model, trim=self.trim, displacement=self.displacement, weight=self.weight, carbon_emission=self.carbon_emission, color=self.color, price=self.price, condition=self.condition, mileage=self.mileage, owner=self.owner)

supra_jza80 = UsedVehicle("1997", "Toyota", "Supra", "RZ", "3.0", "1570kg", "N/A", "Silver", "4005000", "mint", "140000km", dealer_1)
matsumotos_car = UsedVehicle("2007", "Toyota", "Prius", "S 10th Anniversary Edition", "1.5", "1317kg", "N/A", "Silver", "444000", "mint", "58000km", matsumoto)

class Part:
    def __init__(self, name, vehicle_for_use, for_repair, for_maintenance, for_option, price):
        self.name = name
        self.vehicle_for_use = vehicle_for_use
        self.for_repair = for_repair
        self.for_maintenance = for_maintenance
        self.for_option = for_option
        self.price = price
    def __repr__(self):
        return "%s for %s, %s, %s, %s, ¥%s." % (self.name, self.vehicle_for_use, self.for_repair, self.for_maintenance, self.for_option, self.price)          
    def get_price(self):
        return float(self.price)

gr_al_wheel = Part("GR 19-inch forged aluminum wheel", gr_supra_rz, False, False, True, "704000")
 

class Insurance:

    def __init__(self, comprehensive_coverage, third_party_liability, collision, deductable, pedestrian_injury):
        self.comprehensive_coverage = comprehensive_coverage
        self.third_party_liability = third_party_liability
        self.collision = collision
        self.deductable = deductable
        self.pedestrian_injury = pedestrian_injury
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
        return self.price

ins_option_1 = Insurance(True, "100000000", True, "45000", True)
ins_option_1_price = ins_option_1.policy_premium_pricing()
print(ins_option_1_price)

class Warranty:

    def __init__(self, component, year, mileage):
        self.component = component
        self.year = year
        self.mileage = mileage

    def __repr__(self):
        return "The warranty for {component} is {year} years or {mileage}, whichever comes earlier.".format(component=self.component, year=self.year, mileage=self.mileage)

engine_warranty = Warranty("engine", "5 year", "100000km")
whole_car_warranty = Warranty("whole_vehicle", "3 year", "60000km")

class WarrantyList:
    def __init__(self, warranty):
        self.warranty = warranty
    def __repr__(self):
        return "%s, %s or %s." % (self.warranty.component, self.warranty.year, self.warranty.mileage)

warranty_list1 = WarrantyList(whole_car_warranty)

#Both Finance and Promotion classes need to be fixed and simulate real car financing situations. Need more research.
#Might need to consider merging Finance class and Promotion class into a single class, or set up Promotion class as a sub class of Finance class.

class Finance:
    def __init__(self, loan_apr, loan_term, loan_down_pay_rate, price):
        self.loan_apr = loan_apr
        self.loan_term = loan_term
        self.loan_down_pay_rate = loan_down_pay_rate
        self.price = price
    def get_loan_apr(self):
        return self.loan_apr
    def get_loan_term(self):
        return self.loan_term
    def get_loan_down_pay_rate(self):
        return self.loan_down_pay_rate
    def down_payment(self, price, loan_down_pay_rate):
        self.dp = self.price * self.loan_down_pay_rate
        return self.dp
    def monthly_installment(self, price):
        self.mi = (self.price - self.dp) * ((self.loan_apr / 1200.0) * (1.0 + self.loan_apr / 1200.0) ** self.loan_term) / (((1.0 + self.loan_apr / 1200.0) ** self.loan_term) - 1.0)
        return self.mi
    

finance_op1 = Finance(4.8, 60.0, 0.30, gr_supra_rz.total_price())
print(gr_supra_rz.total_price())
dp1 = finance_op1.down_payment(gr_supra_rz.total_price(), 0.30)
mi1 = finance_op1.monthly_installment(gr_supra_rz.total_price())
print(dp1)
print(mi1)

class Lease:
    def __init__(self, lease_apr, lease_term, lease_down_pay_rate, lease_residual_value_ratio, price, annual_mileage_allowance):
        self.lease_apr = lease_apr
        self.lease_term = lease_term
        self.lease_down_pay_rate = lease_down_pay_rate
        self.lease_residual_value_ratio = lease_residual_value_ratio
        self.price = price
        self.annual_mileage_allowance = annual_mileage_allowance
    def get_lease_apr(self):
        return self.lease_apr
    def get_lease_term(self):
        return self.lease_term
    def get_lease_down_pay_rate(self):
        return self.lease_down_pay_rate
    def get_lease_residual_value_ratio(self):
        return self.lease_residual_value_ratio
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

lease_op1 = Lease(4.8, 60.0, 0.25, 0.34, gr_supra_rz.total_price(), 24025.0)
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

class Promotions:
    def __init__(self, discount, new_lease_apr, new_loan_apr, new_lease_term, new_loan_term, vehicle_applied, promotion_end_date):
        self.discount = discount
        self.new_lease_apr = new_lease_apr
        self.new_loan_apr = new_loan_apr
        self.new_lease_term = new_lease_term
        self.new_loan_term = new_loan_term
        self.vehicle_applied = vehicle_applied
        self.promotion_end_date = promotion_end_date
    def __repr__(self, Lease.get_lease_apr(), Finance.get_loan_apr()):
        if self.discount > 0:
            return "Buying {vehicle_applied} by {promotion_end_date}, you will be getting a {discount} of discount.".format(vehicle_applied=self.vehicle_applied, promotion_end_date=self.promotion_end_date, discount=self.discount)
        if (self.new_lease_apr > 0) and (self.new_lease_apr < Lease.get_lease_apr()):
            return "Buying {vehicle_applied} by {promotion_end_date}, you can lease your vehicle with a rate of {new_lease_apr} for {new_lease_term} months.".format(vehicle_applied=self.vehicle_applied, promotion_end_date=self.promotion_end_date, new_lease_apr=self.new_lease_apr, new_lease_term=self.new_lease_term)
        if (self.new_loan_apr > 0) and (self.new_loan_apr < Finance.get_loan_apr()):
            return "Buying {vehicle_applied} by {promotion_end_date}, you can finance your vehicle with a rate of {new_loan_apr} for {new_loan_term} months.".format(vehicle_applied=self.vehicle_applied, promotion_end_date=self.promotion_end_date, new_loan_apr=self.new_loan_apr, new_loan_term=self.new_loan_term)
    def application(self, discount, new_lease_apr, new_loan_apr, price_to_pay_after_promo):
        if self.discount > 0:
            self.price_to_pay_after_promo = Vehicle.total_price() - self.discount
            return self.price_to_pay_after_promo
        if (self.new_lease_apr > 0) and (self.new_lease_apr < Finance.get_lease_apr):
            Finance.get_lease_apr = self.new_lease_apr
            Finance.get_lease_term = self.new_lease_term
            return self.new_lease_apr, self.new_lease_term
        if (self.new_loan_apr > 0) and (self.new_loan_apr < Finance.get_loan_apr):
            Finance.get_loan_apr = self.new_loan_apr
            Finance.get_loan_term = self.new_loan_term
            return self.new_loan_apr, self.new_loan_term


class Maintenance:
    def __init__(self, name, price, human_hours, mileage_required):
        self.name = name
        self.price = price
        self.human_hours = human_hours
        self.mileage_required = mileage_required
    def __repr__(self):
        return "{name}, ¥{price}, {human_hours} human hours needed for maintenance, every {mileage_required} kms.".format(name=self.name, price=self.price, human_hours=self.human_hours, mileage_required=self.mileage_required)

oil_and_filter_change = Maintenance("Oil and filter change", "50000", "3", "8000km")


class Repair:
    def __init__(self, customer_look_for_service, part, warranty):
        self.customer_look_for_service = customer_look_for_service
        self.part = part
        self.warranty = warranty
        self.human_hours = 0.0
        self.price = 0.0
    def making_repair(self, customer_look_for_service):
        if self.part.status == "Out of stock":
            print("Part out of stock.")
        self.human_hours += float(self.part.human_hours)
        if (customer_look_for_service.mileage < self.warranty.mileage) and (float(customer_look_for_service.serice_date - customer_look_for_service.purchase_date) < float(self.warranty.year)):
            self.part.price = 0.0
            self.price += float(self.part.price) + float(self.part.human_hours) * 6000.0
        return self.human_hours, self.price

class CustomerMaintenance:
    def __init__(self, customer_look_for_service, mileage_before_service, maintenance):
        self.customer_look_for_service = customer_look_for_service
        self.mileage_before_service = mileage_before_service
        self.maintenance = maintenance
        self.price = 0.0
        self.human_hours = 0.0
        self.required_maintenance = []
    def maintain_vehicle(self, customer_look_for_service):
        pass