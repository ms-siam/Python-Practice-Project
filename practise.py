import re
heroRegex = re.compile(r'Batman|Spider man') # | is used for or , and called pipe( | )
matchObject1 = heroRegex.search('Batman and Spider man')# it will return the first occurance of the pattern
print(matchObject1.group()) #Batman

matchObject2 = heroRegex.search('Spider man and Batman')
print(matchObject2.group()) #Spider man
