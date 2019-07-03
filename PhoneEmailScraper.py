#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-666-6666, 555-555-3424, (454)555-4354, 555-0000 ext 12345, 555-7000 x12345


(                                      # this starts a whole group so findall does not print tuples, line 18 ends group 
((\d\d\d)|(\(\d\d\d\)))?               # area code (optional)
(\s|-)                                 # first separator
\d\d\d                                 # first three digits
-                                      # separator
\d\d\d\d                               # last four digits
(((etx(\.)?\s) |x)                     # extension word part (optional)
(\d{2,5}))?                            # extension number part(optional)
)
 

''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# example@example.com, some.+_thing@something.com

[a-zA-Z0-9_.+]+                       # name part (created a character class in the brackets)
@                                     # @ symbol
[a-zA-Z0-9_.+]+                       # domain name part


''', re.VERBOSE)

# Get the text off the clipboard

text = pyperclip.paste()

# Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhonenumbers = [] # because findall is printing tuples we need to tell it to find each group and print only item zero
for phoneNumber in extractedPhone:
    allPhonenumbers.append(phoneNumber[0])

# print(extractedEmail) we used this to test before moving forward
# print(allPhonenumbers) we used this to test before moving forward

# Copy the extracted email/phone to the clipboard

# join method takes a list of strings and joins them together in a single string
# we add newline char so that we get a new line between each phone number in the string we print

results = '\n'.join(allPhonenumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results) #copies results to the clipboard
print(results)

