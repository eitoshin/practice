to_seconds = 24 * 60 
name_of_unit = "seconds"

def days_to_units(num_of_days):
    condition_check = num_of_days >0
    print(type(condition_check))
    print(num_of_days > 0)


    if num_of_days > 0:
        return f"{num_of_days} days are  {num_of_days * to_seconds} {name_of_unit}"
    elif num_of_days == 0:
        return "you enterde 0. please a vaild positive number."
    else:
        return "you entered a negative value"

#mv_var = days_to_units(20)
#print(mv_var)

user_input = input("hey enter number of days and I will covert it to hours!\n")

if user_input.isdigit():
    user_input_number = int(user_input)
#   print(user_input)
    calc_value = days_to_units(int(user_input))
    print(calc_value)
else:
    print("your input number is not integer!")

#print(type(30.99))

