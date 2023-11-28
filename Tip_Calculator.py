print("Welcome to tip calculator.")
total_bill=float(input("What was the total bill? $"))
percentage_of_tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_prople=int(input("How many people to split the bill? "))
total_tip_amount=total_bill*(percentage_of_tip*0.01)
split_bill=((total_bill + total_tip_amount ) / no_of_prople)
final_amount="{:.2f}".format(split_bill) #Formating the amount up to 2 decimal place
print(f"Each person should pay: ${final_amount}")