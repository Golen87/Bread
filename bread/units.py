import math


# preferred_units = ['gallon', 'cup', 'tbsp', 'tsp']
# preferred_units = ['gallon', 'cup', '½ cup', '⅓ cup', '¼ cup', '⅛ cup', 'tbsp', 'tsp']
preferred_units = ['l', 'dl', 'msk', 'tsk', 'krm']
# preferred_units = ['ml']


weight_base = 'kg'
weight_units = {
	't':	1000,
	'kg':	1,
	'hg':	.1,
	'g':	.001,
	'mg':	.000001,

	'lb':	.45359237,
	'oz':	.0283495231,
}

volume_base = 'l'
volume_units = {
	'l':		1,
	'dl':		.1,
	'cl':		.01,
	'ml':		.001,

	'msk':		.015,
	'tsk':		.005,
	'krm':		.001,

	'kkp':		.15,
	'glas':		.20,
	'tekopp':	.25,

	'tsp':			.00492892159,
	'teaspoon':		.00492892159,
	'teaspoons':	.00492892159,
	'tbsp':			.0147867648,
	'tablespoon':	.0147867648,
	'tablespoons':	.0147867648,
	'cup':			.236588237,
	'cups':			.236588237,
	'½ cup':		.236588237/2,
	'½ cups':		.236588237/2,
	'⅓ cup':		.236588237/3,
	'⅓ cups':		.236588237/3,
	'¼ cup':		.236588237/4,
	'¼ cups':		.236588237/4,
	'⅛ cup':		.236588237/8,
	'⅛ cups':		.236588237/8,
	'gallon':		3.78541178,
	'gallons':		3.78541178,

	'floz':			.0295735296,
}

countable_base = 'st'
countable_units = {
	'':			1,
	'st':		1,
	'pcs':		1,
	'dussin':	12,
	'dozen':	12,
}


def is_weight(unit: str) -> bool:
	return unit in weight_units

def is_volume(unit: str) -> bool:
	return unit in volume_units

def is_countable(unit: str) -> bool:
	return unit in countable_units

def get_base(unit: str) -> str:
	if is_weight(unit):
		return weight_base
	elif is_volume(unit):
		return volume_base
	elif is_countable(unit):
		return countable_base
	return unit

def get_multiplier(unit1: str, unit2: str) -> float:
	if is_weight(unit1) and is_weight(unit2):
		return weight_units[unit1] / weight_units[unit2]
	elif is_volume(unit1) and is_volume(unit2):
		return volume_units[unit1] / volume_units[unit2]
	elif is_countable(unit1) and is_countable(unit2):
		return countable_units[unit1] / countable_units[unit2]
	elif unit1 == unit2:
		return 1.0
	else:
		raise TypeError(f'Mismatching units: {unit1}, {unit2}')

def soft_volume(amount, old_unit: str):
	global preferred_units

	def convert(unit):
		return get_multiplier(old_unit, unit) * amount
	def score(unit):
		log = math.log10(convert(unit))
		return abs(0.1 - log)

	if amount <= 0:
		# return (0, '')
		return (amount, old_unit)

	scores = [(unit, score(unit)) for unit in preferred_units]
	optimal_unit = min(scores, key=lambda x:x[1])[0]

	# units = [optimal_unit]
	# debug = f'{amount:.0f} {old_unit}\t'
	# for new_unit in units:
		# value = convert(new_unit)
		# debug += f'{soft_round(value):>4} {new_unit}\t'
		# score = abs(math.log10(value))
		# print(' |', round(value,1), new_unit, '---', round(score,1))

	# print(, '->', round(value,1), new_unit)
	# print(debug)
	return (convert(optimal_unit), optimal_unit)

def set_units(*args):
	global preferred_units
	for unit in list(args):
		if unit not in volume_units:
			raise TypeError(f"Unknown unit for volume: '{unit}'")
	preferred_units = list(args)


if __name__ == '__main__':
	for i in range(10):
		value = i
		print(soft_volume(value, 'ml'))
	for i in range(9):
		value = 10 + 10*i
		print(soft_volume(value, 'ml'))
	for i in range(10):
		value = 100 + 100*i
		print(soft_volume(value, 'ml'))
	for i in range(9):
		value = 1000 + 1000*i
		print(soft_volume(value, 'ml'))
