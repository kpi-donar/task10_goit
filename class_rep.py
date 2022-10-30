from collections import UserDict


class Field:
	def __init__(self, value):
		self.value = value


class Name(Field):
	pass


class Phone(Field):
	pass


class Record():
	def __init__(self, name):
		self.name = Name(name)
		self.phones = []

	def add(self, phone):
		self.phones.append(Phone(phone))

	def remove(self, phone):
		if self.phones:
			for ph in self.phones:
				if ph.value == phone:
					self.phones.remove(ph)

	def edit(self, phone_old, phone_new):
		if self.phones:
			for ph in self.phones:
				if ph.value == phone_old:
					self.phones.remove(ph)
		self.phones.append(Phone(phone_new))


class AddressBook(UserDict):
	def add_record(self, record):
		self.data[record.name.value] = record

	def search(self, value):
		if self.data.get(value):
			return self.data[value].name.value, [x.value for x in self.data[value].phones]

		for record in self.data.values():
			for phone in record.phones:
				if phone.value == value:
					return record.name.value, [x.value for x in record.phones]

		return "Contact unavailable."

