#! python3
import pyperclip, re

phoneRegex = re.compile(r'''(
            (\+?\d{3})?                     # country code
            (\s|-)?                         # separator
            (\d{4})                         # first 4 digits
            (\s|-)?                         # separator
            (\d{6})                         # last 6 digits
            (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
            )''', re.VERBOSE)

emailRegex = re.compile(r'''(
                        ([^-]\w{,64}\d*)        # username
                        @                       # separator
                        (\w+?mail\.\w{2,3}|com) # domain
                        )''', re.VERBOSE)

text = str(pyperclip.paste())   
matches = []    
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')