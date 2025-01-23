import re
def regex_strip(string, chars=None):
    if chars:
        chars = re.escape(chars)
        strip = re.compile(rf'''(
                           ^[{chars}]+|[{chars}]+$
                           )''', re.VERBOSE)
        matches = strip.findall(string)
        string = strip.sub('', string)
    else:
        strip = re.compile(r'''(
                           ^\s*|\s*$
                           )''', re.VERBOSE)
        matches = strip.findall(string)
        string = strip.sub('', string)
    return string
text = input("Enter a text: ")
print(f"{regex_strip(text, 's')}")
