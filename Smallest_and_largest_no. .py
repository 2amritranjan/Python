print("This is the program to find out larget and smallest number from given input. ")
print(" ")
numbers = input("Enter your numbers here separated by comma (x,y,z): ")
num_list = numbers.split(",")
int_num= [eval(i) for i in num_list]
print(" ")
print(f"Your entered no. is:- {int_num} ")
largest_num = max(int_num)
smallest_num = min(int_num)
print(" ")
print(f"Largets number is:- {largest_num}")
print(f"Smallest number is:- {smallest_num} ")

