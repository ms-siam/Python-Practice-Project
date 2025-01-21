import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') #instead of (r'Batman | Batmobile | Batcopter | Batbat')
matchObject = batRegex.search('Batman lost his bat while driving Batmobile')
print(matchObject.group())
print(matchObject.group(1)) #group(1) will return the first group of the matched string

batRegex1 = re.compile(r'Bat(wo)?man') # ? means optional 
matchObject1 = batRegex1.search('The adventures of Batman')  
print(matchObject1.group()) # Batman
matchObject2 = batRegex1.search('The adventures of Batwoman')
print(matchObject2.group()) # Batwoman