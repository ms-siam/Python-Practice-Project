import re

dateRegex = re.compile(r'''(
                       (\d{2})[-\/\.](\d{2})[-\/\.](\d{4})
                       |
                       (\w+)\s(\d{1,2})[,\s\.](d{4})
                       |
                       (\d{1,2})\s(\w+)[,\s](\d{4})
                       )''', re.VERBOSE | re.IGNORECASE)

text = "Today's date is 22-01-2025. Tomorrow's date is 23-01-2025. Yesterday's date was 21-01-2025."

matches = dateRegex.findall(text)

dates = []

for match in matches:
    if match[1] and match[2] and match[3]:
        day, month, year = match[1], match[2], match[3] 
        dates.append(f'{day}-{month}-{year}')
    
    elif match[4] and match[5] and match[6]:
        month, day, year = match[4], match[5], match[6]
        dates.append(f'{month} {day}, {year}')  
    
    elif match[7] and match[8] and match[9]:
        day, month, year = match[7], match[8], match[9]
        dates.append(f'{day} {month}, {year}')

if dates:
    print('Dates found:')
    for date in dates:
        print(date)
else:
    print('No dates found.')