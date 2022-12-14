import math


def to_int(value):
	return int(value) if value.is_integer() else value

def soft_round(value, prec_inc=0):
	if value == 0:
		return 0
	prec = 3 if value > 1 else 2
	e = prec - 2 - math.floor(math.log10(value))
	if e <= 0:
		return round(value)
	return to_int(round(value, e))

def to_perc(value):
	return str(soft_round(value * 100)) + '%'
