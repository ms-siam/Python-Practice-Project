catNames = []
while True:
    print(
        "Enter the name of cat "
        + str(len(catNames) + 1)
        + "(Or Enter nothing to stop) :"
    )
    name = input()
    if name == "":
        break
    catNames = catNames + [name]
print("The cat names are: ")
for x in range(len(catNames)):
    print(catNames[x])  # Write your code here :-)

#for name in catNames:
 #   print( name)
