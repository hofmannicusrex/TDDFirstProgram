"""
Program: camper_age_input_hofmann.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/3/2020

Program specifications: The program will have will prompt for the age of one infant (age 1-5 years)
who is attending camp and convert the age in months to years via a function call then print the result.
"""


# Function to convert the user's input from years to months
def convert_to_months(years):
    # There are 12 months in a year so we divide by 12 to get the number of years.
    return int(years / 12)  # Casting to an int


if __name__ == '__main__':
    # Casting the user's input to a float and then an int since I assume we want integer results.
    camper_age = int(float(input("Enter the age of the camper in months: ")))

    print("\nThe camper's age in years:", convert_to_months(camper_age))

# End of camper_age_input_hofmann.py
