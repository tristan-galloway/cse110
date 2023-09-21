NAME_INDEX = 0
HEX_INDEX = 1
DESC_INDEX = 2

# Reads in the colors.txt file as variable name color_file
with open("colors.txt", "r") as color_file:
    # For each lin in the colors file split it into 3 columns: name, hex, and description
    for line in color_file:
        column = line.split("|")
        color_name = column[NAME_INDEX].strip()
        color_hex = column[HEX_INDEX].strip()
        color_desc = column[DESC_INDEX].strip()

        # Print the separated variables
        print(f"{color_name} ({color_hex})\n{color_desc}\n")