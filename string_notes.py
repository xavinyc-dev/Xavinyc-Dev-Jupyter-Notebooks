# Practice script for self practice

my_str = "hello world"


####################################################
# Three """ can let you mutli string
my_multi_string = """This
Is A Multi
String"""
print(my_multi_string)
####################################################


####################################################
# in operator checking if string contains certain characters
print(
    "hel" in my_str
)  # checks if those characters are in that string and returns a boolean
####################################################

####################################################
# Finding length of string
print(len(my_str))  # output length of the string
####################################################


####################################################
# String indexing
print(my_str[6])  # output index 6 of the string
####################################################


####################################################
# String slicing [:]
print(my_str[1:7])  # string slicing from index 1 to index 7
print(my_str[:8])  # string slicing omitting the start which python defaults to 0
print(my_str[1:7:2])  # step by 2 which means it extracts every 2nd character
print(my_str[::-1])  # -1 in step for string slicing outputting string backwards
####################################################
