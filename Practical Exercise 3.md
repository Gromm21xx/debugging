
# Debugging

## Practical Exercise 3: Debugging in Visual Studio Code

## Exercise instructions:

1. Open customer_utils.py in VS Code. 
2. Set a breakpoint on the first line inside the get_preferred_customers function. 
3. Open main.py and modify it to use the following test data: 

        customers = [ Customer("customer1@example.com", 1200, 1), Customer("customer2@example.com", 800, 3), Customer("customer3@example.com", 900, 1), Customer("customer4@example.com", 1100, 2) ]

4. Start the debugger on main.py. 
5. When the breakpoint is hit, use the "Step Over" function to move through the code line by line. 
6. Observe the customers and preferred_customers variables in the Variables pane. 
7. Identify why customer2 is not being added to preferred_customers. 
8. Fix the bug in the get_preferred_customers function. 
9. Restart the debugger and confirm all preferred customers are now included.
