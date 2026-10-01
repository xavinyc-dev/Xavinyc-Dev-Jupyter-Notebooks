my_str = "Hello World!"

### String Methods###
# String methods always begin with .
# upper() - Upper case the entire string by using upper()
uppercase_my_str = my_str.upper()  # .upper() prints string in all uppercase
print(uppercase_my_str)

# lower() - Lower case entire string by adding .lower()
lowercase_my_str = my_str.lower()  # .lower() prints string in all lowercase
print(lowercase_my_str)

# strip() Returns new string with specified leading and trailers characters removed. If no argument it removes whitespace
messy_str = "     Hello World   \n"
stripped_messy_str = my_str.strip()
print(stripped_messy_str)

# replace(old, new) - returns a new string with everything in old replaced with new
replaced_my_str = my_str.replace("Hello", "Hi")
print(replaced_my_str)

# split(separator) - splits a string on a specified separator, not including the separator, into a list of strings. If no separator is specified, split() splits on whitespace
split_my_str = my_str.split()
print(split_my_str)

# join() - takes a list of strings and joins the strings together into one string
my_list = ["Hello", " World!"]
joined_str = "".join(my_list)
print(joined_str)


####################################################
