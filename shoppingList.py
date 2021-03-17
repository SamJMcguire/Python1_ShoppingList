'''Shopping List exercise

This is a demonstration of how to complete the shopping list task. The shopping list contains user generated lists, boolean while loops, selection
I always start a program with a docstring'''

#Set variables: user_items as empty list, and add_more as True
user_items = ['']
add_more = True

#Set user input name - greet user
name = input("What is your name"  ?)
print("Hello {}.  Let's make a list!" .format(name))

#Begin loop (loop while add_more True)
while add_more == True:
#User input  add item to user_items
    item = input("What would you like to add?  ")
#add user item
    user_items = user_items.append(item)
#Selection check add_more is still true - loop or else 
    more_items = input("Would you like to add more items?  Y/N")
    if more_items == "Y":
        add_more = True
    else:
  #Print "name" the items on you list are [print list]
        print("{} The items on your list are {}". format(name, user_items))

