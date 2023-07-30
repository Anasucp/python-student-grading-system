name = input("Enter your name:")
Class = input('Enter your class:')

#For Class FSCM
if Class  == 'fscm':
	print("Enter Your Number:")
	urdu = int(input('Urdu:'))
	pakst = int(input('Pakst:'))
	isl = int(input('Isl:'))
	chem = int(input('Chem:'))
	bio = int(input('Bio:'))
	phy = int(input('Phy:'))
	eng = int(input('Eng:'))
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
	urdu = int(input('Urdu:'))
	pakst = int(input('Pakst:'))
	isl = int(input('Isl:'))
	chem = int(input('Chem:'))
	math = int(input('math:'))
	phy = int(input('Phy:'))
	eng = int(input('Eng:'))
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
	urdu = int(input('Urdu:'))
	pakst = int(input('Pakst:'))
	isl = int(input('Isl:'))
	chem = int(input('Chem:'))
	bio = int(input('Bio:'))
	phy = int(input('Phy:'))
	eng = int(input('Eng:'))
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





