# Coding Project CE156
# Author : Tanu Ruhela
# Date: 11 March 2023
# Description: Exercise 1 - Calculate user's age based on  his/her date of birth(American format) and return the output in European format

from datetime import date, datetime

# Input user's date of birth which will be default in string format
users_dob_str = input("Please enter your date of birth in 'mm/dd/yyyy' format: ")
try:
    # Convert string to date object in 'mm/dd/yyyy' format
    dateOfBirth = datetime.strptime(users_dob_str, "%m/%d/%Y").date()

    # Get current date when program is being executed
    currentDate = date.today()

    # Calculate user's age based on today's date (month and day)
    is_dob_greater_than_today = (dateOfBirth.month, dateOfBirth.day) > (currentDate.month, currentDate.day)

    # (not is_dob_greater_than_today) represents 1 and 0 based on the above condition
    users_age = currentDate.year - dateOfBirth.year - int(not is_dob_greater_than_today)

    # Print user's age
    print("You have turned:", users_age)

    # Print date of birth in European format('dd/mm/yyyy')
    dateOfBirth_europeanFormat = dateOfBirth.strftime("%d/%m/%Y")
    print("Your date of birth in European format (dd/mm/yyyy) is:", dateOfBirth_europeanFormat)

except ValueError:
    print("Invalid date format. PLease enter a valid date in format 'mm/dd/yyyy'")