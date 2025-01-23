import re
def regex_strip(string, chars):
    if chars:
        chars = re.escape(chars)
        strip = re.compile(rf'''(
                           ^[{chars}]+|[{chars}]+$
                           )''', re.VERBOSE)
        matches = strip.findall(string)
        for match in matches:
            string = re.sub(rf'{match}', '',string)
        return string
    else:
        strip = re.compile(r'''(
                           ^\s*|\s*$
                           )''', re.VERBOSE)
        matches = strip.findall(string)
        for match in matches:
            string = re.sub(rf'{match}', '',string)
        return string
    

text = input("Enter a text: ")
print(f"{regex_strip(text, 'a')}")
