'''
in class exercise #1

my_string = "This string has 10909090 numbers, but it is only 1 string. I hope you solve this 2day."

# Output: ['10909090','1',2]

'''
import re

# my_string = "This string has 10909090 numbers, but it is only 1 string. I hope you solve this 2day."

# pattern_num = re.compile('[0-9]*[0-9]')

# found_numbers = pattern_num.findall(my_string)

# found_numbers

# # Output: ['10909090','1',2]

# Importing the regex module
import re

# Redefining the string and the two regex patterns
my_string = "This string has 10909090 numbers, but it is only 1 string. I hope you solve this 2day."

# First regex pattern
pattern_num = re.compile('[0-9]*[0-9]')
found_num = pattern_num.findall(my_string)

# Second regex pattern
pattern_num_second = re.compile('[0-9]+')
found_num_second = pattern_num_second.findall(my_string)

found_num, found_num_second
