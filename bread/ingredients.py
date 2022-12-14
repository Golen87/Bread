
# Density: kg/l
# Weight: kg/st
# Cost: kr/kg

data = {

	# Flours

	'bread flour': {
		'content': {
			'flour': 1
		},
		'density': .6,
		'cost': 11.5,
		'alias': ['vetemjöl special'],
	},
	'all-purpose flour': {
		'content': {
			'flour': 1
		},
		'density': .6,
		'cost': 8.0,
		'alias': ['vetemjöl', 'mjöl', 'flour'],
	},
	'cake flour': {
		'content': {
			'flour': 1
		},
		'density': .6,
		'cost': 18.0,
		'alias': ['kakmjöl', 'pastry flour'],
	},
	'whole-wheat flour': {
		'content': {
			'flour': 1
		},
		'density': .6,
		'cost': 13.3,
		'alias': ['grahamsmjöl', 'graham flour'],
	},
	'light rye flour': {
		'content': {
			'flour': 1
		},
		'density': .50,
		'cost': 15.3,
		'alias': ['finmalt rågmjöl', 'siktat rågmjöl', 'white rye flour'],
	},
	'rye flour': {
		'content': {
			'flour': 1
		},
		'density': .55,
		'cost': 15.3,
		'alias': ['grovmalt rågmjöl', 'rågmjöl', 'coarse rye flour', 'coarse dark rye flour', 'dark rye flour'],
	},
	'sifted rye flour': {
		'content': {
			'flour': 1
		},
		'density': .55,
		'cost': 11.48,
		'alias': ['rågsikt'],
	},
	'spelt wheat': {
		'content': {
			'flour': 1
		},
		'density': .60,
		'cost': 25,
		'alias': ['dinkelmjöl', 'dinkelsikt', 'dinkel', 'spelt', 'speltvete', 'dinkel wheat', 'hulled wheat'],
	},
	'dinkelmjöl fullkorn': {
		'content': {
			'flour': 1
		},
		'density': .60,
		'cost': 29,
		'alias': ['dinkelmjöl fullkorn'],
	},
	'almond flour': {
		'content': {
			'flour': 1,
			'fat': .5,
		},
		'density': .50,
		'cost': 170,
		'alias': ['mandelmjöl'],
	},
	'potato flour': {
		'content': {
			'flour': 1,
		},
		'density': .80,
		'cost': 22,
		'alias': ['potatismjöl'],
	},
	'oats': {
		'content': {
			'flour': 1,
			'fat': .07,
		},
		'density': .37,
		'cost': 15,
		'alias': ['havregryn'],
	},
	'crushed rye': {
		'content': {
			'flour': 1,
		},
		'density': .65,
		'cost': 33,
		'alias': ['rågkross'],
	},
	'wheat bran': {
		'content': {
			'flour': 1,
		},
		'density': .3,
		'cost': 20,
		'alias': ['vetekli'],
	},


	# Fluids

	'water': {
		'content': {
			'water': 1
		},
		'density': 1.0,
		'cost': 0,
		'alias': ['vatten', 'kallt vatten'],
	},
	'cold water': {
		'content': {
			'water': 1
		},
		'density': 1.0,
		'cost': 0,
		'alias': ['kallt vatten'],
	},
	'boiling water': {
		'content': {
			'water': 1
		},
		'density': 0.95865,
		'cost': 0,
		'alias': ['kokhett vatten'],
	},
	'coffee': {
		'content': {
			'water': 1,
		},
		'density': 0.95865,
		'cost': 8,
		'alias': ['hett kaffe', 'kaffe'],
	},
	'milk': {
		'content': {
			'water': .87,
			'fat': .02
		},
		'density': 1.03,
		'cost': 10,
		'alias': ['mjölk'],
	},
	'sour milk': {
		'content': {
			'water': .88,
			'sugar': .05,
			'fat': .03,
		},
		'density': 1.03,
		'cost': 12,
		'alias': ['filmjölk'],
	},
	'yoghurt': {
		'content': {
			'water': .88,
			'sugar': .05,
			'fat': .03,
		},
		'density': 1.03,
		'cost': 14,
		'alias': ['yoghurt', 'mild yoghurt', 'naturell yoghurt', 'mild naturell yoghurt'],
	},


	# Salt

	'salt': {
		'content': {
			'salt': 1
		},
		'density': 1.25,
		'cost': 8.95,
		'alias': ['salt'],
	},


	# Yeast

	'fresh yeast': {
		'content': {
			'water': .71,
			'yeast': 50,
		},
		'weight': .055,
		'cost': 59.8,
		'alias': ['jäst', 'färsk jäst', 'fresh', 'cake yeast'],
	},
	'instant dry yeast': {
		'content': {
			'water': .05,
			'yeast': 14,
		},
		'density': .63,
		'cost': 267.86,
		'alias': ['torrjäst', 'dry yeast', 'instant yeast', 'idy'],
	},
	'active dry yeast': {
		'content': {
			'water': .05,
			'yeast': 20,
		},
		'density': .63,
		'cost': 267.86,
		'alias': ['aktiv torrjäst', 'active yeast', 'ady'],
	},


	# Fat

	'butter': {
		'content': {
			'water': .16,
			'salt': .012,
			'fat': .82,
		},
		'density': .95,
		'cost': 95.0,
		'alias': ['smör'],
	},
	'olive oil': {
		'content': {
			'fat': .92,
		},
		'density': .96,
		'cost': 91.6,
		'alias': ['olivolja', 'olja'],
	},
	'oil': {
		'content': {
			'fat': 1,
		},
		'density': .96,
		# 'cost': 91.6,
		'alias': ['olja'],
	},


	# Sugar

	'sugar': {
		'content': {
			'sugar': 1,
		},
		'density': .9,
		'cost': 9.25,
		'alias': ['socker', 'strösocker', 'granulated sugar'],
	},
	'light molasses': {
		'content': {
			'water': .19,
			'sugar': .80,
		},
		'density': 1.4,
		'cost': 23.93,
		'alias': ['ljus sirap'],
	},
	'dark molasses': {
		'content': {
			'water': .19,
			'sugar': .80,
		},
		'density': 1.4,
		'cost': 23.93,
		'alias': ['mörk sirap', 'brödsirap'],
	},
	'honey': {
		'content': {
			'water': .16,
			'sugar': .82,
		},
		'density': 1.2,
		'cost': 150,
		'alias': ['honung'],
	},
	'brown sugar': {
		'content': {
			'water': .017,
			'sugar': .973,
		},
		'density': .75,
		'cost': 32,
		'alias': ['farinsocker'],
	},
	'muscovado sugar': {
		'content': {
			'water': .04,
			'sugar': .90,
		},
		'density': .75,
		'cost': 57,
		'alias': ['muscovadosocker', 'mörkt muscovadosocker', 'muscovado'],
	},
	'powdered sugar': {
		'content': {
			'sugar': 1,
		},
		'density': .6,
		'cost': 28,
		'alias': ['florsocker'],
	},
	'pearl sugar': {
		'content': {
			'sugar': 1,
		},
		'density': .6,
		'cost': 28,
		'alias': ['pärlsocker'],
	},
	'vanilla sugar': {
		'content': {
			'sugar': 1,
			'vanilla': 0.75
		},
		'density': .60,
		'cost': 90,
		'alias': ['vaniljsocker'],
	},
	'vanilla extract': {
		'content': {
			'vanilla': 1
		},
		'density': .88,
		'cost': 2000,
		'alias': ['flytande vaniljextrakt', 'liquid vanilla extract'],
	},
	'vanilla powder': {
		'content': {
			'vanilla': 0.3
		},
		'density': .89,
		'cost': 7000,
		'alias': ['vaniljpulver'],
	},
	# Vaniljstång = 1.5 tsk extrakt


	# Egg

	'egg': {
		'content': {
			'water': .74,
			'fat': .11,
		},
		'density': 1.03,
		'weight': .06*.89, # No shell
		'cost': 3.0 / (.06*.89),
		'alias': ['ägg', 'eggs'],
	},
	'egg white': {
		'content': {
			'water': .88,
		},
		'density': 1.03,
		'weight': .06*.58,
		'cost': 3.0 / (.06*.58),
		'alias': ['äggvita', 'white'],
	},
	'egg yolk': {
		'content': {
			'water': .48,
			'fat': .33,
		},
		'density': 1.03,
		'weight': .06*.31,
		'cost': 3.0 / (.06*.31),
		'alias': ['äggula', 'yolk'],
	},


	# Spices

	'cocoa': {
		'density': .40,
		'cost': 105,
		'alias': ['kakao'],
	},
	'cardamom': {
		'density': .70,
		'cost': 700,
		'alias': ['kardemumma'],
	},
	'cinnamon': {
		'density': .52,
		'cost': 300,
		'alias': ['kanel', 'malen kanel', 'ground cinnamon'],
	},
	'baking powder': {
		'density': 1.0,
		'cost': 60,
		'alias': ['bakpulver'],
	},
	'bicarbonate': {
		'density': 1.0,
		'cost': 70,
		'alias': ['bikarbonat'],
	},
	'hjorthornssalt': {
		'density': .60,
		'cost': 220,
		'alias': ['hjorthornssalt', 'ammonium carbonate'],
	},

	'anise seeds': {
		'density': .4,
		'cost': 575,
		'alias': ['hel anis'],
	},

	'cumin seeds': {
		'density': .4,
		'cost': 380,
		'alias': ['hel kummin'],
	},

	'fennel seeds': {
		'density': .4,
		'cost': 585,
		'alias': ['fänkålsfrö'],
	},

	'cardamom seeds': {
		'density': .4,
		'cost': 1000,
		'alias': ['hela kardemummakärnor', 'kardemummakärnor'],
	},

	'powder ginger': {
		'density': .5,
		'cost': 800,
		'alias': ['malen ingefära', 'ground ginger'],
	},

	'carnation': {
		'density': .4,
		'cost': 625,
		'alias': ['malen nejlika'],
	},
	'torkade hela pomeransskal': {
		#.
	},


	# Nuts, seeds, bran

	'whole spelt': {
		'density': .8,
		'cost': 48,
		'alias': ['hel dinkel'],
	},
	'almonds': {
		'content': {
			'fat': .56,
			'water': .06,
		},
		'density': .70,
		'cost': 160,
		'alias': ['mandel', 'sötmandel'],
	},
	'hazelnuts': {
		'content': {
			'fat': .65,
			'water': .07,
		},
		'density': .65,
		'cost': 170,
		'alias': ['hasselnötter', 'hasselnötskärnor'],
	},
	'walnuts': {
		'content': {
			'fat': .58,
			'water': .03,
		},
		'density': .60,
		'cost': 190,
		'alias': ['valnötter', 'valnötskärnor'],
	},
	'pecans': {
		'content': {
			'fat': .53,
		},
		'density': .66,
		'cost': 375,
		'alias': ['pecannötter'],
	},
	'sesame seeds': {
		'content': {
			'fat': .46,
			'water': .09,
		},
		'density': .68,
		'cost': 70,
		'alias': ['sesamfrön'],
	},
	'coconut flakes': {
		'content': {
			'fat': .69,
			'sugar': .07,
		},
		'density': .35,
		'cost': 70,
		'alias': ['kokos', 'kokosflingor'],
	},
	'linseeds': {
		'content': {
			'fat': .39,
			'water': .10,
		},
		'density': .65,
		'cost': 25,
		'alias': ['linfrön', 'linfrö', 'flax seeds'],
	},
	'sunflower seeds': {
		'content': {
			'fat': .38,
			'water': .07,
		},
		'density': .62,
		'cost': 40,
		'alias': ['solrosfrön', 'solroskärnor'],
	},
	'pumpkin seeds': {
		'content': {
			'fat': .39,
			'water': .07,
		},
		'density': .58,
		'cost': 85,
		'alias': ['pumpafrön', 'pumpakärnor'],
	},


	# Fruits

	'carrot': {
		'content': {
			'water': .88,
			'sugar': .06,
			'fat': .06,
		},
		# 'density': .60,
		'cost': 25,
		'alias': ['morot', 'finriven morot'],
	},
	'apples': {
		'content': {
			'water': .85,
			'sugar': .11,
		},
		# 'density': .60,
		'cost': 30,
		'alias': ['äpple', 'grovrivet äpple med skal'],
	},
	'raisin': {
		'content': {
			'water': .15,
			'sugar': .60,
		},
		'density': .60,
		'cost': 75,
		'alias': ['russin'],
	},
	'dried figs': {
		'content': {
			'water': .17,
			'sugar': .60,
			'fat': .01,
		},
		# 'density': .60,
		'cost': 130,
		'alias': ['torkade fikon'],
	},


	# '': {
	# 	'content': {
	# 		'flour': 0,
	# 		'water': 0,
	# 		'salt': 0,
	# 		'fat': 0,
	# 	},
	# 	'density': 1.0,
	# 	'cost': 0,
	# 	'alias': [],
	# },
}


def get_base(name: str) -> str:
	if name in data:
		return name

	for key in data:
		if name in data[key].get('alias', []):
			return key

	raise TypeError(f'Unknown ingredient: {name}')

def get_content(name: str) -> float:
	return data[get_base(name)].get('content', {})
