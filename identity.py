# identity operators


a=[50,40]
b=[50,40]
c=a
pirnt ( a is c)
print(b is c) # it will return false becuase it is not a same object
print(a==b) # it returns true because a is== b


# is not operator returns true if it is not same object
print ( a is not c) # it returns true as it is same object
print( b is not c) # it returns ture as it is not same object
print(a!=b) # it returns false as a is equals to b
# Membership operators

# These operartors are used to test if a sequnece is present or not in an object
a=[50,60,70,80]
print(50 in a)
print(10 not in a)
# Bit wise operators
# They are used to compare Binary Numbers
# & -> ANd <- If both bits are 1, it sets each bits to 1
# | -> OR <- If one of two bits is 1, it sets each bits to 1
# ^ -> XOR <- If only one of two bits is 1, it sets each bits to 1
# # -> NOR <- It returns compliment of a bit
# << -> Zero fill left shift -> the binary number is appended with 0's at the end
# >> -> Right Shift <- In single term it removes elemnets from right side

x= 15
y= 7
print(x & y)
print(x | y)
print(x ^ y)
# print(x % y)
print(x << y)
print(x >> y)
