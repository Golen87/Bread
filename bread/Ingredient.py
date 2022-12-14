import re

import bread.units as units
import bread.ingredients as ingredients
from bread.Quantity import Quantity


class Ingredient:
	def __init__(self, *args):
		self.name = None
		self.quantity = None

		if len(args) == 1:
			m = re.search('^\s*([0-9.]+)\s*([A-Za-z]+)\s+(.+)\s*$', str(args[0]))
			if m:
				self.quantity = Quantity(m.group(1), m.group(2));
				self.set_name(m.group(3))
			else:
				raise TypeError(f'Illegal arguments: {args}')

		elif len(args) == 2:
			if isinstance(args[0], str):
				self.set_name(args[0])
			else:
				raise TypeError(f'Illegal arguments: {args}')

			if isinstance(args[1], (int,float,str)):
				self.quantity = Quantity(args[1])
			elif isinstance(args[1], Quantity):
				self.quantity = args[1]
			else:
				raise TypeError(f'Illegal arguments: {args}')

		elif len(args) == 3:
			if isinstance(args[0], str):
				self.set_name(args[0])
			else:
				raise TypeError(f'Illegal arguments: {args}')

			if isinstance(args[1], (int,float,str)) and isinstance(args[2], str):
				self.quantity = Quantity(float(args[1]), args[2])
			else:
				raise TypeError(f'Illegal arguments: {args}')

		else:
			raise TypeError(f'Illegal arguments: {args}')

		if self.quantity.is_volume() and not self.is_measurable():
			raise TypeError(f"Ingredient is not measurable: '{self}'")
		if self.quantity.is_countable() and not self.is_countable():
			raise TypeError(f"Ingredient is not countable: '{self}'")

	def __str__(self):
		return f'{self.quantity} {self.get_name()}'

	def __repr__(self):
		return f"<class 'Ingredient' name:{self.name!r}, quantity:{self.quantity!r}>"

	def __add__(self, other):
		if isinstance(other, Ingredient):
			if self.name == other.name:
				converted = other.to_unit(self.quantity.unit)
				return Ingredient(self.name, self.quantity + converted.quantity)
			raise TypeError(f"Cannot add ingredients: '{self.name}' + '{other.name}'")
		raise TypeError(f'Cannot add Ingredient with {type(other)}')

	def __iadd__(self, other):
		return self._copy(self.__add__(other))

	def __mul__(self, other):
		return Ingredient(self.name, other * self.quantity)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __imul__(self, other):
		return self._copy(self.__mul__(other))

	def _copy(self, other):
		self.name = other.name
		self.quantity = other.quantity
		return self


	@property
	def weight(self):
		if self.quantity.is_weight():
			return self.quantity.to_base()
		elif self.quantity.is_volume():
			density = ingredients.data[self.name]['density']
			weight = density * self.quantity.to_base().value
			return Quantity(weight, units.weight_base)
		elif self.quantity.is_countable():
			density = ingredients.data[self.name]['weight']
			weight = density * self.quantity.to_base().value
			return Quantity(weight, units.weight_base)
		raise TypeError(f"Cannot convert unit to weight: '{self.quantity.unit}'")

	@property
	def volume(self):
		if self.quantity.is_volume():
			return self.quantity.to_base()
		else:
			if 'density' not in ingredients.data[self.name]:
				raise TypeError(f"Ingredient is not measurable: '{self}'")
			density = ingredients.data[self.name]['density']
			weight = self.weight.value / density
			return Quantity(weight, units.volume_base)

	@property
	def count(self):
		if self.quantity.is_countable():
			return self.quantity.to_base()
		else:
			if 'weight' not in ingredients.data[self.name]:
				raise TypeError(f"Ingredient is not countable: '{self}'")
			density = ingredients.data[self.name]['weight']
			weight = self.weight.value / density
			return Quantity(weight, units.countable_base)

	@property
	def cost(self):
		cost = ingredients.data[self.name].get('cost', 0)
		weight = self.weight.to_base().value
		return Quantity(cost * weight, 'kr')


	def is_measurable(self):
		return 'density' in ingredients.data[self.name]

	def is_countable(self):
		return 'weight' in ingredients.data[self.name]

	def get_name(self):
		# return self.name
		return ingredients.data[self.name]['alias'][0]

	def get_content(self, cont_type):
		return ingredients.get_content(self.name).get(cont_type, 0)

	def to_unit(self, new_unit: str):
		if units.is_weight(new_unit):
			return Ingredient(self.name, self.weight.to_unit(new_unit))
		elif units.is_volume(new_unit):
			return Ingredient(self.name, self.volume.to_unit(new_unit))
		elif units.is_countable(new_unit):
			return Ingredient(self.name, self.count.to_unit(new_unit))
		raise TypeError(f"Unknown unit: '{new_unit}'")

	def to_base(self, strict=False):
		return Ingredient(self.name, self.quantity.to_base(strict))

	def set_name(self, new_name: str):
		self.name = ingredients.get_base(new_name.lower())

	def convert(self, content: str, new_name: str):
		other = Ingredient(new_name, 0)

		if self.name == other.name:
			return self

		r1 = self.get_content(content)
		r2 = other.get_content(content)

		if r1 and r2:
			weight = self.weight.to_base().value * r2 / r1
			return Ingredient(new_name, weight, units.weight_base)
		else:
			raise TypeError(f"Unknown replacement: {self.name}' -> '{new_name}'")
