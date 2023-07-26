"""
#Using if, elif, else to search output based on names
name = input("Whats your name? ")

if name == "Harry" or name == "Daryl":
  print("Orchard Road")

elif name == "JJ":
  print("Bedok")

else:
  print("No record")

"""

#Using fn "match" to achieve the same 
name = input("what's your name? ") 

match name:
    case "Harry" | "JJ" | "Tim":
      print("Orchard Rd")
# "_" here means "catchall"
    case _ :
      print("Who's that? ")





