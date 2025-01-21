import re

phoneNumRegex = re.compile(r'\+\d{3} \d{4}-\d{6}')
MatchObject = phoneNumRegex.search('My number is +880 1521-768750')
print('Phone number: ' + MatchObject.group())