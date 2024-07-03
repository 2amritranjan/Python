weight=input("enter your weight in kg ")
height=input("enter your height in meter ")
bmi=int(weight)/(float(height)**2)
print("bmi "+"=" + str(bmi))
if bmi<16:
	print("You are severly underweight. ")
elif bmi<16.9:
	print("You are moderately Underweight. ")
elif bmi<18.4:
	print("You are underweight. ")
elif bmi<24.9:
	print("You are in healthy range. ")
elif bmi<29.9:
	print("You are overweight. ")
elif bmi<34.9:
	print("You are moderately overweight. ")
elif bmi<39.9:
	print("You are severly overweight. ")
elif bmi>=40:
	print("You are respondsible for global warming my friend please commit suicide. ")
print("Thankyou")


	
	

		