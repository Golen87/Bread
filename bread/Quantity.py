import re

import bread.units as units
from bread.utils import soft_round, to_int

class Quantity:
	def __init__(self, *args, **kwargs):
		self.value = 0
		self.unit = None

		# Value
		if len(args) > 0:
			if isinstance(args[0], (int,float)):
				self.value = float(args[0])
			elif isinstance(args[0], str):
				m = re.search('^\s*([0-9.]+)\s*([A-Za-z]+)?\s*$', args[0])
				if m:
					self.value = float(m.group(1))
					self.unit = m.group(2)
				else:
					raise TypeError(f'Illegal arguments: {args}')
			else:
				raise TypeError(f'Illegal arguments: {args}')

		# Unit (optional)
		if len(args) == 1:
			if not self.unit:
				self.unit = 'g'
		elif len(args) == 2 and isinstance(args[1], str):
			self.unit = args[1]
		else:
			raise TypeError(f'Illegal arguments: {args}')

		self.unit = self.unit.lower()

		self.strict = False
		if 'strict' in kwargs:
			self.strict = kwargs['strict']

	def __str__(self):
		if self.strict:
			return f'{soft_round(self.value)} {self.unit}'

		if self.value == 0:
			return ''

		if self.is_weight():
			base = self.to_unit('g')
			return f'{soft_round(base.value)} {base.unit}'

		if self.is_volume():
			amount, unit = units.soft_volume(self.value, self.unit)
			return f"{soft_round(amount)} {unit}"

			# units = ['l', 'dl', 'msk', 'tsk', 'krm']
			# units = ['l', 'cups']

			# print('---')
			# for unit in units:
				# amount = self.to_unit(unit).value
				# print(f"{soft_round(amount)} {unit}")
			# print('---')

			# for unit in units:
				# amount = self.to_unit(unit).value
				# is_good_amount = (amount >= 0.49 and amount < 3.1)
				# if (amount >= 1.0 or unit != 'l') and (amount >= 0.49 or unit == 'g') and (amount < 3.1 or unit == 'dl'):
					# return f"{soft_round(amount)} {unit}"
				# raise TypeError(f"Internal error")

		if self.is_countable():
			base = self.to_unit('st')
			return f'{soft_round(base.value)} {base.unit}'

		return f'{soft_round(self.value)} {self.unit}'

	def __repr__(self):
		return f"<class 'Quantity' value:{self.value!r}, unit:{self.unit!r}>"

	def __int__(self):
		return int(self.value)

	def __float__(self):
		return float(self.value)

	def __add__(self, other):
		if isinstance(other, Quantity):
			b1 = self.to_base()
			b2 = other.to_base()
			if b1.unit == b2.unit:
				return Quantity(b1.value + b2.value, b1.unit)
			raise TypeError(f"Cannot add units: '{self.unit}' + '{other.unit}'")
		raise TypeError(f'Cannot add Quantity with {type(other)}')

	def __iadd__(self, other):
		return self._copy(self.__add__(other))

	def __mul__(self, other):
		if isinstance(other, (int,float)):
			return Quantity(other * self.value, self.unit)
		raise TypeError(f'Cannot multiply Quantity with {type(other)}')

	def __imul__(self, other):
		return self._copy(self.__mul__(other))

	def __rmul__(self, other):
		return self.__mul__(other)

	def __truediv__(self, other):
		if isinstance(other, Quantity):
			b1 = self.to_base()
			b2 = other.to_base()
			if b1.unit == b2.unit:
				return float(b1) / float(b2)
			raise TypeError(f"Cannot divide units: '{self.unit}' + '{other.unit}'")
		raise TypeError(f'Cannot divide Quantity with {type(other)}')

	def _copy(self, other):
		self.value = other.value
		self.unit = other.unit
		return self


	def is_weight(self):
		return units.is_weight(self.unit)

	def is_volume(self):
		return units.is_volume(self.unit)

	def is_countable(self):
		return units.is_countable(self.unit)


	def to_unit(self, new_unit: str, strict=True):
		mult = units.get_multiplier(self.unit, new_unit)
		return Quantity(mult * self.value, new_unit, strict=strict)

	def to_base(self, strict=False):
		base = units.get_base(self.unit)
		return self.to_unit(base, strict)

	def to_soft(self):
		if self.is_weight():
			return self.to_unit('g', strict=False)

		if self.is_volume():
			amount, unit = units.soft_volume(self.value, self.unit)
			return Quantity(amount, unit)

		if self.is_countable():
			return self.to_unit('st', strict=False)

		return self
