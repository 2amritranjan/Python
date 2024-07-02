print("This is a programe to check if a given year is leap year or not. ")
print(" ")
print(" ")
year=int(input("Type any year you want to check: "))
if year % 4==0:
	if year % 100==0:
				if year % 400==0:
					print(f"Yes, {year} is a leap year. ")
				else:
					print("No, entered year is not a leap year. ")
	else:
		print(f"Yes, {year} is a leap year. ")
		
else:
	print("Entered year is not a leap year. ")