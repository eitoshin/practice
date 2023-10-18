to_seconds = 24 * 60 
name_of_unit = "seconds"

def days_to_units(num_of_days):
    return f"{num_of_days} days are  {num_of_days * to_seconds} {name_of_unit}"

#mv_var = days_to_units(20)
#print(mv_var)

user_input = input("hey enter number of days and I will covert it to hours!\n")
user_input_number = int(user_input)

#print(user_input)
calc_value = days_to_units(user_input_number)
print(calc_value)