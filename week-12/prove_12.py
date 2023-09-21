"""

student: tristan galloway
teacher: brother keers
file: prove_11
assignment: open the file, read through it line by line, strip off leading and trailing whitespace and display each book to the screen.

"""

max_life = 0
max_country = ""
max_year = 0
min_life = 999999
min_country = ""
min_year = 0

COUNTRY_INDEX = 0
ID_INDEX = 1
YEAR_INDEX = 2
EXPECT_INDEX = 3

print("Welcome to the life expectancy data set.")

year_of_int = int(input("What year would you like to know the min and max life expectancy? "))
int_max = 0
int_country_max = ""
int_min = 999999
int_country_min = ""
# This will get a sum of all the years
int_life_expec = 0
# Count will stand for how many times we have successfully added to the in_life_ecpec var
count = 0

with open("life-expectancy.csv", "r") as expec_file:

    for line in expec_file.readlines()[1:]:

        # Splitting the columns in the .csv file at the comma's
        column = line.split(",")

        # Setting a variable name for the given set index value
        country = column[COUNTRY_INDEX].strip()
        country_id = column[ID_INDEX].strip()
        data_year = int(column[YEAR_INDEX].strip())
        life_expect = float(column[EXPECT_INDEX].strip())

        # W11: What is the year and country that has the lowest life expectancy in the dataset?
        if life_expect < min_life:
            min_life = life_expect
            min_country = country
            min_year = data_year

        # W11: What is the year and country that has the highest life expectancy in the dataset?
        if life_expect > max_life:
            max_life = life_expect
            max_country = country
            max_year = data_year

        # W12: See if the current year is the users year of int and the LARGEST number so far.
        if year_of_int == data_year and life_expect > int_max:
            int_max = life_expect
            int_country_max = country

        # W12: See if the current year is the users year of int and the SMALLEST number so far.
        if year_of_int == data_year and life_expect < int_min:
            int_min = life_expect
            int_country_min = country

        # for all of the years that line up with the user input, add them together
        if year_of_int == data_year:
            int_life_expec += life_expect
            count += 1

        # Read through the data and print
        # it with "-" in between each column
        # print(f"{country} - {country_id} - {data_year} - {life_expect}")

    # This will do the math with the previous variables to give the average life expectancy
    int_av = int_life_expec / count

    print(f"\nThe overall max life expectancy is {max_life} years in {max_country} in the year {max_year}")
    print(f"The overall min life expectancy is {min_life} years in {min_country} in the year {min_year}")
    
    print(f"\nIn the year {year_of_int} the longest life expectancy was {int_max} in {int_country_max}")
    print(f"In the year {year_of_int} the shortest life expectancy was {int_min} in {int_country_min}")
    print(f"The average life expectancy for the year {year_of_int} was {int_av}")