name = input("What is your name: ")
age = int(input(f"Ok {name}, can you tell me your current age: "))
years_left = 90 - age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12
print(f"Surprise {name}, you have only {days_left} days or {weeks_left} weeks or {months_left} months left only so enjoy every moment out of it. ")