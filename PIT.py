# Define the Employee class
class Employee:
    def _init_(self, name, income, position, organization):# Define the  method of the Employee class
        self.name = name  # Assigning the 'name' argument to the 'name' attribute of the instance
        self.income = income  # Assigning the 'income' argument to the 'income' attribute of the instance
        self.position = position  # Assigning the 'position' argument to the 'position' attribute of the instance
        self.organization = organization  # Assigning the 'organization' argument to the 'organization' attribute of the instance

class TaxCalculator: # Defineing the TaxCalculator class
    def _init_(self, employee): # Defineing the method of the TaxCalculator class
        self.employee = employee   # Assigning the 'employee' argument to the 'employee' attribute of the instance
        self.taxable_income = self.calculate_taxable_income()   # Calling the calculate_taxable_income and assign its result to the 'taxable_income'
        self.tax_amount = self.calculate_tax_amount()  # Calling the calculate_tax_amount and assign its result to the 'tax_amount' 

    def calculate_taxable_income(self):  # Defineing the calculate_taxable_income of the TaxCalculator class
    
        taxable_income = self.employee.income  # Initializeing the 'taxable_income' variable with the employee's income

        if self.employee.position == "Regular":  # Checking if the employee's position is "Regular"
            taxable_income -= 0.10 * self.employee.income   # Deducting PF contribution (10%) from the taxable income
            taxable_income -= 0.05 * self.employee.income  # Deducting GIS contribution (5%) from the taxable income

        
        general_deductions = min(0.05 * taxable_income, 350000)# Calculateing general deductions (5% of taxable income or 350,000, whichever is lower)
        taxable_income -= general_deductions  # Deducting general deductions from the taxable income

        return taxable_income     # Returning the calculated taxable income

    def calculate_tax_amount(self): # Defineing the calculate_tax_amount method of the TaxCalculator class
       # Defineing tax slabs and rates
        tax_slabs = [
            (300000, 0.0),
            (400000, 0.10),
            (650000, 0.15),
            (1000000, 0.20),
            (1500000, 0.25),
            (float('inf'), 0.30)
        ]

        # Calculateing tax amount based on taxable income and tax slabs
        tax_amount = 0 # Initializeing the 'tax_amount' variable to 0
        for slab, rate in tax_slabs:  # Iterate through tax slabs and calculate tax amount
            if self.taxable_income <= 0:  # Breaking the loop if taxable income is zero or less
                break
            if self.taxable_income > slab: # Calculateing tax amount for the current slab and update taxable income
                tax_amount += slab * rate
                self.taxable_income -= slab
            else:
                tax_amount += self.taxable_income * rate
                break

        # Applying surcharge if applicable
        if tax_amount >= 1000000: # Applying surcharge if tax amount is equal to or greater than 1,000,000
            tax_amount += 0.10 * tax_amount

        return tax_amount   # Returning the calculated tax amount
    
# Example usage:
try:
    # Prompting user for employee details  
    name = input("Enter employee's name: ")
    income = float(input("Enter employee's income: "))
    position = input("Enter employee's position (Regular/Non-Regular): ")
    organization = input("Enter employee's organization: ")
# Createing an Employee instance with the provided details
    emp1 = Employee(name, income, position, organization)
    calculator = TaxCalculator(emp1)  # Createing a TaxCalculator instance with the created Employee instance
    print(f"Tax amount for {emp1.name}: Nu. {calculator.tax_amount:.2f}")    # Printing the tax amount for the employee
except Exception as e:
    print("An error occurred:", str(e))   # Printing an error message if an exception occurs