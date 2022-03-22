

# Relational Operator
# <, <=, >, >=, !=, ==
# Logical Operator 
# and, or, not 

# true_or_false = "b" > "a" # True
# true_or_false = "z" < "!" # False 
# true_or_false = "Z" < "!" and "b" > "a" # False
# true_or_false = "z" < "!" or "b" > "a" # True, it just needs one to be true in order to make the whole thing true
# true_or_false = not("z" < "!" or "b" > "a") # False
# print("true or false", true_or_false)

# true_or_false = [3,5] < [3,7] 
# true_or_false = [3,5] < [3,5,6]
# true_or_false = [3,5,7] < [3,7,2] 
# true_or_false = [7,"three",5] < [7,"two",2] 
# print("true or false", true_or_false)

# list1 = [6,4,-5,3.5]
# print(list1)
# list1.sort()
# print(list1)

# list2= ["ha","hi","B", "7"]
# print(list2)
# list2.sort()
# print(list2)

state = "CA" 
states = ["MD", "VA", "WV", "DE"]
is_in_list = state in states 
print(not(is_in_list)) #true because CA is not in the list
print(not(is_in_list) and "VA" in states) # True True
