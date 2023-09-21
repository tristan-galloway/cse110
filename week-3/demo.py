_str = "kh84jdig"
# Any combination of characters

_int = 29496
# Whole numbers

_float = 4523.54
# Number with a decimal

_bool = False
# Always True or False

# Be careful of built in variables. If it's highlighting blue be wary, add a "_" or something to differentiate it


# More advanced data types that we won't use for awhile unless we want to for stretch challenges
_list = [345, 2342.5, "hey there", True]
# Lists = Array
# Any data type works

_tup = (4352, 245.5, "general kenobi", False)
# tup is read only once its created. It's not mutable

_dictionary = {} # Object in other languages



eggs = int(input("How many eggs do you have left? "))

# int(...) takes less space on the memory
# float(...) takes more space
# the difference used to matter more when computers were weaker

print(f"{type(eggs)} {eggs * 4}")