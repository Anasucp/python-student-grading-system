name = input("Enter your name:")
Class = input('Enter your class:')

#For Class FSCM
if Class  == 'fscm':
	print("Enter Your Number:")
	urdu = input('Urdu:')
	if urdu > 100:
		print ("Score must be under 100")
	pakst = input('Pakst:')
	if pakst > 100:
		print ("Score must be under 100")
	isl = input('Isl:')
	if isl > 100:
		print ("Score must be under 100")
	chem = input('Chem:')
	if chem > 100:
		print ("Score must be under 100")
	bio = input('Bio:')
	if bio > 100:
		print ("Score must be under 100")
	phy = input('Phy:')
	if phy > 100:
		print ("Score must be under 100")
	eng = input('Eng:')
	if eng > 100:
		print ("Score must bet under 100")
	sum_ = int(urdu) + int(pakst) + int(isl) + int(chem) + int(bio) + int(phy) + int(eng)
	percent = (sum_ / 700) * 100
	print (f"Name:{name}")
	print (f"Class:{Class}")
	print  (f"Total:{sum_}/700 ")
	print (f"Percentage:{percent}")
	if percent > 80:
		print ("Grade:A")

	elif percent > 50:
		print ("Grade:B")

	else:
		print ("Grade:F")

#For Class FSCE	
elif Class  == 'fsce':
	print("Enter Your Number:")
	urdu = input('Urdu:')
	if urdu > 100:
		print ("Score must be under 100")
	pakst = input('Pakst:')
	if pakst > 100:
		print ("Score must be under 100")
	isl = input('Isl:')
	if isl > 100:
		print ("Score must be under 100")
	chem = input('Chem:')
	if chem > 100:
		print ("Score must be under 100")
	math = input('math:')
	if math > 100:
		print ("Score must be under 100")
	phy = input('Phy:')
	if phy > 100:
		print ("Score must be under 100")
	eng = input('Eng:')
	if eng > 100:
		print ("Score must be under 100")
	sum_ = int(urdu) + int(pakst) + int(isl) + int(chem) + int(math) + int(phy) + int(eng)
	percent = (sum_ / 700) * 100
	print (f"Name:{name}")
	print (f"Class:{Class}")
	print  (f"Total:{sum_}/700 ")
	print (f"Percentage:{percent}")
	if percent > 80:
		print ("Grade:A")

	elif percent > 50:
		print ("Grade:B")

	else:
		print ("Grade:F")

#For class ICS
elif Class  == 'ics':
	print("Enter Your Number:")
	urdu = input('Urdu:')
	if urdu > 100:
		print ("Score must be under 100")
	pakst = input('Pakst:')
	if pakst > 100:
		print ("Score must be under 100")
	isl = input('Isl:')
	if isl > 100:
		print ("Score must be under 100")
	comp = input('Comp:')
	if comp> 100:
		print ("Score must be under 100")
	math = input('Math:')
	if map > 100:
		print ("Score must be under 100")
	phy = input('Phy:')
	if phy > 100:
		print ("Score must be under 100")
	eng = input('Eng:')
	if eng > 100:
		print ("Score must be under 100")
	sum_ = int(urdu) + int(pakst) + int(isl) + int(comp) + int(Math) + int(phy) + int(eng)
	percent = (sum_ / 700) * 100
	print (f"Name:{name}")
	print (f"Class:{Class}")
	print  (f"Total:{sum_}/700 ")
	print (f"Percentage:{percent}")
	if percent > 80:
		print ("Grade:A")

	elif percent > 50:
		print ("Grade:B")

	else:
		print ("Grade:F")





