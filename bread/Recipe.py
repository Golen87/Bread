import math

from bread.utils import soft_round, to_int
from bread.Ingredient import Ingredient
from bread.Quantity import Quantity


class Recipe:
	def __init__(self, **kwargs):
		self.name = kwargs.get('name', None)
		self.ingredients = []

		ingredients = kwargs.get('ingredients', {})
		if isinstance(ingredients, dict):
			for name in ingredients:
				amount = ingredients[name]
				self.ingredients.append(Ingredient(name, amount))
			return
		elif isinstance(ingredients, str):
			for line in ingredients.splitlines():
				line = line.strip()
				if '---' in line:
					if len(self.ingredients) > 0:
						self.ingredients.append(None)
				elif line:
					self.ingredients.append(Ingredient(line))
			return

		# raise TypeError(f'Illegal arguments: {args}')

	def __str__(self):
		def boxify(lines):
			box_width = max(map(len, lines))
			title = f' {self.name} '
			title_left = math.floor((box_width-len(title)+2)/2)
			title_right = math.ceil((box_width-len(title)+2)/2)

			text = '+' + title_left*'-' + title + title_right*'-' + '+\n'
			for line in lines:
				if line:
					text += f'| {line:>{box_width}} |\n'
				else:
					text += '+' + (box_width+2) * '-' + '+\n'
			text += '+' + (box_width+2) * '-' + '+'
			return text

		volumes = []
		volume_units = []
		ratios = []
		total_weight = self.total_weight()
		for ingr in self.ingredients:
			# Volumes
			if ingr and ingr.is_measurable() and ingr.quantity.value > 0:
				vol = ingr.volume.to_soft()
				volumes.append(f'{soft_round(vol.value)}')
				volume_units.append(f'{vol.unit}')
			# elif ingr.is_countable():
				# volumes.append(f'{ingr.count}')
			else:
				volumes.append(f'')
				volume_units.append(f'')

			# Ratios
			ratio = ingr.weight / total_weight if ingr else 0
			if ingr and ingr.quantity.value > 0:
				ratios.append(f'{soft_round(ratio*100)} %')
			else:
				ratios.append('')

		name_width = max(map(lambda ingr:len(ingr.get_name()) if ingr else 0, self.ingredients))
		volume_width = max(map(len, volumes))
		volume_unit_width = max(map(len, volume_units))
		ratio_width = max(map(len, ratios))
		weight_width = max(map(lambda ingr:len(str(ingr.weight)) if ingr else 0, self.ingredients))

		lines = []
		for i,ingr in enumerate(self.ingredients):
			if ingr:
				line = ''
				line += f'{ingr.get_name():>{name_width}}   '
				line += f'{volumes[i]:>{volume_width}} {volume_units[i]:<{volume_unit_width}}  '
				line += f'{str(ingr.weight):>{weight_width}}   '
				line += f'{str(ratios[i]):>{ratio_width}}'
				lines.append(line)
			else:
				lines.append('')

		return boxify(lines)

	def __repr__(self):
		return f"<class 'Recipe' ingredients:{len(self.ingredients)}>"


	@property
	def flour(self):
		return self.get_content('flour')

	@property
	def water(self):
		return self.get_content('water')

	@property
	def salt(self):
		return self.get_content('salt')

	@property
	def hydration(self):
		return self.water / self.flour


	def set_total_weight(self, quantity):
		# if isinstance(quantity, (int, float)):
			# quantity = Quantity(quantity, 'g')
		if isinstance(quantity, Quantity):
			scale = quantity / self.total_weight()
			for ingr in self.ingredients:
				if ingr:
					ingr *= scale
			return self
		raise TypeError(f'must be Quantity, not {type(quantity)}')

	def total_weight(self):
		total = Quantity(0, 'kg')
		for ingr in self.ingredients:
			if ingr:
				total += ingr.to_unit('kg').quantity
		return total

	def total_cost(self):
		total = Quantity(0, 'kr')
		for ingr in self.ingredients:
			if ingr:
				total += ingr.cost
		return total

	def get_content(self, cont_type):
		total = Quantity(0, 'kg')
		for ingr in self.ingredients:
			if ingr:
				fac = ingr.get_content(cont_type)
				weight = ingr.to_unit('kg').quantity
				total += fac * weight
		return total

	def replace(self, content: str, new_name: str):
		for ingr in self.ingredients:
			if ingr and ingr.get_content(content):
				ingr._copy(ingr.convert(content, new_name))
		return self
