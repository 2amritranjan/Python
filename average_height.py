print(" This is a program to find average height. \n The given values is in centimeters.")
print(" ")
#height of everyone
height= input("Enter everyone's height separeted with + sign(like x + y + z): ")
#converting height into list using split function
height_list =(height.split("+"))
#converting height_list (str) in (int) using eval()
int_height = [ eval(i) for i in height_list]
#adding every element of int_height using Sum()
sum = (sum(int_height))
#calculating the count of height using len()
length = len(height_list)
average = sum/length
print(f" The averge height of given values are {average} in cm. ")
