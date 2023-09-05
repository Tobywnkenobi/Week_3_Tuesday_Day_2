import re

def extract_names_and_handles(text):
    pattern = r'^([\w\s\-]+)\s+\/\s+(@[\w\-]+)$'
    
    matches = re.findall(pattern, text, re.MULTILINE)
    
    output = "==============\nFull Name / Twitter\n=============="
    for match in matches:
        output += f"\n{match[0]} / {match[1]}"
    
    return output

# Sample input
input_text = """
Derek Hawkins / @derekhawkins
Erik Sven-Osterberg / @sverik
Ryan Butz / @ryanbutz
Example Exampleson / @example
Ripal Pael / @ripalp
Darth Vader / @darthvader
"""

print(extract_names_and_handles(input_text))
