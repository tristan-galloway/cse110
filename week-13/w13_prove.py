"""

student: tristan galloway
teacher: brother keers
file: prove_13
assignment: Calculate for wind chill with user given tempurature.

"""

# Ask the user for the tempurature and what measurement system they are using
temp = float(input("What is the tempurature? "))
symbol = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

# If the user inputs the tempurature is Celsius convert it to Farhenheit
def cel_to_far(cel):
    return cel * 9/5 + 32

# Calculations for figuring out the windchill based on the input tempurate and wind speed
def windchill(temp, speed):
    return  35.74 + 0.6215 * temp - 35.75 * (speed ** 0.16) + 0.4275 * temp * (speed ** 0.16)

# If the user inputs "C" run the conversion function
if symbol == "C":
    temp = cel_to_far(temp)

# Loop through generating the windchill for each windspeed going from 5mph - 60mph
for wind_speed in range(5, 61, 5):

    wc = windchill(temp, wind_speed)

    print(f"At tempurature {temp}F, and wind speed {wind_speed} mph, the windchill is: {wc:.2f}F")