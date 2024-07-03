print("Blue Moon Burger welcomes you to our ordering site. \nWish you have your best experince of burgers with us. ")
print(" ")
non_veg = ("Chicken burger @ ₹79", "Chicken tikka Maharaja @ ₹99", "Mutton tikka Maharaja @ ₹119" )
veg = ("Plain Veg Burger @ ₹39","Veggy loaded Burger @ ₹59", "Veg Maharaja @ ₹79 ")
property = input("Tell me your current location: ").lower()
if property in (('kochas'), ('sasaram'), ('buxar'), ('patna'), ('varanasi'), ('delhi'), ('kolkata'), ('ara'), ('mohaniya'), ('chennai'), ('bangalore')):
	print(" ")
	print(f" Property entered is:- {property}")
	print(" ")
	print("Welcome to Blue Moon Burgers. \n We are the Largest Burger chains deliverig in more than 50+ locations in your locality. ")
	print(" ")
	order = input(" What woul you like to have (veg /non-veg): ").lower()
	if order in ("nonveg", "non veg", "non-veg", "n", "nv"):
		print(" ")
		norder_id = input(f"We have 3 differnt variety of non-veg burgers {non_veg} type(1/2/3) to order of your choice. ")
		if norder_id == "1":
			print(" ")
			print(f" Your order of chicken burger is beinged ready, Please pay ₹79 to the counter.\n Thankyou. ")
		elif norder_id == "2":
			print(" ")
			print(f" Your order of chicken tikka maharaja is beinged ready, Please pay ₹99 to the counter.\n Thankyou. ")
		elif norder_id =="3":
			print(" ")
			print(f" Your order of mutton tikka maharaja is beinged ready, Please pay ₹119 to the counter.\n Thankyou. ")
		else:
			print("Wrong inout please try again. ")
	elif order in ("veg", "v"):
			print(" ")
			vorder_id = input(f" We have 3 different variety of veg burgers {veg} type (1/2/3) to order of your choice. ")
			if vorder_id == "1":
				print(" ")
				print(f" Your order of plain veg burger is beinged ready, Please pay ₹39 to the counter.\n Thankyou. ")
			elif vorder_id =="2":
				print(" ")
				print(f" Your order of veggy loaded burger is beinged ready, Please pay ₹59 to the counter.\n Thankyou. ")
			elif vorder_id =="3":
				print(" ")
				print(f" Your order of veg maharaja is beinged ready, Please pay ₹79 to the counter.\n Thankyou. ")
			else:
				print("Wrong inout please try again. ")
	else:
			print("Wrong inout please try again. ")
			
elif property in (" "):
	print(" ")
	print(" Wrong input please try again. ")
	
else:
	print(" ")
	print(f"We are sorry as our Outlet is opening soon in {property}, sorry for inconvenience. ")
	
	