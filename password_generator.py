import random
letters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["_", "*", "(", ")", "/", "%"]
print("This is a code to generate password. ")
print(" ")
password = " "
n_numbers = int(input("How many numbers you want in your password: "))
for i in range(1, n_numbers+1):
	char = random.choice(numbers)
	password += char
n_letters = int(input("How many letters you want in your password: "))
for i in range (1, n_letters+1):
	char = random.choice(letters)
	password += char
n_symbols = int(input("How many symbols you want in your password: "))
for i in range (1, n_symbols+1):
	char = random.choice(symbols)
	password += char
print(" ")
password_list = list(password)
random.shuffle(password_list)
shuffled_pass = ''.join(password_list)
print(shuffled_pass)
