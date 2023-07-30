name = input("Enter your name:")
Class = input('Enter your class:')
sum_ = 0
subject_flag = False


#For Class FSCM
if Class  == 'fscm':
	print("Enter Your Number:")
	urdu = int(input('Urdu:'))
	if urdu <= 100 and urdu >= 0:
		sum_ = sum_ + urdu
	else:
		subject_flag = True
		sum_ = sum_ + 0
	pakst = int(input('Pakst:'))
	if pakst <= 100 and pakst >= 0:
		sum_ = sum_ + pakst
	else:
		subject_flag = True
		sum_ = sum_ + 0
	isl = int(input('Isl:'))
	if isl <= 100 and isl >= 0:
		sum_ = sum_ + isl
	else:
		subject_flag = True
		sum_ = sum_ + 0
	chem = int(input('Chem:'))
	if chem <= 100 and chem >= 0:
		sum_ = sum_ + chem
	else:
		subject_flag = True
		sum_ = sum_ + 0
	bio = int(input('Bio:'))
	if bio <= 100 and bio >= 0:
		sum_ = sum_ + bio
	else:
		subject_flag = True
		sum_ = sum_ + 0
	phy = int(input('Phy:'))
	if phy <= 100 and phy >= 0:
		sum_ = sum_ + phy
	else:
		subject_flag = True
		sum_ = sum_ + 0
	eng = int(input('Eng:'))
	if eng <= 100 and eng >= 0:
		sum_ = sum_ + eng
	else:
		subject_flag = True
		sum_ = sum_ + 0


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

	if subject_flag:
		print("Note: some of your input is incorrect so it will effect on your results.")

#For Class FSCE	
elif Class  == 'fsce':
	print("Enter Your Number:")
	urdu = int(input('Urdu:'))
	if urdu <= 100 and urdu >= 0:
		sum_ = sum_ + urdu
	else:
		subject_flag = True
		sum_ = sum_ + 0
	pakst = int(input('Pakst:'))
	if pakst <= 100 and pakst >= 0:
		sum_ = sum_ + pakst
	else:
		subject_flag = True
		sum_ = sum_ + 0
	isl = int(input('Isl:'))
	if isl <= 100 and isl >= 0:
		sum_ = sum_ + isl
	else:
		subject_flag = True
		sum_ = sum_ + 0
	chem = int(input('Chem:'))
	if chem <= 100 and chem >= 0:
		sum_ = sum_ + chem
	else:
		subject_flag = True
		sum_ = sum_ + 0
	math = int(input('math:'))
	if math <= 100 and math >= 0:
		sum_ = sum_ + math
	else:
		subject_flag = True
		sum_ = sum_ + 0
	phy = int(input('Phy:'))
	if phy <= 100 and phy >= 0:
		sum_ = sum_ + phy
	else:
		subject_flag = True
		sum_ = sum_ + 0
	eng = int(input('Eng:'))
	if eng <= 100 and eng >= 0:
		sum_ = sum_ + eng
	else:
		subject_flag = True
		sum_ = sum_ + 0
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

	if subject_flag:
		print("Note: some of your input is incorrect so it will effect on your results.")
#For class ICS
elif Class  == 'ics':
	print("Enter Your Number:")
	urdu = int(input('Urdu:'))
	if urdu <= 100 and urdu >= 0:
		sum_ = sum_ + urdu
	else:
		subject_flag = True
		sum_ = sum_ + 0
	pakst = int(input('Pakst:'))
	if pakst <= 100 and pakst >= 0:
		sum_ = sum_ + pakst
	else:
		subject_flag = True
		sum_ = sum_ + 0
	isl = int(input('Isl:'))
	if isl <= 100 and isl >= 0:
		sum_ = sum_ + isl
	else:
		subject_flag = True
		sum_ = sum_ + 0
	comp = int(input('Comp:'))
	if comp <= 100 and comp >= 0:
		sum_ = sum_ + comp
	else:
		subject_flag = True
		sum_ = sum_ + 0
	math = int(input('Math:'))
	if math <= 100 and math >= 0:
		sum_ = sum_ + math
	else:
		subject_flag = True
		sum_ = sum_ + 0
	phy = int(input('Phy:'))
	if phy <= 100 and phy >= 0:
		sum_ = sum_ + phy
	else:
		subject_flag = True
		sum_ = sum_ + 0
	eng = int(input('Eng:'))
	if eng <= 100 and eng >= 0:
		sum_ = sum_ + eng
	else:
		subject_flag = True
		sum_ = sum_ + 0
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

	if subject_flag:
		print("Note: some of your input is incorrect so it will effect on your results.")




