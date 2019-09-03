#the format() method used to insert numbers into strings.

age = 36
txt = "my name is Fatma , and I am {} "
print(txt.format(age))


#The format() method takes unlimited number of arguments, .
quantity = 3
itemno= 56
price = 49.5
txt = "I want {} pieces of item {} , for  {} dollars."
print(txt.format(quantity , itemno , price))

"""You can use index numbers {0} to be sure the arguments are placed in the
correct placeholders"""
quantity = 3
itemno= 56
price = 49.5
txt = "I want to pay {2} dollars  for {0} pieces of item {1}"
print(txt.format(quantity , itemno , price))

