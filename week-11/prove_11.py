"""

student: tristan galloway
teacher: brother keers
file: prove_11
assignment: open the file, read through it line by line, strip off leading and trailing whitespace and display each book to the screen.

"""

max_life = 0
min_life = 999999

COUNTRY_INDEX = 0
ID_INDEX = 1
YEAR_INDEX = 2
LENGTH_INDEX = 3

print("Welcome to the life expectancy data set.")

with open("life-expectancy.csv", "r") as expectancy_file:

    for line in expectancy_file.readlines()[1:]:

        # Splitting the columns in the .csv file at the comma's
        column = line.split(",")

        # Setting a variable name for the given set index value
        country = column[COUNTRY_INDEX].strip()
        country_id = column[ID_INDEX].strip()
        data_year = int(column[YEAR_INDEX].strip())
        life_length = float(column[LENGTH_INDEX].strip())

        # W11: What is the year and country that has the lowest life expectancy in the dataset?
        if life_length < min_life:
            min_life = life_length

        # W11: What is the year and country that has the highest life expectancy in the dataset?
        if life_length > max_life:
            max_life = life_length

        # Read through the data and print it with "-" in between each column
        print(f"{country} - {country_id} - {data_year} - {life_length}")

    print(f"\nThe overall max life expectancy is: {max_life}")
    print(f"The overall min life expectancy is: {min_life}")


# w12: Allow the user to type in a year, then, find the average life expectancy for that year. Then find the country with the minimum and the one with the maximum life expectancies for that year.
