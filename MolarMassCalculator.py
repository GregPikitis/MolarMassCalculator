def main():
	numberToMultiply = ""
	elementToMultiply = ""
	numbersList = []
	elements = {"H": 1.008, "He": 4.003, "Li": 6.941, "Be": 9.012, "B": 10.81, "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.179, "Na": 22.990, "Mg": 24.305, "Al": 26.982, "Si": 28.086, "P": 30.974, "S": 32.06, "Cl": 35.453, "Ar": 39.948, "K": 39.098, "Ca": 40.08, "Sc": 44.956, "Ti": 47.88, "V": 50.942, "Cr": 51.996, "Mn": 54.938, "Fe": 55.847, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.39, "Ga": 69.72, "Ge": 72.61, "As": 74.922, "Se": 78.96, "Br": 79.904, "Kr": 83.80, "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.224, "Nb": 92.906, "Mo": 95.94, "Tc": 97.907, "Ru": 101.07, "Rh": 102.906, "Pd": 106.42, "Ag": 107.868, "Cd": 112.411, "In": 114.82, "Sn": 118.710, "Sb": 121.757, "Te": 127.60, "I": 126.905, "Xe": 131.29, "Cs": 132.905, "Ba": 137.327, "La": 138.905, "Ce": 140.12, "Pr": 140.908, "Nd": 144.24, "Pm": 144.913, "Sm": 150.36, "Eu": 151.96, "Gd": 157.25, "Tb": 158.925, "Dy": 162.50, "Ho": 164.930, "Er": 167.26, "Tm": 168.934, "Yb": 173.04, "Lu": 174.967, "Hf": 178.49, "Ta": 180.948, "W": 183.85, "Re": 186.207, "Os": 190.2, "Ir": 192.22, "Pt": 195.08, "Au": 196.967, "Hg": 200.59, "TI": 204.383, "Pb": 207.2, "Bi": 208.980, "Po": 208.982, "At": 209.987, "Rn": 222.018, "Fr": 223.020, "Ra": 226.025, "Ac": 227.028, "Th": 232.038, "Pa": 231.036, "U": 238.029, "Np": 237.048, "Pu": 244.064, "Am": 243.061, "Cm": 247.070, "Bk": 247.070, "Cf": 251.080, "Es": 252.083, "Fm": 257.095, "Md": 258.099, "No": 259.101, "Lr": 262, "Rf": 261, "Db": 262, "Sg": 263, "Bh": 262, "Hs": 265, "Mt": 266}
	
	tempAdded = 0
	done = False
	finalAdd = 0
	
	while not(done):
		tempAdded = 0
		elementToMultiply = ""
		numberToMultiply = ""

		rawinput = input(">>>")
		if rawinput == "Q" or rawinput == "q":
			done = True
			break
			
		if rawinput == "help" or rawinput == "h":
			print("Very limited, sry future me. Capital and input specific. Carefull.\nNumber of atom then element. (12H) Q to quit and add all the masses up from this session.")

		if rawinput == "":
			done = True
			break
			
		for character in rawinput:
			if character.isdigit() == True:
				numberToMultiply = numberToMultiply + character
			elif character.isdigit()== False:	  
				elementToMultiply = elementToMultiply + character
				
		if numberToMultiply == "":
			numberToMultiply = 1
		
		numberToMultiply = float(numberToMultiply)
		elementToMultiply = elements[elementToMultiply]
	
		tempAdded = numberToMultiply*elementToMultiply
		print()
		print (rawinput+":",tempAdded)
		print ()
		numbersList.append(tempAdded)
		
	for item in numbersList:
		finalAdd = finalAdd + item
	
	print ()
	print ("All Together:",finalAdd)
	print ()
	


if __name__ == "__main__":
    main()
