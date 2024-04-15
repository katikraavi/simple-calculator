
from calc_functions import calculation_operation, number_is_digit

print("Hello! This is a simple calculator. Made by Kati")
continue_calculation = "y"
number_test = "()"
operator_list = ["+", "-", "*", "/"]

with open("calculation_history.txt", "a") as calc_history_file:
	calculation_history = calc_history_file.write(f"------------------\n")

print("For history press - 'h'\nFor calculation - any key")
continue_calculation_or_history = input("h / any key :")
if continue_calculation_or_history == "h":
	with open("calculation_history.txt", "r") as calc_history_file:
		calculation_history = calc_history_file.readlines()
		for line in calculation_history:
			print(line, end='')
		print("Do you want to calculate something?")
		continue_calculation = input("y/n: ")

while continue_calculation == "y":
	first_number = input("Enter first number: ")
	while number_is_digit(first_number) != "digit":
		print("please print in digits (1,2,3...etc) and use '.' instead of ','")
		first_number = input("Enter a valid first number: ")

	operator = input("Print your chosen operator (+ - * / ): ")
	while operator not in operator_list:
		operator = input("I can only help you with simple operators (+ - * / ): ")
	print(f"Your chosen operator: {operator}")
	operator = operator[0]

	second_number = input("Enter second number: ")
	while number_is_digit(second_number) != "digit":
		print("please print in digits (1,2,3...etc) and use '.' instead of ','")
		second_number = input("Enter second number: ")

	if operator == "/":
		while second_number == "0" or number_is_digit(second_number) != "digit":
			print(
				"Print in digits (1,2,3...etc), '.' instead of ','"
				"can't divide with 0 "
			)
			second_number = input(f"Calculate {first_number} / ")

	operation_result = calculation_operation(first_number, operator, second_number)

	if operation_result.is_integer():
		print("the answer is INT")
		operation_result = int(operation_result)
		result: str = f"{first_number} {operator} {second_number} = {operation_result}"
		print(result)
	else:
		operation_result = round(operation_result, 2)
		result: str = f"{first_number} {operator} {second_number} = {operation_result} "
		print(result)

	with open("calculation_history.txt", "a") as calc_history_file:
		calculation_history = calc_history_file.write(f"{result}\n")

	print("Calculate something else -> y/n history -> h")
	continue_calculation_or_history = input("y/n/h: ")
	if continue_calculation_or_history == "y":
		continue_calculation = "y"
	elif continue_calculation_or_history == "h":
		with open("calculation_history.txt", "r") as calc_history_file:
			calculation_history = calc_history_file.readlines()
			for line in calculation_history:
				print(line, end='')
			print("Do you want to calculate something else?")
			continue_calculation = input("y/n: ")
	else:
		continue_calculation = "n"

print("Save calculation history for future?")
save_history = input(f"y/n: ")
if save_history == "n":
	with open("calculation_history.txt", "w") as calc_history_file:
		calculation_history = calc_history_file.write(" Here is your history:\n")
	print("history deleted")
else:
	print("history is saved")

print("By!")
