import re

dateRegex = re.compile(r'''(
                       (\d\d)
                       (\s\-\.\/)
                       (\d\d)
                       (\s\-\.\/)
                       (\d{4})
                       |
                       (\w+)
                       (\s)
                       (\d{1,2})
                       (\s\,\.\/)
                       (\d{4})
                       |
                       (\d{1,2})
                       (\s)
                       (\w+)
                       (\s\,\.\/)
                       (\d{4})
                       )''', re.VERBOSE | re.IGNORECASE)

text = "Today's date is 01-01-2020. Tomorrow's date is 02-01-2020. Yesterday's date was 31-12-2019."

matches = dateRegex.findall(text)

dates = []

for match in matches:
    if match[1] and match[3] and match[5]:
        day, month, year = match[1], match[3], match[5] 
        dates.append(f'{day}-{month}-{year}')
    
    elif match[6] and match[8] and match[10]:
        month, day, year = match[6], match[8], match[10]
        dates.append(f'{month} {day}, {year}')  
    
    elif match[11] and match[13] and match[15]:
        day, month, year = match[11], match[13], match[15]
        dates.append(f'{day} {month}, {year}')

if dates:
    print('Dates found:')
    for date in dates:
        print(date)
else:
    print('No dates found.')