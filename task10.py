from class_rep import AddressBook, Record


CONTACTS = AddressBook()


def input_error(handler):
	def wrapper(*args, **kargs):
		try:
			return handler(*args, **kargs)
		except KeyError:
			return 'Enter user name'
		except ValueError:
			return 'Give me name and phone please'
		except IndexError:
			return 'Try again'
		except TypeError:
			return 'Give me name and phone please'
	return wrapper


def hello():
	return  "How can I help you?"


def quit_func():
	return 'Good bye!'


def show():
	contact_book = {}
	for key, ph in CONTACTS.items():
		contact_phone = []
		for phone in ph.phones:
			contact_phone.append(phone.value)
		contact_book[key] = contact_phone
	return contact_book

@input_error
def add(data):
	name, phones = create_data(data)
	record = Record(name)
	for phone in phones:
		record.add(phone)
	CONTACTS.add_record(record)
	return "Contact added!"

@input_error
def change_phone(data):
	change_data = data.split()
	phone_old = change_data[0]
	phone_new = change_data[1]
	for key, record in CONTACTS.items():
		for phone in record.phones:
			if phone_old == phone.value:
				record.edit(phone_old, phone_new)
				CONTACTS[key] = record
	return f"{phone_old} --> {phone_new}: Changed!"

@input_error
def remove_phone(phone_to_delete):
	phone_to_delete = phone_to_delete.strip()
	for key, record in CONTACTS.items():
		for phone in record.phones:
			if phone_to_delete == phone.value:
				record.remove(phone.value)
				CONTACTS[key] = record
	return f"{phone_to_delete}: Deleted!"


@input_error
def search_func(data):

	return CONTACTS.search(data.strip())


def change_input(user_input):
	new_input = user_input
	data = ''
	for key in COMMANDS:
		if user_input.lower().startswith(key):
			new_input = key
			data = user_input[len(new_input):]
			break
	if data:
		return reaction_func(new_input)(data)
	return reaction_func(new_input)()


def reaction_func(reaction):
	return COMMANDS.get(reaction, break_func)


def break_func():
    return 'Wrong enter.'


def create_data(data):
	new_data = data.split()
	name = new_data[0]
	phones = new_data[1:]
	if name.isnumeric():
		raise ValueError()
	for phone in phones:
		if not phone.isnumeric():
			raise ValueError()
	return name, phones

COMMANDS = {
'hello': hello, 
'add': add, 
'change phone': change_phone,
'remove phone' : remove_phone,
'search': search_func, 
'show all': show,
'good bye': quit_func, 
'close': quit_func, 
'exit': quit_func
}

@input_error
def main():
	while True:
		user_input = input('Enter command for bot: ')
		result = change_input(user_input)
		print(result)
		if result == 'Good bye!':
			break


if __name__ == '__main__':
	main()