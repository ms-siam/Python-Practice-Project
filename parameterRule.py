def hello(name):    #defined a function with parameter
    print('hi. ' + name)   #body of the function
hello('siam')               # 1st functtion call
try:
    print(name)             # you can't use the parameter with another function outside the body of the function

except:
    hello('esha')           #but you can use the parameter (variable : name ) anywhere in the code with the function call
# Write your code here :-)
