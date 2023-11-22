#   to  Everyone
# As a wedding planner, you are writing code to track who to invite to a wedding. You don’t know in advance how many people your clients may invite. Create a list. In a loop, ask the user "Enter a guest's name or type 'end' to stop."
# Add the guest’s name to the list. A value of “end” will stop the loop. Continue to add names to the list until “end” is entered by the user. The user may enter “end”, “End”, “END” and code should break out of the loop being case-insensitive.
# After the loop, print the list of invited guests.
# Multiply the count of guests by $12 to get a total cost of the food for the wedding. Display the message “You have invited 10 guests at a cost of $120.00 for food.” Replace 10 and 120.00 with the appropriate values. The output will look like Figure 6. The quantity and the names of the guests are of your choosing, as long as the code works and calculates the cost.
# Blezed  to  Everyone 4:40 PM
# Hints:
# • Consider breaking this unstructured task into smaller tasks. Test each smaller
# task to make sure your code works. Real-world clients give you unstructured
# problems that you have to organize into code.
# • Consider NOT coding a while loop until later. Code as if you were only inviting
# one guest. Print the guest list, calculate everything else, print what you need to print. Then after that code is working, add a while loop. This approach will be much easier to identify where problems are and fix them.
# • Use a while loop with condition of (true). In the while loop, use an if statement to check if “end” was entered by the user, then break, else add the name to the list.
# You can use the .lower() method to make the comparison case-insensitive for “end”. 
# • What’s the comparison operator for equality used in an if statement? One equal sign or two equal signs? • Look for syntax errors identified by red underline text. Sometimes the syntax error is to the left of the red underlined text or on the line above the red underlined text. Hover over the red underline to see if the linter explains the error.
# • Remember your indentation. Improper indentation can cause errors.
# • Manage your struggles and frustration. It's very normal to make many mistakes
# as we code, even for professional developers. Coding in a process with many experiments 

# solution

invited=[]
food=[]
while True:
    user_input=input("Enter a guest's name or type 'end' to stop.")
    if user_input == "end":
        break
    else:
        invited.append(user_input)
        print(f"{user_input} has been added to the guest list")
name=len(invited)
# print(name)
cal=name*12
for x in invited:
    print(x)
print(f"you have invited {name} guest at the cost of ${cal}")