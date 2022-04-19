
# i = 0 # iterator / incrementor
# while i < 10:
#     print("Hello World! " + str(i)) 
#     i += 1 # i = i + 1 (samething)

# num = 1 
# while num <= 5:
#     print (num)
#     num += 1 # Increase the value of num by 1

# print ("This program displays a famous movie quotation.")
# responses = ('1', '2', '3')
# response = '0'
# while response not in responses: 
#     response = input ("Enter 1, 2, or, 3: ")
#     if response == '1':
#         print ("Plastics.")
#     elif response == '2':
#         print("Rosebud.")
#     elif response == '3':
#         print ("That's all folks. ")

# count = 0  
# total = 0 
# print("(Enter -1 to terminate entering numbers.)")
# num = eval(input("Enter a nonnegative number: "))
# min = num
# max = num 
# while num != -1:
#     count += 1
#     total += num 
#     if num < min:
#         min = num
#     if num > max: 
#         max = num
#     num = eval(input("Enter a nonegative number: "))
# if count > 0:
#     print("Minimum:", str(min))
#     print("Maximum:", str(max))       
#     print("Average:", str(total / count))
# else: 
#     print("No nonnegative numbers were entered.")

# list1 = [300, 1, 2, 3, 60]
# list1.sort() # [1, 2, 3, 60, 300]
# list1[0] # 1 - Lowest number in the list
# list1[-1] # 300 - Largest number in the list

# numberofyears = 0
# balance = eval (input("Enter initial deposit: "))
# while balance < 1000000:
#     balance += .04 * balance
#     numberofyears += 1
# print("In", numberofyears, "years you will have a million dollars.")

# i = 0
# balance = eval(input("Enter initial deposit: "))
# rate = eval(input("Enter the annual rate of return: "))
# while balance < 1000000:
#     balance += .04 * balance
#     i += 1
# print("In", str(i), "years you will have a million dollars")

# list1 = []
# while True:
#     num = eval(input("Enter a nonnegative number: "))
#     if num == -1:
#         break  # Immediately terminate the loop
#     list1.append(num)
# print(list1)

# print("Enter a number from the menu to obtain a fact")
# print("about the United States or to exit the program.\n")
# print("1. Capital")
# print("2. National Bird")
# print("3. National Flower")
# print("4. Quit\n")
# while True:
#     num  = int(input("Make a selection from the menu: "))
#     if num == 1:
#         print("Washington, DC is the capital of the United States.")
#     elif num == 2: 
#         print("The American Bald Eagle is the national bird.")
#     elif num == 3:
#         print("The Rose is the national flower.")
#     elif num == 4:
#         break

 
