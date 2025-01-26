import pyinputplus as pyip
response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], 
blockRegexes=[r'cat'])
print(response)