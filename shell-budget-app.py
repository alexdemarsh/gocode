from collections import OrderedDict
import os.path

commands_list = ['o)pen', 's)ave', 'a)dd item', 'l)ist items', 'r)emove item']

for i in commands_list:
	print i

def open_command(state):
	state["filename"] = raw_input("File to open: ")
	state["rows"] = csv_to_array(read_data(state["filename"]))

def write_data(filename, data):
	with open(filename, "w") as f:
		f.write(data)

def read_data(filename):
	if not os.path.exists(filename):
		return []
		print "File not found."

	with open(filename, "r") as f:
		return f.readlines


def save_command(state):
	write_data(state["filename"], array_to_csv(state["rows"]))

def new_budget_item():
	#as ordered dictionary ?
	item = OrderedDict()

	item["name"] = raw_input("Name: ")
	item["amount"] = raw_input("Amount: ")
	item["monthly"] = raw_input("Monthly: ")

	return item

def add_budget_item(state):
	state["rows"].append(new_budget_item())

def list_budget_items(state):
	

def convert_to_float(num):
	try:
		num = float(num)
	except ValueError:
		print 'That was not a number'
	finally:
		return num

def array_to_csv():
	print "a"

def csv_to_array():
	print "c"

def display_budget_items():
	total = 0.0
	for i in rows:
		total = total + convert_to_float(i[1])
		print i
	print 'Total is: %s' % total

def sum_budget_items():
	print 'sum'

def remove_budget_item():
	removed_item = raw_input("Item to remove: ")
	for i in rows:
		if str(i[0]) == removed_item:
			rows.remove(i)
	else:
		print '%s not found.' % removed_item
		
commands = {'o':open_command, 's':save_command, 'a':add_budget_item, 'l':list_budget_items, 'r': remove_budget_item}

def ui_loop():
	ui = raw_input(': ')
	while ui[0].lower() != 'q':
		if ui[0].lower() not in commands.keys():
			print 'Try one of these: '
			for i in commands_list:
				print i
		else:
			commands[ui[0].lower()]()
		ui = raw_input(': ')


ui_loop()