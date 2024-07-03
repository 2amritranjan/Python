size= input("Welcome to Domino's \n What would you like to have(S/M/L): ")
bill = 0
if size == 'S' or size =='s':
	bill += 100
	print(f"For small size pizza you need to pay {bill} rupees. ")
elif size == 'm' or size == 'M':
	bill += 200
	print(f"For medium size pizza you need to pay {bill} rupees. ")
elif size == 'l' or size == 'L':
	bill += 300
	print(f"For big size pizza you need to pay {bill} rupees. ")
else:
	print("Wrong input please try again. ")
add_peppo = input("Do you want to add pepparoni (Y/N): ")
if size == 'S' or size =='s':
		if add_peppo == "y" or add_peppo == "Y":
			bill += 30
		else:
				bill == 100
elif size == 'm' or size == 'M':
								  if add_peppo == "y" or add_peppo == "Y":
								        bill += 50
								  else:
								   	bill == 200
elif size == 'l' or size == 'L':
						    				if add_peppo == "y" or add_peppo == "Y":
						    				        bill += 50
						    				else:
						    					bill == 300
extra_cheese= input("Do you want to add cheese for ₹20 extra only?(Y/N): ")
if size == 'S' or size =='s':
			if extra_cheese =='y' or extra_cheese == 'Y':
				bill += 20
			else:
				bill == 100
elif size == 'm' or size =='M':
			if extra_cheese =='y' or extra_cheese == 'Y':
				bill += 20
			else:
				bill == 200
elif size == 'l' or size =='L':
			if extra_cheese =='y' or extra_cheese == 'Y':
				bill += 20
			else:
				bill == 300
print(f"Your final bill amout is ₹{bill} only, Thankyou. ")
