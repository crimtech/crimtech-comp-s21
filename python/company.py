class Company:
	# This is the constructor of the class. It gets called every time a new Company object is created.
	def __init__(self, name):
		self.name = name
		self.catalog = {}
		self.employees = []
		# Add other fields here!

	# The self parameter is a reference to the current instance of the class,
	# and is used to access variables that belong to the class.
	# Don't forget to add other parameters (arguments) as required.
	def add_product(self, name, price):
		# Write your method here!
		if name in self.catalog.keys():
			return False
		self.catalog[name] = price
		return True

	def add_employee(self, employee):
		# Write your method here!
		self.employees.append(employee)
		return

class Employee:
	def __init__(self, name, *role):
		self.role = role[0] if role else 1
		self.name = name
