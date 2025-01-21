import re

phoneNumRegex = re.compile(r'(\+\d{3}) (\d{4}-\d{6})')
MatchObject = phoneNumRegex.search('My number is +880 1521-768750')
print('Phone number: ' + MatchObject.group())
print('Country Code: ' + MatchObject.group(1)) #Group(1) means first group in the regex
print('Main Number: ' + MatchObject.group(2)) #Group(2) means second group in the regex
print('Main Number with country code: ' + MatchObject.group(0)) #Group(0) means entire match
print(MatchObject.groups()) # groupS() returns a tuple of multiple values
