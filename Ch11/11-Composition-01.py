class Customer:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def customer_details(self):
        return "%s %s Email ID is : %s" % (self.first_name, self.last_name, self.email)


class CustomerIspPLAN():  # Class Composition Example

    def __init__(self, first_name, last_name, email, isp_plan):

        self.customer = Customer(first_name, last_name, email)

        self.isp_plan = isp_plan

    def customer_plan_details(self):
        return "%s %s Email ID and plan is << %s : %s Per Month >> respectively" % \
               (self.customer.first_name, self.customer.last_name, self.customer.email, self.isp_plan)


class CustomerMobilePlan():

    def __init__(self, first_name, last_name, email, mobile_plan):
        self.customer = Customer(first_name, last_name, email)

        self.mobile_plan = mobile_plan

    def customer_mobile_plan_details(self):
        return "%s %s Email ID and plan is << %s : %s Per Month>> respectively" % \
               (self.customer.first_name, self.customer.last_name, self.customer.email, self.mobile_plan)


if __name__ == "__main__":

    customer1 = CustomerIspPLAN("John", "Doe", "JohnDoe@email.com", "499")
    print (customer1.customer.customer_details())
    print (customer1.customer_plan_details())

    print ("\n#######################################\n")

    customer2 = CustomerMobilePlan("Michael", "Carrick", "MichaelCarrick@email.com", "325")
    print (customer2.customer.customer_details())
    print (customer2.customer_mobile_plan_details())