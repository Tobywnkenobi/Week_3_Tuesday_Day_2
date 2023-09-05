# DESCRIPTION:
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= length of input <= 100

# All inputs will be strings, consisting only of characters ( and ).
# Empty strings are considered balanced (and therefore valid), and will be tested.
# For languages with mutable strings, the inputs should not be mutated.

# Protip: If you are trying to figure out why a string of parentheses is invalid, paste the parentheses into the code editor, and let the code highlighting show you!


def parentheses_valid(parentheses):
    
    parentheses_counter = 0
    for x in parentheses:
        if x == "(":
            parentheses_counter += 1
        elif x == ")":
            parentheses_counter -= 1
            if parentheses_counter < 0:
                return False
    if parentheses_counter == 0:
        return True
    else:
        return False

print(parentheses_valid(")()("))

