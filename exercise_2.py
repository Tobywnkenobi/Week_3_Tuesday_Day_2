'''

# You can also use the $ at the end of your compile expression -- this stops the search

#.com OR .org => com|org

What is a valid email?  ((group of characters)@(group).(com/.org)) THAT IS WHY THE DOLLLAR SIGN ABOVE IS USED - stops the search

#Expected output:
#None
#pocohontas1776@gmail.com
#None
#yourfavoriteband@g6.org
#None

'''
import re

my_emails = ["jordanw@codingtemple.orgcom", "pocohontas1776@gmail.com", "helloworld@aol..com",
             "yourfavoriteband@g6.org", "@codingtemple.com"]

pattern_email = re.compile('([a-z]+|[0-1]+)@([a-z]+)(.com|.org)')

found_emails = pattern_email.findall(my_emails[0])
print(found_emails)

def validateEmail(email):
    pattern = re.compile("([A-Za-z0-9]+)@([A-Za-z0-9]+).(com|org)$")

    if pattern.match(email):
        return email
    else:
        return None

for email in my_emails:
    print(validateEmail(email))