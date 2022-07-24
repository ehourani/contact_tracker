class Location_Collection:
	"""docstring for Location_Collection"""
	def __init__(self, locations=[]):
		self.locations = locations

	def __str__(self):
		loc_string = ''
		for loc in self.locations:
			loc_string += str(loc) + '\n\n'
		return loc_string

	def __repr__(self):
		return str(self)

	def add_location(self, location):
		self.locations += [location]

	def delete_location(self, location):
		self.locations -= [location]


class Location:
	"""
	Represents a specific location that people can exist in
	"""
	def __init__(self, name, description, people=[]):
		self.name = name
		self.description = description
		self.people = [] + people

	def __str__(self):
		people_string = ''
		for person in self.people:
			people_string += str(person) + '\n\t'
		return f"========== Location:\t{self.name} ==========\n" + \
		f"Description:\t {self.description}\n" + \
		f"People:\n\t{people_string}"

	def __repr__(self):
		return str(self)

	def add_person(self, person):
		self.people += [person]

	def delete_person(self, person):
		self.people -= [person]

	def combine_with(self, location, new_name=None, new_description=None):
		if new_name is not Null:
			self.name = new_name
		if new_description is not Null:
			self.description = new_description

		for person in self.people:
			if person not in self.people:
				self.add_person(person)


class Person():
	"""Represents a specific person"""
	def __init__(self, fname, lname, phone):
		self.fname = fname
		self.lname = lname
		self.phone = phone

	def __str__(self):
		return f"{self.fname} {self.lname}; Phone: {self.phone}"

	def __repr__(self):
		return str(self)




if __name__ == '__main__':

	# #### New test #####
	# name = input('Please enter a location name: ')
	# desc = input('Please enter a location description: ')
	# print('Please provide the following info for people:')

	# people = []
	# while True:
	# 	fname = input('First name: ')
	# 	if fname == '':
	# 		break
	# 	lname = input('Last name: ')
	# 	phone = input('Phone number: ')
	# 	person = Person(fname, lname, phone)
	# 	people += [person]

	# location_people = people
	# print(Location(name, desc, location_people))



	# # Define people
	# bb = Person('Brendan', 'Halpin', 8573294300)
	# catherine = Person('Katherine', 'Beane', 8573048230)
	# harley = Person('Harley', 'Halpin', 6173492849)
	# mallory = Person('Mallory', 'DeVoe', 8573048230)
	# me = Person('Eesam', 'Hourani', 7202859329)

	# # Define Locations
	# quincy = Location("Quincy", "pizza connection :D", [catherine, harley, mallory])
	# beacon_hill = Location('Beacon Hill', 'old money af', [bb])

	# # Print
	# print(str(Location_Collection([quincy, beacon_hill])))

